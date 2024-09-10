import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize as opt

def func(x,f_zero,l_over_r):
    x = np.array(x)
    return 1/np.sqrt(1+np.power((((2*np.pi)/x)*(l_over_r)),2)*np.power((np.power(x,2)-np.power(f_zero,2)),2))

plt.xlabel("Frequency (kHz)")
plt.ylabel("Ratio of Current")

plt.title("Current/Max Current V.S. Frequency")

#loading the values for the graph
x_values = []
y_values = []
y_error = []
filename = "Lab 2/Lab/Max_Current_over_Current_VS_Frequency.csv"
file_reader = pd.read_csv(filename)
file_array = np.array(file_reader)
#adding vals to axes
for row in file_array:
    x_values.append(row[0])
    y_values.append(row[1])
    y_error.append(row[2])
#fitting the data


plt.errorbar(x_values,y_values, yerr = y_error, marker = 'o',capsize = 5, linestyle = 'None', label = 'Current/Max Current V.S. Frequency')

guess_params = [11.21,0.045516]

parameters, covariance = opt.curve_fit(func, x_values, y_values,sigma = y_error, p0=guess_params)


plt.plot(x_values,func(x_values,*parameters),label = 'Fit')

print("Parameters: ",*parameters)

perr = np.sqrt(np.diag(covariance))

print("Error: ",perr)
plt.legend(loc="lower right")
plt.show()
#plt.save()