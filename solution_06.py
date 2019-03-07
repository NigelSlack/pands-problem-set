#---------------------------------------------------------------------------------------------#
# Program      : solution_06.py
# Author       : Nigel Slack
# Language     : python
#
# Function     : Accept an input string from the user and output every second 'word' 
#
# Syntax       : python solution_06.py
#
# Dependencies : System 'sys' module - proc runtime args
# Arguments    : 'Help' can be accepted as a run time argument
#                None
#
# Versions     :
# 13/02/2019 NS Initial
# 15/02/2019 NS Correct the append loop upto len(s)-1 rather than len(s)
# 23/02/2019 NS Put the user input into a loop, until they exit with CR
#               Append to the output var using '+' rather than ',', then there
#               are no brackets and commas to get rid of at the end.
#               If the input contains the Escape Key character, replace with '^',
#               so that the following character is still printed.
# 07/03/2019 NS Put check for escape key into own function, and apply it to the first element
#               in the space separated list (as well as the other elements)
#-----------------------------------------------------------------------------------------------#
import sys

# Define a help text function, to be used if the user inputs 'help'
# This is called with no arguments
# Afterwards, return to main processing.
# ref: https://www.datacamp.com/community/tutorials/functions-python-tutorial
def helptext():

# Surround help text with blank lines for readability - 
# ref https://pythonprogramminglanguage.com/text-output/
   print(" \nThis code accepts an input string from the user and outputs every second")
   print("element (as defined by a space separator).")
   print("Syntax : python solution_06.py [help]")
   return;  

# Check the input string for the Escape Key character. Set it to '^' if found, otherwise it
# stops the following character from being printed 
def check_for_esc_key(ix):
  ixlen = len(ix)
  i=0
  while i < ixlen:
# ref https://stackoverflow.com/questions/5137238/how-to-detect-escape-keypress-in-python
    if ix[i] == chr(27):
      if i == 0:
        ix = '^' + ix[1:]
      else:
# ref https://stackoverflow.com/questions/1228299/change-one-character-in-a-string          
        ix = ix[:i] + '^' + ix[(i+1):] 
      # end-if
    # end-if    
    i = i+1
  # end-while  
  return ix     
         
# Use the python 'sys' module to check for run time arguments. 
# If the user input 'help' output help text, otherwise tell them no arguments are required.
# ref https://stackabuse.com/command-line-arguments-in-python/
if len(sys.argv)-1:
  if sys.argv[1].upper() == "HELP":   
    helptext()
  else:
    print(" \nNo run time arguments required")
  # end-if  
# end-if

# Keep asking the user to enter strings, until they exit by entering CR
while True:
# If the user enters 'help', output help text. Otherwise prompt until they enter
# a string, or CR to exit
  s = ""
  while (not len(s)):
    s = input(" \nPlease enter a string ('Help' for help text, Carriage Return to Exit) : ") 
    if len(s) == 0:
      print(" ")
      sys.exit()
    # end-if  
    if (s.upper() == "HELP"):
      helptext()
      s = ""      
    # end-if    
  # end-while   

# Split the string using the space character as a delimiter into a list that can be indexed,
# replacing multiple spaces with single ones
# ref https://stackoverflow.com/questions/2077897/substitute-multiple-whitespace-with-single-whitespace-in-python
  s=" ".join(s.split())
  s=s.split(" ")
  
# Append every second element in the list to the first element, checking each one for the escape
# key (so that we don't miss characters)
  j=2
  ou = check_for_esc_key(s[0])
  while j <= len(s)-1:
    ix = check_for_esc_key(s[j])
    ou = ou + " " + ix
    j=j+2
  # end-while  
 
  print(ou)  
# end-while
#end-program
    