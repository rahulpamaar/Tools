#!/usr/bin/python
import sys
import os
import time
import threading
import subprocess
from os.path import expanduser

home = expanduser("~")
Input=[]
Output=[]
Answer=[]
Verdict=[]
Time=[]
Ret=[]

x=sys.argv[0]
y=sys.argv[1]
z=sys.argv[2]
z+='.cpp'


def Code(z):
	a=z[::-1]
	ans=[]
	ans.append('')
	ans.append('')
	flag=0
	for i in a:
		if(i=='/'):
			return ans
		if(flag==1 and i!='_'):
			ans[0]+=i
		if(flag==2):
			ans[1]+=i
		if(i=='_'):
			flag=2
		if(i=='.'):
			flag=1

TL=1  # Time limit (Default : 1 second), change this according to question.

if('CodeForces' in y):
	ret=Code(y)
	pc=ret[0]
	cc=ret[1]
	cc=cc[::-1]
	os.system('python '+home+'/templates/CodeForcesParser '+cc+' '+pc)
	f=open(home+'/Programming/CodeForces/'+z, 'r')
	content=f.read()
	f.close()

if('CodeChef' in y):
	ret=Code(y)
	pc=ret[0]	
	cc=ret[1]
	cc=cc[::-1]
	pc=pc[::-1]
	os.system('python '+home+'/templates/CodeChefParser '+cc+' '+pc)
	
if('TopCoder' in y):
	ret = Code(y)
	pc = ret[0][::-1]
	os.system('make -s sysv')
	sys.exit(0);

class Command(object):
	def __init__(self, cmd):
		self.cmd = cmd
		self.process = None

	def run(self, timeout):
		def target():
			global infile
			myinput=open(home+'/templates/tin','r')
			myoutput=open(home+'/templates/tout','w')
			self.process = subprocess.Popen(self.cmd,bufsize=4096,shell=False,stdin=myinput,stdout=myoutput)
			self.process.communicate()
			myoutput.flush()
		return_code=0
		thread = threading.Thread(target=target)
		thread.start()
		thread.join(timeout)
		if thread.isAlive():
			return_code=123456
			try:
				self.process.terminate()
	 			thread.join()
	 		except AttributeError:
		 		pass
		else:
		 	return_code=self.process.returncode
		return return_code

def Check(x,y,v):
	if(v==123456):
		return "Time Limit Exceeded"
	elif(v==0):
		if(y==''):
			return "No Result"
		L1=len(x)
		L2=len(y)
		for i in xrange(min(L1,L2)):
			if(x[i]!=y[i]):
				return "Wrong Answer at line #"+str(i+1)
		if(L1==L2):
			return "OK"
		else:
			return "Wrong Answer at line #"+str(min(L1, L2)+1)
	else:
		return "Run Time Error"
error=""
print "-------------------------------------------------------------"
if('.cpp' in z):
	Cmd='g++ -g '+z+' -o '+home+'/templates/tocheck'
	p = subprocess.Popen(Cmd,bufsize=4096,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, error = p.communicate()

else:
	os.system('cp '+z+' '+home+'/templates/tocheck')	
	os.system('chmod 777 '+home+'/templates/tocheck')
if(error==''):
	f=open(home+'/templates/input.txt','r')
	filein=f.readlines()
	f.close()

	f=open(home+'/templates/output.txt','r')
	fileout=f.readlines()
	f.close()
	temp=[]
	for i in filein:
		t=i.strip("\n")
		if(t=="'''"):
			Input.append(temp)
			temp=[]
		else:
			temp.append(t)
	Input.append(temp)

	temp=[]
	for i in fileout:
		t=i.strip("\n")
		if(t=="'''"):
			Answer.append(temp)
			temp=[]
		else:
			temp.append(t)
	Answer.append(temp)
	L=len(Input)
	for i in xrange(L):
		print "Test #"+str(i+1)+" : "
		f=open(home+'/templates/tin','w')
		print 'Input : '
		for j in Input[i]:
			if(len(str(j)) > 50 ):
				print ""+j[:50]+' ....'
			else:
				print ""+j
			f.write(j+'\n')
		f.close()
		start_time=time.time()
		command = Command(home+'/templates/tocheck')
		ret=command.run(timeout=int(TL))	
		end_time=time.time()

		f=open(home+'/templates/tout','r')
		temp=f.readlines()
		Output.append([])
		for j in temp:
			t=j.strip('\n')
			Output[i].append(t)
		f.close()
		try:
			Verdict.append(Check(Output[i],Answer[i],ret))
		except IndexError:
			Verdict.append(Check(Output[i],'',ret))
		Time.append(round(end_time-start_time,3))
		Ret.append(ret)

		print "\nExecution Result : "
		if('Run Time Error' in Verdict[len(Verdict)-1]):
			print
			f=open(home+'/templates/tin','w')
			for j in Input[i]:
				f.write(j.strip('\n')+'\n')
			f.close()
			Comm="gdb -q -x "+home+"/templates/gdbin "+home+"/templates/tocheck > "+home+"/templates/gdbout"
			os.system(Comm)
			f=open(home+'/templates/gdbout','r')
			x=f.readlines()
			signaltype=''
			for j in x:
				y=j
				y=y.replace('Reading symbols from '+home+'/templates/tocheck...done.', '')
				y=y.replace('A debugging session is active.', '')
				y=y.replace('Quit anyway? (y or n) [answered Y; input not from terminal]', '')
				y=y.strip('\n').replace('\n','')
				if('Program received' in y):
					temp=y.split(',')
					temp[0]=temp[0][::-1]
					for k in temp[0]:
						if(k==' '):
							break
						else:
							signaltype+=k
					signaltype=signaltype[::-1]
				if(y!='\n' and y!='' and 'Inferior 1' not in y):
					print y
		else:
			for j in Output[i]:
				if(len(str(j)) > 90 ):
					print ""+j[:90]+" ...."
				else:
					print ""+j
		print "\nExpected Output : "
		try:
			for j in Answer[i]:
				if(len(str(j)) > 90):
					print ""+j[:90]+" ...."
				else:
					print ""+j
		except IndexError:
				pass
		if('Run' in Verdict[len(Verdict)-1]):
			Verdict[len(Verdict)-1]+=' ('+signaltype+') '
		print "\nVerdict :",Verdict[len(Verdict)-1],"in",Time[len(Time)-1],"sec"
		tflag=0
		for i in xrange(len(Verdict)):
			if('OK' not in Verdict[i]):
				tflag=1
				break
		print "---------------------------------------------"
	print "Test Results : "
	if(tflag==1):
		for i in xrange(L):
				if((L-i)>10):
					print "  Test #"+str(i+1)+" : "+Verdict[i].strip(' ')+' *'
				else:
					print "  Test #"+str(i+1)+" : "+Verdict[i].strip(' ')
	else:
		print "    All Tests Passed."
	print "---------------------------------------------"
else:
	print "********** COMPILATION ERROR ***************"
	print error
