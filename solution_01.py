#---------------------------------------------------------------------------------------------#
# Program      : solution_01.py
# Author       : Nigel Slack
# Language     : python
#
# Function     : Accept a positive integer input from the user and output the sum
#                of all integers from 1 to the input value
#
# Syntax       : python solution_01.py
#
# Dependencies : System 'sys' module - proc runtime args
#                User 'get_integer_input' - get user input of +ve int 
# Arguments    : 'Help' can be accepted as a run time argument
#                None
#
# Versions :
# 31/01/2019 NS Initial
# 07/02/2019 NS Include more comments
# 13/02/2019 NS Amend blank line printing, references to include URL, and allow runtime arguments
# 13/02/2019 NS Insert/correct 'end-if' comments
# 23/02/2019 NS Put user input in loop, until user terminates with Carriage Return
#               Get user input from external module 'get_positive_int_input'
#-----------------------------------------------------------------------------------------------#

# Import required modules
import sys
import get_integer_input

# Define help text for this program as multiline string, with newline characters
# ref https://www.python-course.eu/python3_passing_arguments.php
# ref https://stackoverflow.com/questions/11497376/how-would-i-specify-a-new-line-in-python
hlptext = """\nThis code outputs the sum of all numbers between one and a positive integer input by the user
             \nSyntax : python solution_01.py [help]"""

# Use the python 'sys' module to check for run time arguments. 
# If the user input 'help' output help text, otherwise tell them no arguments are required.
# ref https://stackabuse.com/command-line-arguments-in-python/
if len(sys.argv)-1:
  if sys.argv[1].upper() == "HELP":   
    print(hlptext)
  else:
    print(" \nNo run time arguments required")
  # end-if  
# end-if
        
# Keep asking the user to enter positive integers, or help, until they terminate
# the process by just entering Carriage Return (in get_integer_input).
while True:

# Pass the help text, and user prompt, as arguments to get_integer_input. Receive back the integer
# input by the user. 
# ref https://www.python-course.eu/python3_functions.php
  i = get_integer_input.get_int_input(hlptext,"Please enter a positive integer ")
    
# Calculate the required value - sum integers from input value down to 1
  i2 = 0
  while (i):
    i2=i2+i
    i=i-1
  # end-while  
  
# Output value to terminal
  print(" \nSum =",i2)
  
# end-while  
# end-program
