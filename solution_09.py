#---------------------------------------------------------------------------------------------#
# Program      : solution_09.py
# Author       : Nigel Slack
# Language     : python
#
# Function     : Read a text file, with the filename passed as a runtime argument,
#                and output every second line.
#
# Syntax       : python solution_09.py
#
# Dependencies : None
# Arguments    : 'Help' can be accepted as a run time argument
#                None
#
# Versions     :
# 15/02/2019 NS Initial
#-----------------------------------------------------------------------------------------------#

# Define a help text function, to be used if the user inputs 'help'
# This is called with no arguments
# Afterwards, return to main processing.
# ref: https://www.datacamp.com/community/tutorials/functions-python-tutorial
def helptext():

# Surround help text with blank lines for readability - 
# ref https://pythonprogramminglanguage.com/text-output/
   print(" \nThis code reads a text file, with the filename passed as a runtime argument,")
   print("and outputs every second line.")
   print("Syntax : python solution_09.py input-filename\n ")
   sys.exit();  
   
# Use the python 'sys' module to check for run time arguments. 
# If the user input 'help' output help text.
# If no runtime param was passed, tell the user they must run the program with a 
# filename argument.
# ref https://stackabuse.com/command-line-arguments-in-python/
import sys

if len(sys.argv)-1:
  if sys.argv[1].upper() == "HELP":   
    helptext()
  # end-if
else:
  print(" \nThis code must be run with a runtime argument of a text filename, eg")
  print("python solution_09.py testtext.txt\n ")
  sys.exit()
# end-if
        
i = False

# Check the file extension is '.txt'. If not, output a message and stop.
# ref https://stackoverflow.com/questions/5899497/checking-file-extension
if not sys.argv[1].lower().endswith('.txt'):
  print(" \nInput file must be a text file (file extension '.txt')\n ")
  sys.exit()
# end-if

# Open the text file for read-only (default mode, 'b' not required as it's not binary), with
# the system default for buffering (no third argument passed to 'open')
# ref https://docs.python.org/2/library/functions.html#open
rf = True

# Use 'with open' to automatically close the file when finished
# ref https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
with open(sys.argv[1]) as f:
  for line in f:
    if rf:
      print(line)
      rf = False
    else:  
      rf = True
    # end-if
  # end-for
# end-with    