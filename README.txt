1) Install sublime Input plugin from here : https://github.com/mavidser/SublimeInput

2) Restart sublime input and now open KeyBindings-user file using : 
        Preferences -> KeyBindings-User

3) Copy contents of SublKeyMap file(Present at Tools/SublEss directory) into it.

4) Now open Sublime Input Settings-User file using :
        Preferences -> Package Settings -> SublimeInput -> Settings-User

5) Copy contents of SublInp file(Present at Tools/SublEss directory) into it.

6) Now install gettc(TopCoder tool for offline practice) from here : https://github.com/seri/gettc

7) Now copy runner.rb and runner.sh (files present at Tools/gettcEss directory) into "/var/lib/gems/1.9.1/gems/gettc-1.10/dist/template/bin/" directory

8) Now copy "create" file(Present at Tools/templates/ directory) into "/bin/" directory and change permissions so that you have right to execute.

9) Now copy "templates/" directory to your home folder.

10) Install BeautifulSoup module(Module for parsing HTML) using "sudo apt-get install python-BeautifulSoup"

11) To work, you need to have directory structures like this (In your home directory) :
     
     |-- Programming
     |   |-- CodeChef
     |   |-- CodeForces
     |   |-- Spoj
     |   `-- TopCoder

     That is :
         -> If you need to do CodeChef Problem you need to work at "~/Programming/CodeChef/" directory and file name should be 
            ContestCode_ProblemCode.cpp
            example : MAY15_CHEFRP.cpp, COOK56_DIVGOLD, .....
         -> If you need to do CodeForces Problem you need to work at "~/Programming/CodeForces/" directory and file name should be
            ContestCode_ProblemCode.cpp
            example : 546_B.cpp, 71_C, 538_B.cpp, .....
         -> If you need to do TopCoder Problem you need to work at "~/Programming/TopCoder/" directory

12) To create a new problem or to continue with the old one, type : create "ProblemName" in terminal.
    That is 
       To do CodeChef problem, type :
            create ContestCode_ProblemCode.cpp
	    example : create MAY15_CHEFRP.cpp, create COOK56_DIVGOLD.cpp, .....
       To do CodeForces problem, type :
            create ContestCode_ProblemCode.cpp
            example : create 71_C.cpp, create 546_B.cpp, .....
       To do TopCoder problem, type :
            create ProblemCode (You can find problem code in problem link, for example I want to do PermutationDiv2 problem and it's link is 
            http://community.topcoder.com/stat?c=problem_statement&pm=13679 So in this ProblemCode is 13679)
            example : create 13679, create 13035, .....	

13) To Compile and run, just press "CTRL + z" in the sublime text. The code then compiles(The Compilation errors will be show if any) and runs.
    The output will be shown and corresponding verdict(TLE, ACC, WA, RTE) will be displayed.
