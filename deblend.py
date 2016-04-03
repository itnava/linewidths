
import numpy as np
from scipy.optimize import curve_fit
from matplotlib.pyplot import savefig
import matplotlib
from matplotlib import pyplot

# I have to first write a script to test on SDSS data, then on FAST.
#FAST data have a different structure and dimension, so the steps for extracting spectrum 
# will have to be redone.
#I cannot figure out how to read a FAST spectrum. Start with SDSS instead?

def func(x, a, b, c,d):
    return a*np.exp(-(x-b)**2/(2.*c**2)) + d

f = open("0070.out", 'r')
g = open("0070.bands", 'r')

# setting up list for data to be read
counts = []
waves = []

col = []

#skipping first line, with Hbeta. for the test file, I am going to just try and fit OIII
g.readline()

#reading second line, splitting it so that band information is saved in 'bands'
line = g.readline()
bands = line.split()
print bands[3]
print bands[4]

#redshifting OIII wavelength
z = float(f.readline())
o3 = 5007 * z
#first guess for fit. func defined above, in the order (x, a,b,c,d)
#a: amplitude, b: peak wavelength, c: band width, d: a constant
p_guess=(1, o3, 5., 0.01)

for line in f:
    col = line.split()
    #only interested in data between the bands specified in the .bands file
    if float(bands[3]) <= float(col[0]) <= float(bands[4]):
        waves.append(float(col[0]))
        counts.append(float(col[1]))

# recording initial function for plotting later. linspace returns evenly spaced samples
x_func = np.linspace(min(waves), max(waves), 50)
initial_plot = func(x_func, *p_guess)

        
x = counts
y = waves

# fitting function to data. Assuming 20% error in y for now. May need to come up with a more
#realistic way to estimate error, later. 
#Using try-except so that the script does not crash because it could not find a line.
#If line does not exist, the initial guess is returned with no covariance matrix
#maxlev is the number of iterations
try:
    popt, pcov = scipy.optimize.urve_fit(func, x, y, p0=pguess, sigma = 0.3*y, maxfev = 1000*(len(x)+1))
except:
    popt, pcov = p_guess, None
    
print popt
print pcov

try:
    # Calculating residuals ( difference between data and fit). 
    #y_fit calculated by using the function described by the fitting parameters and x
    for i in enumerate(y):
        y_fit = func(x, *popt)
        y_residual = y - y_fit

    #Degrees of freedom of fit.
    dof = len(x_data) - len(popt)

    #Making a plot for comparison 
    #3 rows, 1 column, 1 subplot
    #   3 rows are declared, but there are only 2 plots; this leaves room for text
    #       in the empty 3rd row
    fig = subplot(311)
    #plotting one plot on top of another to compare fit
    #remove ticklabels from the upper plot
    fit.set_xticklabels(  ()  )
    fit.plot(x, y, func(x, *popt))
    fit.plot(x, initial_plot, linestyle="--")
    savefig("test.png")
except:
    pass


