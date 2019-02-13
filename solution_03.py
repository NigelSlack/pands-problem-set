#-------------------------------------------------------------------------------#
# Program      : solution_03.py
# Author       : Nigel Slack
# Language     : python
#
# Function     : Print out all the numbers between 1000 and 10000 that are 
#                divisible by 6 but not by 12
# Syntax       : python solution_03.py
#
# Dependencies : None
# Arguments    : 'Help' can be accepted as a run time argument
#                None
#
# Versions     :
# 13/02/2019 NS Initial
#-------------------------------------------------------------------------------#

# Use the python 'sys' module to check for run time arguments. 
# If the user input 'help' output help text, otherwise tell them no arguments are required.
# ref https://stackabuse.com/command-line-arguments-in-python/
import sys
if len(sys.argv)-1:
  if sys.argv[1].upper() == "HELP":
# Output a blank line (for easy readability), then the help text  
# ref https://pythonprogramminglanguage.com/text-output/
    print(" \nOutput all numbers from 1000 to 10000 divisible by 6 but not 12")
    print("The required output is given without a run-time argument\n ")
  else:
    print(" \nNo run time arguments required\n ")
  # end-if
# end-if  

# Ask the user if they wish to continue using 'click.confirm'. Otherwise this help
# text disappears off-screen with all the numbers being output. If the user enters
# 'y' 'finish' is set to False and the code continues, otherwise it stops.
# ref https://stackoverflow.com/questions/3041986/apt-command-line-interface-like-yes-no-input
  import click   
  finish=True
  if click.confirm('Continue?'):
    finish=False
  # end-if  
  if finish:     
# The user does not wish to continue, so stop. Use 'sys.exit()'.
# ref https://stackoverflow.com/questions/73663/terminating-a-python-script 
    print(" ")
    sys.exit()
  # end-if
# end-if

# Find the lowest number >= 1000 that is divisible by 6. '//' returns the integer
# part of a division operation
# ref https://python-reference.readthedocs.io/en/latest/docs/operators/floor_division.html
i = 6*(1000//6)
if i != 1000:
  i = i+6
# end-if  
  
# If this number is divisible by 12 (using '.is_integer'), add 6 to it. 'i' is then the lowest number
# >= 1000 that is divisible by 6 but not by 12.
# ref https://docs.python.org/3/library/stdtypes.html
if (i/12).is_integer():
  i = i+6
# end-if
    
# Output all numbers from start 'i' <= 10000 adding 12 each time. As the start value is 
# divisible by 6 and not by 12, this gives the required output set.
while i <= 10000:
  print (i)
  i=i+12
# end-while
print(" ")

# end-program 
