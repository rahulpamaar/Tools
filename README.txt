1) Install sublime Input plugin from here : https://github.com/mavidser/SublimeInput

2) Restart sublime input and now open KeyBindings-user file using : 
        Preferences -> KeyBindings-User

3) Copy content of SublKeyMap file(Present at Tools/SublEss directory) into it.

4) Now open Sublime Input Settings-User file using :
        Preferences -> Package Settings -> SublimeInput -> Settings-User

5) Copy content of SublInp file(Present at Tools/SublEss directory) into it.

6) Now install gettc(TopCoder tool for offline practice) from here : https://github.com/seri/gettc

7) Now copy runner.rb and runner.sh (files present at Tools/gettcEss directory) into "/var/lib/gems/1.9.1/gems/gettc-1.10/dist/template/bin/" directory

8) Change permissions of runner.sh, runner.rb files as shown :<pre>
      sudo chmod 755 /var/lib/gems/1.9.1/gems/gettc-1.10/dist/template/bin/runner.sh
      sudo chmod 755 /var/lib/gems/1.9.1/gems/gettc-1.10/dist/template/bin/runner.rb</pre>
      
9) Now reset the gettc by 
      gettc reset
      
10) Now copy "create" file(Present at Tools/templates/ directory) into "/bin/" directory and change permissions so that you have right to execute. That is : 
      sudo chmod 755 /bin/create

11) Now copy "templates/" directory to your home folder. And make sure that you are the owner of this directory.

12) Install BeautifulSoup module(Python module for parsing HTML) using 
      sudo apt-get install python-BeautifulSoup

13) To work, you need to have directory structure like this (In your home directory) :
     ~/
     |-- Programming
     |   |-- CodeChef
     |   |-- CodeForces
     |   |-- Spoj
     |   `-- TopCoder

     That is :
         -> If you need to do CodeChef Problem you need to work in "~/Programming/CodeChef/" directory and file name should be 
            ContestCode_ProblemCode.cpp
            example : MAY15_CHEFRP.cpp, COOK56_DIVGOLD.cpp, .....
         -> If you need to do CodeForces Problem you need to work in "~/Programming/CodeForces/" directory and file name should be
            ContestCode_ProblemCode.cpp
            example : 546_B.cpp, 71_C, 538_B.cpp, .....
         -> If you need to do TopCoder Problem you need to work in "~/Programming/TopCoder/" directory

14) To create a new problem or to continue with the old one, type : create "ProblemName" in terminal.
    That is 
       To do CodeChef problem, type :
            create ContestCode_ProblemCode.cpp
-	    example : create MAY15_CHEFRP.cpp, create COOK56_DIVGOLD.cpp, .....
       To do CodeForces problem, type :
            create ContestCode_ProblemCode.cpp
            example : create 71_C.cpp, create 546_B.cpp, .....
       To do TopCoder problem, type :
            create ProblemCode (You can find problem code in problem link, for example I want to do PermutationDiv2 problem and it's link is 
            http://community.topcoder.com/stat?c=problem_statement&pm=13679 So in this ProblemCode is 13679)
            example : create 13679, create 13035, .....	

15) To Compile and run, just press "CTRL + z" in the sublime text. The code then compiles(The Compilation errors will be show if any) and runs.
    The output will be shown and corresponding verdict(TLE, ACC, WA, RTE) will be displayed.
That's it.
-----------------------------------------
NOTE :
   1) If you have your own template for cpp, then put that in ~/templates/template.cpp file.
   2) This works only for cpp. If your code is java/python/c .... it doesn't work so don't use this. 
      This is one limitation.
   3) Report bugs at : achaitanyasai[AT]gmail[AT]com
