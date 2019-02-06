#-------------------------------------------------------------------------------#
# Program      : solution1.py
# Author       : Nigel Slack
# Language     : python
#
# Function     : Accept a positive integer input from the user and output the sum
#                of all integers from 1 to the input value
#
# Syntax       : python solution1.py
#
# Dependencies : None
#
# Versions     :
# 31/01/2019 Initial
#-------------------------------------------------------------------------------#

# Set up help text
def helptext():
   print(" ")
   print("This code outputs the sum of all numbers between one and a positive integer input by the user")
   print("Syntax : python solution1.py")
   print(" ") 
   return;  

i = False

# Get input from user until a positive integer is entered
while (not i):
    i = input("Please enter a positive integer ('Help' for help text) : ") 
    if i.isdigit():
      i1 = int(i) 
      if (i1 < 1):   
        print(" ","Input integer must be positive"," ",sep='\n') 
        i = False
     # end-if   
    else:
      if (i.upper() == "HELP"):
        helptext()
      else:       
        print(" ","Input must be a positive integer",sep='\n')
        print(i," ",sep='\n')
      i = False
    # end-if    
# end-while    

# Calculate the required value
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
