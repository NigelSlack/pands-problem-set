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
# Dependencies : None
# Arguments    : 'Help' can be accepted as a run time argument
#                None
#
# Versions     :
# 31/01/2019 NS Initial
# 07/02/2019 NS Include more comments
# 13/02/2019 NS Amend blank line printing, references to include URL, and allow runtime arguments
#-----------------------------------------------------------------------------------------------#

# Define a help text function, to be used if the user inputs 'help'
# This is called with no arguments
# Afterwards, return to main processing.
# ref: https://www.datacamp.com/community/tutorials/functions-python-tutorial
def helptext():

# Surround help text with blank lines for readability - 
# ref https://pythonprogramminglanguage.com/text-output/
   print(" \nThis code outputs the sum of all numbers between one and a positive integer input by the user")
   print("Syntax : python solution_01.py")
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

# Calculate the required value - sum integers from input value down to 1
i2 = 0
while (i1):
  i2=i2+i1
  i1=i1-1
# end-while  
  
# Output value to terminal
print(" \nSum =",i2)
print(" ")

# end-program
