#---------------------------------------------------------------------------------------------#
# Program      : solution_07.py
# Author       : Nigel Slack
# Language     : python
#
# Function     : Accept a positive floating point number input from the user and output the
#                approximate square root (or the exact square root if found)
#
# Syntax       : python solution_07.py
#
# Dependencies : System 'sys' module  - proc runtime args
#                System 'math' module  - to get square root
# Arguments    : 'Help' can be accepted as a run time argument
#                None
#
# Versions     :
# 14/02/2019 NS Initial
# 24/02/2019 NS Allow for exponential inputs. Also deal with 'NaN' and 'Infinity'
#-----------------------------------------------------------------------------------------------#
import sys
import time

# Check how long it takes to load 'math' module - for comparing two ways of getting the 
# square root
# ref https://docs.python.org/2/library/time.html
tload=time.time()
import math
tload=(time.time()-tload)

# Define a help text function, to be used if the user inputs 'help'
# This is called with no arguments
# Afterwards, return to main processing.
# ref: https://www.datacamp.com/community/tutorials/functions-python-tutorial
def helptext():

# Surround help text with blank lines for readability - 
# ref https://pythonprogramminglanguage.com/text-output/
   print(" \nThis code outputs the (approximate) square root of a positive number input by the user")
   print("Exponents may be used, eg 2.345e5 or 1.764e-10, but for larger values small floating point")
   print("errors may occur. The number of decimal places output will be the same as for the input,")
   print("except for exact square roots when fewer places may be displayed, eg an input of 3.0 will")
   print("give one decimal place, whereas 3.000 will yield 3 places. The square root is calculated")
   print("using 2 methods - an external library call 'math.sqrt', and the Newton iteration, with the")
   print("timings given for both.")
   print("Syntax : python solution_07.py [help]")
   return;  
   
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

def get_user_input():
# Get input from user until a positive number is entered
# If the user enters 'help', output help text. For any other input that is not a positive
# number display an error message and continue.
  ok=False
  dp2=1
  while (not ok):
    exp=0
    f = input(" \nPlease enter a positive number ('Help' for help text,'CR' to exit) : ")

# User entered CR, so stop processing
    if len(f) == 0:
      print(" ")
      sys.exit()
    # end-if  

# Check if the user entered an exponential value    
    f=f.lower()      
    ex=f.find("e")
    if ex > 0:
      f1 = f
      exponent = True
      try: 
# Check if the input is numeric with 'float'
        f1 = float(f1)
      except ValueError:
        exp = 0
        exponent = False
      # end-try
              
# If the exponent value is positive, we'll just print to one decimal place - use
# 'exp' as an indicator for this. Look for a '-' sign starting at position 1 in 
# the input string, in case the input was a negative number.
# ref https://www.tutorialspoint.com/python/string_find.htm 
      if exponent:
        if f.find("-",1) < 0: 
          exp = -1
        else:
# Get the exponent part of the input, 'eg in 10e-5' the 'e-5', and delete it.
# The number can then be processed as for a non-exponent, before adding decimal
# places in at the end if the exponent is negative.     
          exp=int(f[(ex+2):len(f)])  
        # end-if  
        f=f[0:ex]
      # end-if  
    # end-if
        
# Check if the user input contains a decimal point. If the user enters a whole number, the
# output will be given to one decimal place, otherwise it's given to the same number of
# decimal places entered by the user.
    dp=f.find(".")
# If the user input's last character is '.', with no following numerals, append 0 
# to the end of the input. This then reflects a whole number input followed by '.0'.
# If the first character is a '.', append '0' to the front of the input, so that,
# eg .12 becomes 0.12
    if dp >= 0:
      if dp == len(f)-1: f = f+"0" 
      if not dp: f = "0"+f
      dp=len(f.split('.')[1])
    # end-if  

# Check for numeric input. If the input is a number, 'NaN', or 'Inf[inity]',
# then 'float' will not generate an error. For an exponent use the float
# value we've already obtained - f1
# ref: https://pynative.com/python-check-user-input-is-number-or-string/
    try:
      if not exp:
        f = float(f)
      else:
        f = f1 
      # end-if   
      fs=str(f)
# 'nan' (not a number) and 'inf' (infinity) pass 'float' test, but are not 
# positive integers
      if fs == "nan" or fs == "inf":
        print(" \nInput must be a positive number") 
      else:
        if f > 0:
          ok=True
# If the input is a whole number we'll note it so that we output a whole number
          if f.is_integer() and dp > 0:
            dp2=dp
            dp = -1
          # end-if
        else:  
          print(" \nInput must be a positive number")
        # end-if    
    except ValueError:
      try: 
        f = int(f)
        f = float(f)
# If the input was positive than it is valid. We can stop prompting for input and
# and continue processing
        if f > 0: ok = True
      except ValueError:
# Output help text if the user entered 'help', otherwise tell them they must enter a
# positive number      
        if (f.upper() == "HELP"):
          helptext()
        else:       
          print(" \nInput must be a positive number")
      # end-if    
    # end-try
  # end-try      
# end-while
  
# We'll output at least one decimal place for all inputs (other than when the input
# is a whole number and so is the square root - for which variable 'dp' is used)
  if dp2 < 1: dp2 = 1
  return(f,dp,dp2,exp)
# end get_user_input  

while True:
# Get the user input. The return contains the number input; 'dp' for if an integer
# is input and the square root is an integer (so no decimal place will be output);
# 'dp2' to otherwise show the number of decimal places to output, and an indicator "exp"
# for exponent input
  f, dp, dp2, exp = get_user_input()
  if dp > dp2: dp2 = dp
 
# If there was a positive exponent we'll just output one decimal place, otherwise we'll
# add the value of the exponent to the number of decimal places to output
  if exp:
    if exp < 0:
      dp = 1
      dp2 = 1
    else:
      dp2 = (dp2 + exp) - 1
    # end-if
  # end-if    
  
# We'll use two ways of getting the square root - the 'math.sqrt' library call, 
# and an iteration using the Newton method. In the output we'll show how long each 
# method took (but we'll just display one output value)
  
      
# Get the square root using the 'math' module
# ref https://docs.python.org/2/library/math.html    

# Find the start time 
  t1=time.time()
  f2=math.sqrt(f)
# Check how long this method took. For the first time someone gets a square root
# whilst running the code, we'll add on how long it took to load the 'math' module.
  t1=(time.time()-t1)+tload
  tload = 0
  
# Set dpx to the number of decimal places in the input number
  if dp < 0 or exp:
    if f2.is_integer(): 
      dpx= (-1)
    else:
      dpx=dp2*(-1) 
    # end-if   
  else:
    dpx=dp*(-1)
  # end-if


# Get the square root using the Newton iteration method   
# ref https://tour.golang.org/flowcontrol/8 and 
# Ian McLoughlin GMIT 'Programming and Scripting' lecture week 8 (Newton)

# Get the exponential (power 10) value of the input number. This is used to 
# get an estimate of the first value to try. The last 3 characters resulting from the 'format'
# command give the exponent, eg +00, -01.
# ref https://stackoverflow.com/questions/51502747/python-convert-float-notation-to-power-of-10-scientific-notation
 
# Get the start time of this method
  t2=time.time() 
  fx = format(f,'.0e')
# Get the last 3 characters
# rf https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string
  fx=fx[-3:]
  fx=int(fx)
  if fx < 0: fx = fx - 1
 
# Use an initial estimate based on the input value expressed as 'x*(10**2n)'. For 'x' < 10 use 
# 2 * (10**(n/2)) otherwise use 6 - this is based on the geometric mean of the ranges considered.
# ref https://en.wikipedia.org/wiki/Methods_of_computing_square_roots
  if (abs(fx)%2==0): 
    est = 2*(10**(int(fx/2)))
  else:
    est = 6*(10**(int(fx/2)))
  # end-if  
  
# Find the estimate using the Newton method, to the number of decimale places input by the user.
  while abs((est*est)-f) > (10**dpx):
    est -= ((est*est)-f)/(2*est)
# Find how long this method took
  t2=time.time()-t2
  
  f5=str(f)
  f6=str(f2)
  exact=False
  
  if dp < 0 or exp:
    if f2.is_integer(): 
# input was a whole number
      f3=int(f2)
      f=int(f)
      exact=True
    else:  
# Round the output to the same number of DPs as the input
# ref https://www.tutorialspoint.com/python/number_round.htm
      if dp2 > 1:
        f3=round(f2,dp2)
      else:
        f3=round(f2,1)
      # end-if
    # end-if  
  else:    
    f3=round(f2,dp)
  # end-if  
      
# Check if we have the exact square root. Output 'approx' if not. If the 
# square root of the input number has fewer characters than the input number
# then it's an exact root
  if exact or (len(f6) < len(f5)):
    print("The square root of",f,"is",f3)
  else:
    print("The square root of",f,"is approx",f3)      
  # end-if
  print("(Time taken by 'math.sqrt'   - ",t1," seconds)")
  print("(Time taken by Newton method - ",t2," seconds)")
# end-while
# end-program