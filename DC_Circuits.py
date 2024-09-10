import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize as opt

def func(x,a):
    return a*x

yerror = 0.005


plt.xlabel("Voltage (V)")
plt.ylabel("Current (Amps)")

plt.title("Current VS Voltage")

#loading the values for the graph
x_values = []
y_values = []
yerror = []
filename = "Lab 1\DC_Circuits.py"
file_reader = pd.read_csv(filename)
file_array = np.array(file_reader)
#adding vals to axes
for row in file_array:
    x_values.append(row[0])
    y_values.append(row[1])
    yerror.append(row[2])

#fitting the data
#parameters, covariance = opt.curve_fit(func, x_values, y_values)

plt.errorbar(x_values,y_values, yerr = yerror,marker = 'o',capsize = 5, linestyle = 'None', label = 'Voltage VS Current')

#print(parameters)

#perr = np.sqrt(np.diag(covariance))

#print(perr)

plt.show()
#plt.save()