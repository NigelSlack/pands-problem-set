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
# Dependencies : System 'sys' module - proc runtime args
#                System 'math' - to get square root
#                User 'get_integer_input' - get user input of +ve int 
# Arguments    : 'Help' can be accepted as a run time argument
#                None
#
# Versions     :
# 13/02/2019 NS Initial
# 23/02/2019 NS Get the user input from get_integer_input, and loop until CR is returned
#---------------------------------------------------------------------------------------------#

# Import external modules
import sys
import math
import get_integer_input

# Set up multiline help text
hlptext = \
"""\n This code accepts a positive integer input by the user and determines 
 if it is a prime
 Syntax : python solution_05.py [help]"""
       
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
# ref https://stackoverflow.com/questions/18833759/python-prime-number-checker
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
if len(sys.argv)-1:
  if sys.argv[1].upper() == "HELP":   
    print(hlptext)
  else:
    print(" \nNo run time arguments required")
  # end-if  
# end-if

# Keep asking the user to enter positive integers, until they enter CR to exit
# (in get_integer_input). Pass the help text and user prompt to get_integer_input
# and receive the user response back in 'i'
while True:
  i = get_integer_input.get_int_input(hlptext,"Please enter a positive integer ")
  if is_prime(i):
    print(i, "is a prime")
  else:
    print(i, "is not a prime")
  # end-if
# end-while        
# end-program  