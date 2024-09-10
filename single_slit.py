"""
author: Logan Mui (lrm2022)
two measured distances and times,
calculate all intermediate quantities leading to
final determination of both q and q_c
include columns for uncertainties, calculated by error propagations, on all measured and calculated quantities
"""

import math

width_of_slit = 0.085 #mm

wavelength_of_light = 0.000656 #mm

distance = 0 #mm

theta = 0 #radians

max_intensity = 0

def to_radians():
    return

def alpha_function(width_of_slit = width_of_slit, wavelength_of_light = wavelength_of_light, theta = theta):
    alpha_function = ( (math.pi * width_of_slit) / wavelength_of_light ) * math.sin()
    return alpha_function

def beta_function(wavelength_of_light = wavelength_of_light, theta = theta):
    beta_function = ( math.pi / wavelength_of_light ) * math.sin(theta)
    return

def intensity_function(max_intensity = max_intensity, width_of_slit = width_of_slit, wavelength_of_light = wavelength_of_light, theta = theta):
    return