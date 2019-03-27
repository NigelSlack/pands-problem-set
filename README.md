# pands-problem-set
GMIT HDip Programming and Scripting problem set solutions. Semester 1, 2019

**Summary**
This project set consists of eleven short Python programs, described below, and one text file used for testing the program
'solution_09.py' These programs utilise the 'sys', 'time' and 'math' modules from the Python standard library, plus the modules 'matplotlib', 'numpy' and 'click'. The program 'get_integer_input' is user written code imported by the programs 
solution_01/04/05/10.py 
solution_01 .. solution_10.py are the ten base programs.  

**Solution_01.py**  
  Output the sum of integers, up to a positive integer input by the user.
  eg for a user input of '4' the output would be '10'
  No run time arguments required, although 'help' is accepted.
  Syntax : python solution_01.py [help]
  
**Solution_02.py**
  Determine if the name of the current day begins with a 'T'.
  eg if the current day is Thursday the output would be "Yes, today begins with a 'T'"
     on a Wednesday the output would be No, today does not begin with a 'T'
  No run time arguments required, although 'help' is accepted.
  Syntax : python solution_02.py [help] 
  
**Solution_03.py**
  Print all numbers from 1,000 to 10,000 divisible by 6 but not 12
  The output consists of the numbers 1002, 1014, 1026 ... 9990
  No run time arguments required, although 'help' is accepted. If 'help' is input, the user is asked if they wish to continue
  so that they can read the help text before it is pushed off screen by the output.
  Syntax : python solution_03.py [help]  
  
**Solution_04.py**
  Accept a positive integer input from the user. Apply the following iteration until the number 1 is obtained. If the number is
  even divide by 2, if it is odd multiply by 3 and add 1. Output the number after each iteration.
  eg for an input of 5 the output would be 5 16 8 4 2 1
  No run time arguments required, although 'help' is accepted.
  Syntax : python solution_04.py [help] 
  
**Solution_05.py**
  Determine if a positive integer input by the user is prime or not
  eg for an input of 7 output '7 is a prime', for an input of 8 output '8 is not a prime'
  No run time arguments required, although 'help' is accepted.
  Syntax : python solution_05.py [help] 
  
**Solution_06.py** 
  Output every second 'word' (space separated element) of a string input by the user
  eg for an input 'H is the 1st element of the periodic table' the output is 'H the element the table'  
  No run time arguments required, although 'help' is accepted.
  Syntax : python solution_06.py [help]   
  
**Solution_07.py** 
  Output the square root of a positive floating point number input by the user. Round to the number of decimal places in the input
  number. Two methods of calculating the root are applied, with the time taken for each being displayed (using the Matplotlib library, and
  using the Newton iteration), though just one result is output. 
  eg an input of 7.00 gives an output of 2.65, an input of 3.6 yields 1.9
  No run time arguments required, although 'help' is accepted.
  Syntax : python solution_07.py [help]
  
**Solution_08.py**
  Print the current date and time in the format 'Monday, January 10th 2019 at 1:15pm'
  No run time arguments required, although 'help' is accepted.
  Syntax : python solution_08.py [help]
  
**Solution_09.py**  
  Output every second line of a text file (type .txt).
  eg for an input file containing :
    Line 1
    Line 2
    Line 3
    Line 4
    
  the output is :
    Line 1
    Line 3
    
  The name of the text file must be input as a run time argument.
  Syntax : python solution_09.py [help] text-file , eg python solution_09.py testtext.txt
  ( a test text file is provided, named Testtext.txt)
  
**Solution_10.py**  
  Plot x, x squared and 2 to the power x in the range [0, 4]. 
  Provide a line plot of the 3 specified functions. Ask the user how many seconds they wish the display to last for.
  No run time arguments required, although 'help' is accepted.
  Syntax : python solution_10.py [help]
  
**Get_integer_input** 
  Get a positive integer input from the user. Output an error message for incorrect inputs and re-prompt.
  Requires two run time arguments - help text and a user prompt.
  Returns the integer input by the user to the calling program.
  eg Syntax : i=get_integer_input.get_int_input(hlptext,"Please enter a positive integer ")
  Used by Solution_01/04/05/10
                    
                 
