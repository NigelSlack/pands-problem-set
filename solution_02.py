#-------------------------------------------------------------------------------#
# Program      : solution_02.py
# Author       : Nigel Slack
# Language     : python
#
# Function     : Check to see if the name of the current day begins with a 'T'.
#                Tell the user whether or not it does.
# Syntax       : python solution_02.py
#
# Dependencies : None
# Arguments    : 'Help' can be accepted as a run time argument
#                None
#
# Versions     :
# 13/02/2019 NS Initial
#-------------------------------------------------------------------------------#

# Import the python 'time' module, so the time related functions within it can be used
# ref https://docs.python.org/3/library/time.html#time.strftime
import time

# Use the python 'sys' module to check for run time arguments. 
# If the user input 'help' output help text, otherwise tell them no arguments are required.
# ref https://stackabuse.com/command-line-arguments-in-python/
import sys
if len(sys.argv)-1:
  if sys.argv[1].upper() == "HELP":
# Output a blank line (for easy readability), then the help text  
# ref https://pythonprogramminglanguage.com/text-output/
    print(" \nThis program tells the user if the current day name begins with the letter 'T'")
    print("The required output is given without a run-time argument")
  else:
    print(" \nNo run time arguments required")
  # end-if   
# end-if
        
# From the above 'time' reference, time.strftime with the %a directive returns the abreviated
# weekday name. The first character of this (at offset [0]) provides the required 
# program output.
if time.strftime("%a")[0] == "T":
# Tell the user the day name starts with a 'T'
  print(" \nYes, today begins with a 'T'\n ")
else:
# Tell the user the day name doesn't start with a 'T'
  print(" \nNo, today does not begin with a T\n ")
# end-if      
     