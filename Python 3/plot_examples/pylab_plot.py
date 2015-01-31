# Plotting curves with Pylab. Python ver. 2.7

import pylab
import math 


def second_pol_plot(A, B, C, start, stop, step=1):
    '''(number, number, number, int, int) --> number
    Inserting the coefficients A, B, C and start and end point
    for selected range, plots the curve for the function:
    A * x ** 2 + B * x + C. Step value is default 1.
    Change step value to 0.1 for smooth curves.
    '''

    x_axe = []  # x values
    y_axe = []  # y values

    x = start
    while x <= stop:
        y = A * x ** 2 + B * x + C  # Polynomia.
        x_axe.append(round(x, 2))   # Appending rounded x value to x_axe
        y_axe.append(round(y, 2))   #Appending rounded y value to y_axe.
        x += step   # Step value - setting new value for x.    
    
    # Seraching for solutions
    D = B ** 2 - (4 * A * C)
    print "D =", D
    
    single_point = []
    double_point = []
    if D == 0:
        x = - B / (2 * A)
        y = A * x ** 2 + B * x + C
        single_point.append([x, y])
    elif D > 0:
        x1 = (-B - math.sqrt(D)) / (2 * A)        
        y1 = A * x1 ** 2 + B * x1 + C
        x2 = (-B + math.sqrt(D)) / (2 * A)        
        y2 = A * x2 ** 2 + B * x2 + C
        double_point.append([round(x1, 2), round(y1, 2)])
        double_point.append([round(x2, 2), round(y2, 2)])
    elif D < 0:
        print "No roots found."

    # Printing the result

    if len(single_point) != 0:
        print "Single root found. x =", single_point[0]
        print "Coordinate set =", single_point
    elif len(double_point) != 0:
        print "Double root found. x =", double_point[0][0], "or x =", double_point[1][0]
        print "Coordinate set root 1 =", double_point[0]
        print "Coordinate set root 2 =", double_point[1]    
        
    # Uncomment the following lines to print
    # x and y values to the prompt.
    #print "x_axe", x_axe
    #print "y_axe", y_axe

    x_min = start - 2   # Creates empty space in left side of coordinate system.
    x_max = stop + 2    # Creates empty space in right side of coordinate system.
    y_max = int(max(y_axe)) + 2     # Creates empty space in top of coordinate system.
    y_min = int(min(y_axe)) - 2     # Creates empty space in bottom of coordinate system.

    pylab.plot(x_axe, y_axe)    # Plots the curve using the values in x_axe and y_axe.
    
    # We check to see which solution we have to plot

    if len(single_point) != 0:  # Testing for occurance of a single root.
        pylab.plot(single_point[0][0], 0, 'ro')   # Printing a red dot at the root point.
    elif len(double_point) != 0:    # Testing for occurance of a double root.        
        pylab.plot(double_point[0][0], 0,'ro')    # Printing a red dot at the root point.
        pylab.plot(double_point[1][0], 0,'ro')    # Printing a red dot at the root point.

    pylab.axis([x_min, x_max, y_min, y_max])    # Sets the min and max values for the x and y axis.
    pylab.axhline(0, 0, color = 'r')    # Draws the x axe.
    pylab.axvline(0, 0, color = 'r')    # Draws the y axe.
    pylab.annotate('y-axis', xy = (0.25, y_max - 1), xytext = (0.25, y_max - 1))    # Place the 'y-axis' on the plot.
    pylab.annotate('x-axis', xy = (x_max - 1, - 1), xytext = (x_max - 1, - 1))  # Place the 'x-axis' on the plot.
    pylab.show()    # Shows the plot.

#second_pol_plot(3, -6, 3, -1, 3, 0.1)   # Single root
second_pol_plot(-2, 8, -6, -0, 4, 0.1) # Double root
