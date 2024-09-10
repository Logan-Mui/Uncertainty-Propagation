import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize as opt


t_values = np.linspace(0,12)
v_values = np.array([])
c_values = np.array([])

for value in t_values:
    voltage = 10 * np.sin(40000*np.pi*value+1.56) #including phase shift
    current = voltage / 4
    v_values = np.append(v_values, voltage)
    c_values = np.append(c_values, current)


    
plt.xlabel("Time (S)")
plt.ylabel("Volts (V) | Current (A)")
plot_voltages = plt.scatter(t_values, v_values)
plot_voltages.set_label("Voltage")
plot_currents = plt.scatter(t_values, c_values)
plot_currents.set_label("Current")

plt.legend()


plt.show()


