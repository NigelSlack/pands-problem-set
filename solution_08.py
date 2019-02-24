#-------------------------------------------------------------------------------#
# Program      : solution_08.py
# Author       : Nigel Slack
# Language     : python
#
# Function     : Output the current date in the example format :
#                Thursday, February 14th 2019 at 1:09pm
# Syntax       : python solution_08.py
#
# Dependencies : System 'sys' module  - proc runtime args
#                System 'time' module  - to get current date
# Arguments    : 'Help' can be accepted as a run time argument
#                None
#
# Versions     :
# 14/02/2019 NS Initial
#-------------------------------------------------------------------------------#

# Import strftime from the python 'time' module, so the time related functions within it can be used
# ref https://docs.python.org/3/library/time.html#time.strftime
from time import strftime

# Use the python 'sys' module to check for run time arguments. 
# If the user input 'help' output help text, otherwise tell them no arguments are required.
# ref https://stackabuse.com/command-line-arguments-in-python/
import sys
if len(sys.argv)-1:
  if sys.argv[1].upper() == "HELP":
# Output a blank line (for easy readability), then the help text  
# ref https://pythonprogramminglanguage.com/text-output/
    print(" \nThis program outputs the current date and time in the format, eg")
    print("Thursday, February 14th 2019 at 1:09pm")
    print("The required output is given without a run-time argument")
  else:
    print(" \nNo run time arguments required")
  # end-if   
# end-if

# Define the different ordinal indicators in a dictionary variable, to be used in the print command
# ref https://stackoverflow.com/questions/5891555/display-the-date-like-may-5th-using-pythons-strftime…
dic = {'1':'st','2':'nd','3':'rd'}

# Get the dayname (%A), month name (%B) and day number from strftime. Combine them in variable 'x'
x = strftime('%A, %B %d')

# If the second last character of 'x' is a '1', then the day number falls in the range 10 - 19, hence
# the ordinal indicator should be set to 'th'. Otherwise, if the last character of 'x' is a '1' then
# the day number is either 1, 21 or 31, and the ordinal indicator should be 'st'. Similarly if the
# last character is '2' the day is 2 or 22 (maximum day number is 31) the ordinal indicator is 'nd',
# and for a value of '3' (day 3 or 23) it is 'rd'. We can use the last character of 'x' therefore 
# (x[-1]) as an index of the dictionary 'dic'.
# strftime('%Y') provides the year number, '%I' gives the hour (from which any leading zero is 
# stripped, if present), '%M' is the minute value, and '%p' returns 'am' or 'pm'.
print(" ")
print (x + ('th' if x[-2]=='1' else dic.get(x[-1],'th')) + strftime(' %Y at ') + strftime('%I:').lstrip("0") + strftime('%M%p'))
print(" ")

# end-program