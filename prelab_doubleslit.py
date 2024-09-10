########################################################################
##
##  prelab_doubleslit.py
##  Oct 5 2015
##  M Zemcov, zemcov@cfd.rit.edu, mod LSB 12/17
##  This code is for the double slit final exam questions. 
##
#########################################################################

# imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

# set up a plot window
figa = plt.figure(0)
axa = figa.add_subplot(1,1,1)

# set some x and y axes for the plot
xmin = -1.5
xmax = 1.5
ymin = 0
ymax = 1

# define parameters given in lab book
a = 8.5e-5              # m nominal
#a = 5.0e-5             # m variant 1
#a = 5.5e-5             #   variant 2
#a = 6.0e-5             #   variant 3
#a = 7.0e-5             #   variant 4
#a = 8.0e-5             #   variant 5
#a = 1.0e-4             #   variant 6
#a = 1.2e-4             #   variant 7
#a = 1.5e-4             #   variant 8

d = 3.5e-4             # m nominal
#d = 2.0e-4             #   variant 1
#d = 2.5e-4             #   variant 2
#d = 3.0e-4             #   variant 3
#d = 3.5e-4             #   variant 4
#d = 4.0e-4             #   variant 5
#d = 4.5e-4             #   variant 6
#d = 5.0e-4             #   variant 7
#d = 5.5e-4             #   variant 8
#d = 6.0e-4             #   variant 9
lambda_laser = 656.e-9 # m
lambda_light = 545e-9  # m

# compute an input range of angles (in degrees)
theta_deg = np.linspace(-1.5,1.5,num=1000) # degrees

# convert to radians
theta = np.pi * theta_deg / 180.

# compute alpha
alpha = np.pi * a * np.sin(theta) / lambda_laser

# compute beta
beta = np.pi * d * np.sin(theta) / lambda_laser

# compute the double slit intensity profile
I_double = np.cos(beta)**2 * (np.sin(alpha) / alpha)**2

# compute the single slit intensity profile
I_single = (np.sin(alpha) / alpha)**2

# make the plot of the curves
axa.plot(theta_deg,I_double,color='red',label='Double Slit')
axa.plot(theta_deg,I_single,color='blue',label='Single Slit')

#axa.plot(theta_deg,I_single,color='blue',label='Single Slit')

# prettify it
axa.set_xlim(xmin,xmax)
axa.set_ylim(ymin,ymax)
axa.set_xlabel(r'$\theta$ (deg)',fontsize=18)
axa.set_ylabel(r'$I(\theta)/I_{0}$',fontsize=18)

# add a legend
plt.legend(loc='upper left',prop={'size':10})

#plot the figure
plt.show()
    
# finally, when we have looped through both fits, save the output
#plt.savefig("prelab_doubleslit.png",dpi=200)

# clear the plot buffer
#plt.close()


# and we're out of here

#return
