#-------------------------------------------------------------------------------#
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
#
# Versions     :
# 31/01/2019 NS Initial
# 07/02/2019 NS Include more comments
#-------------------------------------------------------------------------------#

# Output help text. This is called with no arguments, by the user entering 'help'
# Afterwards, return to the main processing.
# Ref: datacamp.com 'How to define a function'
def helptext():
   print(" ")
   print("This code outputs the sum of all numbers between one and a positive integer input by the user")
   print("Syntax : python solution_01.py")
   print(" ") 
   return;  

i = False

# Get input from user until a positive integer is entered
# If the user enters 'help', output help text. For any other input that is not a positive
# integer display an error message and continue.
while (not i):
    i = input("Please enter a positive integer ('Help' for help text) : ") 
# Check for numeric input.
# Ref: pynative.com - check if user input is a number or string
    if i.isdigit():
      i1 = int(i) 
# Make sure it's in integer form and is >= 1
      if (i1 < 1):   
        print(" ","Input integer must be positive"," ",sep='\n') 
        i = False
      # end-if   
    else:
# Output help text if the user entered 'help', otherwise tell them they must enter a
# positive integer
      if (i.upper() == "HELP"):
        helptext()
      else:       
        print(" ","Input must be a positive integer",sep='\n')
        print(i," ",sep='\n')
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
print(" ")
print("Sum =",i2)
print(" ")

# end-program
