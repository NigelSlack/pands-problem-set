#---------------------------------------------------------------------------------------------#
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
# Dependencies : None
# Arguments    : 'Help' can be accepted as a run time argument
#                None
#
# Versions     :
# 13/02/2019 NS Initial
# 
#-----------------------------------------------------------------------------------------------#

# Define a help text function, to be used if the user inputs 'help'
# This is called with no arguments
# Afterwards, return to main processing.
# ref: https://www.datacamp.com/community/tutorials/functions-python-tutorial
def helptext():

# Surround help text with blank lines for readability - 
# ref https://pythonprogramminglanguage.com/text-output/
   print(" \nThis code accepts a positive integer input by the user")
   print("It performs the following operations on the input number : ")
   print("If the number is even it divides by two to give the next value.")
   print("If the number is odd it multiplies by 3 and adds one.")
   print("The result is output at each step until the value '1' is reached.")
   print("Syntax : python solution_04.py")
   return;  
   
# Use the python 'sys' module to check for run time arguments. 
# If the user input 'help' output help text, otherwise tell them no arguments are required.
# ref https://stackabuse.com/command-line-arguments-in-python/
import sys
if len(sys.argv)-1:
  if sys.argv[1].upper() == "HELP":   
    helptext()
  else:
    print(" \nNo run time arguments required")
# end-if

i = False

# Get input from user until a positive integer is entered
# If the user enters 'help', output help text. For any other input that is not a positive
# integer display an error message and continue.
while (not i):
    i = input(" \nPlease enter a positive integer ('Help' for help text) : ") 
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
# Output help text if the user entered 'help', otherwise tell them they must enter a
# positive integer
      if (i.upper() == "HELP"):
        helptext()
      else:       
        print(" \nInput must be a positive integer")
        print(i)
      i = False
      # end-if
    # end-if    
# end-while    

# Convert 'i' to an integer
# ref https://docs.python.org/2/library/functions.html#int
i = int(i)

# Initialise the output variable to the user input value
ou = i

while (i!= 1):
# Use the modulo operator to check if 'i' is even. No remainder means it is,
# so divide by 2, otherwise *3 +1
# ref http://interactivepython.org/runestone/static/StudentCSP/CSPTurtleDecisions/oddEven.html
  if not (i%2):
    i = i/2
  else:
    i = (i*3)+1
# Append the value of 'i' to the output variable 'ou' after each step
  ou = ou,int(i)
  # end-if  
# end-while  
  
# Remove brackets and commas from the output (put in by the append)
# ref https://docs.python.org/2/library/string.html
ou = str(ou).replace("(","")
ou = str(ou).replace(")","")
ou = ou.replace(',','')
print(ou)
print(" ")

# end-program