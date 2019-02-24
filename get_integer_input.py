#---------------------------------------------------------------------------------------------#
# Program      : get_integer_input.py
# Author       : Nigel Slack
# Language     : python
#
# Function     : Receive a positive integer input from the terminal. Keep looping
#                until a valid integer has been entered, or stop if the user
#                enters Carriage Return with no input.
# Syntax       : python get_integer_input.py (helptext,user-prompt)
#
# Dependencies : System 'sys' module  - proc runtime args
#                Called by:
#                  solution_01.py
#                  solution_04.py
#                  solution_05.py
#                  solution_10.py
#                eg get_integer_input.get_int_input(hlptext,"Please enter a positive integer ")
# Arguments    : The first argument should contain helptext
#                The second argument should contain text for a user prompt
#                Return the user input integer to the calling program
#
# Versions     :
# 15/02/2019 NS Initial
# 
#---------------------------------------------------------------------------------------------#
import sys 

# Check if the input variable holds a floating point number
# ref https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float
def is_number(s):
  try:
    float(s)
    return True
  except ValueError:
    return False  
  # end-try 
# end-module  

# Get input from user until a positive integer is entered
# If the user enters 'help', output help text. For any other input that is not a positive
# integer display an error message and continue.
def get_int_input(hlptext,prompttext): 
 i = False
 
 while (not i):
    i = input(" \n" + prompttext + " ('Help' for help text; Carriage Return to exit) : ") 

# The user entered CR with no input, so terminate 
    if len(i) == 0:
      print(" ")
      sys.exit()
# Check for numeric input.
# ref: https://pynative.com/python-check-user-input-is-number-or-string/
    if i.isdigit():
      i1 = int(i) 
# Make sure it's in integer form and is >= 1
      if (i1 < 1):   
        print(" \nInput integer must be positive") 
        i = False
      # end-if   
    else:
# See if the input is a floating number, in case the user entered eg 4.0, which is allowed
      if is_number(i):
        i=float(i)
# If it is floating point check if the decimal value is zero (residual of division by '1' is '0.0')
# If not then it's not an integer.        
        if (i%1) != 0.0:
          print(" \nInput must be a positive integer")
          i = False
        else: 
          i=int(i)
          if (i<1):
            print(" \nInput integer must be positive")
            i=False
          # end-if
        # end-if    
      else:
# Output help text if the user entered 'help', otherwise tell them they must enter a
# positive integer
        if (i.upper() == "HELP"):
          print(hlptext)
        else:       
          print(" \nInput must be a positive integer")
          print(i)
        # end-if  
        i = False
      # end-if  
    # end-if    
# end-while    

# Convert 'i' to an integer
# ref https://docs.python.org/2/library/functions.html#int
 i = int(i)

# Return the integer input by the user to the calling program
 return i

# end-module
# end-program