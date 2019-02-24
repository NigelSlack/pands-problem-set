#-------------------------------------------------------------------------------#
# Program      : solution_10.py
# Author       : Nigel Slack
# Language     : python
#
# Function     : Display a plot of the functions x, x squared and 2 to the power x 
#                in the range [0, 4]
# Syntax       : python solution_10.py
#
# Dependencies : System 'sys' module - proc runtime args
#                System 'matplotlib' - plot the graphs
#                System 'numpy' - used in conjunction with 'matplotlib' for
#                       plotting the graph
#                User 'get_integer_input' - get user input of +ve int 
# Arguments    : 'Help' can be accepted as a run time argument
#                None
#
# Versions     :
# 15/02/2019 NS Initial
# 24/02/2019 NS Ask the user how long they want the graph to display for (rather
#               than having them close it to terminate the program).
#-------------------------------------------------------------------------------#

# Use the python 'sys' module to check for run time arguments. 
# If the user input 'help' output help text, otherwise tell them no arguments are required.
# ref https://stackabuse.com/command-line-arguments-in-python/
import sys
import matplotlib.pyplot as plt 
import numpy as np 
import get_integer_input
    
# Define the help text
hlptext = \
 """\n This program displays a plot of the functions x, x squared and 2 to the power x 
 in the range [0, 4]
 The required output is given without a run-time argument """

if len(sys.argv)-1:
  if sys.argv[1].upper() == "HELP":
# Output a blank line (for easy readability), then the help text, including superscripts  
# ref https://pythonprogramminglanguage.com/text-output/
# ref https://www.dreamincode.net/forums/topic/296846-help-how-do-you-write-superscript/ 
# ref https://rupertshepherd.info/resource_pages/superscript-letters-in-unicode
    print(" \nThis program displays a plot of the functions x, x" + chr(0x00B2) + " and 2" + chr(0x02E3)) 
    print("in the range [0, 4]")
    print("The required output is given without a run-time argument")
  else:
    print(" \nNo run time arguments required")
  # end-if   
# end-if

# Use 'matplotlib' and 'numpy' modules for graph plotting
# ref https://matplotlib.org/tutorials/introductory/pyplot.html

i = get_integer_input.get_int_input(hlptext,"Enter number of seconds to display graph for ")  
      
# setting the x - coordinates 
x = np.arange(0, 4, 0.1) 
# setting the corresponding three sets of y - coordinates 
y1 = np.power(x,1)
y2 = np.power(x,2)
y3 = np.power(2,x)
  
# plotting the points  
plt.plot(x, y1, label = "y=x")
plt.plot(x, y2, label = "y=$x^2$")
plt.plot(x, y3, label = "y=$2^x$")

# Let matplotlib choose the best location for the labels. Also label the axes
# as 'x' and 'y', and rotate the 'y' label, otherwise it's on it's side
# ref https://stackoverflow.com/questions/27671748/how-to-print-y-axis-label-horizontally-in-a-matplotlib-pylab-chart
plt.legend(loc='best') 
plt.xlabel("x")   
plt.ylabel("y",rotation=0)

# Show the plot for a specified number of seconds
# ref https://stackoverflow.com/questions/40395659/view-and-then-close-the-figure-automatically-in-matplotlib?rq=1 

plt.show(block=False)
plt.pause(i)
plt.close()
# end-program