#---------------------------------------------------------------------------------------------#
# Program      : solution_05.py
# Author       : Nigel Slack
# Language     : python
#
# Function     : Accept a positive integer input from the user.  
#                Tell the user if it is a prime
#
# Syntax       : python solution_05.py
#
# Dependencies : None
# Arguments    : 'Help' can be accepted as a run time argument
#                None
#
# Versions     :
# 13/02/2019 NS Initial
# 
#-----------------------------------------------------------------------------------------------#

# Use the square root of the input number when checking if the input is a prime
# Import this function from the 'math' module
import math

# Define a help text function, to be used if the user inputs 'help'
# This is called with no arguments
# Afterwards, return to main processing.
# ref: https://www.datacamp.com/community/tutorials/functions-python-tutorial
def helptext():

# Surround help text with blank lines for readability - 
# ref https://pythonprogramminglanguage.com/text-output/
   print(" \nThis code accepts a positive integer input by the user and determines ")
   print("if it is a prime")
   print("Syntax : python solution_05.py")
   return;  
   
def is_prime(n1):
# Convert the input to an integer
  n = int(n1)
# 2 is a prime. No even number (residual = 0 on division by 2) is prime and nor 
# is 1
  if n == 2:
    return True
  # end-if    
  if n % 2 == 0 or n <= 1:
    return False
  # end-if    

# If there is no whole number divisor from 3 upto the square root of the number
# (check upto the integer part of the square root + 1), then the number is a prime.
# If n = ab where n,a,b are positive integers and 2 <= a,b <= n-1, then set a<=b.
# a.a is then <= n, therefore at least one of the factors is <= square root n
  sqr = int(math.sqrt(n)) + 1   
  for divisor in range(3, sqr, 2):   
    if n % divisor == 0:
      return False
    # end-if
  # end-for        
  return True   
   
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
      # end-if  
      i = False
    # end-if    
# end-while    


if is_prime(i1):
  print(i1, "is a prime")
else:
  print(i1, "is not a prime")
# end-if
print(" ")
        
# end-program  