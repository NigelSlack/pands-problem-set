#--------------------------------------------------------------------------------------------------------#
# Program      : solution_04.py
# Author       : Nigel Slack
# Language     : python
#
# Function     : Accept a positive integer input from the user.  
#                Iterate from this value : If even, i(user input)=i/2. 
#                If odd i=(i*3)+1. Until i=1
#
# Syntax       : python solution_04.py
#
# Dependencies : System 'sys' module - proc runtime args
#                User 'get_integer_input' - get user input of +ve int 
# Arguments    : 'Help' can be accepted as a run time argument
#                None
#
# Versions     :
# 13/02/2019 NS Initial
# 13/02/2019 NS Correct 'end-if' comments
# 15/02/2019 NS Allow for floating point input with a zero decimal point value, eg 9.0
#               Get user input from get_integer_input module, and loop until the user enters CR
#               Use int(float) for values added to the output to avoid having to remove brackets and commas
#---------------------------------------------------------------------------------------------------------#

import sys
import get_integer_input

# Define the help text as a multiline variable
# ref https://docs.python.org/3/tutorial/introduction.html
hlptext = \
"""\n This code accepts a positive integer input by the user.          
 It performs the following operations on the input number :
 If the number is even it divides by two to give the next value.
 If the number is odd it multiplies by 3 and adds one.
 The result is output at each step until the value '1' is reached.
 Syntax : python solution_04.py [help]"""
   
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

# Keep looping until the user enters CR, then stop (in get_integer_input)
while True:
# Pass the help text and user prompt to get_integer_input, and get back a +ve integer
  i = get_integer_input.get_int_input(hlptext,"Please enter a positive integer ")

# Initialise the output variable to the user input value
  ou = str(i)

  while (i!= 1):
# Use the modulo operator to check if 'i' is even. No remainder means it is,
# so divide by 2, otherwise *3 +1
# ref http://interactivepython.org/runestone/static/StudentCSP/CSPTurtleDecisions/oddEven.html
    if not (i%2):
      i = i/2
    else:
      i = (i*3)+1
    # end-if
# Append the value of 'i' to the output variable 'ou' after each step. Use 'int(float)' to remove '.0' from i values
# ref https://stackoverflow.com/questions/385325/dropping-trailing-0-from-floats
    ou = ou + (" ") + str(int(float(i))) 
  # end-while  
  
  print(ou)
# end-while
# end-program