"""
author: Logan Mui (lrm2022)
two measured distances and times,
calculate all intermediate quantities leading to
final determination of both q and q_c
include columns for uncertainties, calculated by error propagations, on all measured and calculated quantities
"""
import math
#------constants------
voltage = 500 #Volts

magnification = 2.04
magnification_uncertainty = 0.05

density_oil = 872 #kg/m^3

viscocity = 1.85e-5 #Ns/m^2

density_air = 1.2 #kg/m^3

plate_spacing = 5.91 #mm
plate_spacing_uncertainty = 0.05

a = 0.07776 #nano-meters

#--------------------




#asking user for variables collected
def variable_collection():
    off_distance = float(input("Enter distance for OFF: "))
    off_time = float(input("Enter time for OFF: "))
    on_distance = float(input("Enter distance for ON: "))
    on_time = float(input("Enter time for ON: "))
    return off_distance, off_time, on_distance, on_time

def velocity_calulator(distance,time,magnification = magnification):
    velocity = distance / (magnification*time)
    return velocity

def radius_calculator(velocity_freefall):
    numerator = 9 * viscocity * velocity_freefall
    denominator = 2*(density_oil * density_air)*9.81
    radius = math.sqrt(numerator/denominator)
    return radius

def charge_calculator(velocity_freefall,velocity_upwards,radius,voltage,plate_spacing=plate_spacing):
    numerator = 6 * math.pi * viscocity * plate_spacing * (velocity_freefall + velocity_upwards) * radius
    denominator = voltage
    return numerator / denominator

def charge_c_calculator(charge,a,radius):
    numerator = charge
    denominator = math.sqrt( math.pow((1 + ( a / radius )) ,3) )
    return numerator / denominator


def uncertainty_velocity(distance, time, magnification, magnification_uncertainty):
    adding_uncertainty = abs(velocity_calulator(distance, time, magnification+magnification_uncertainty) - velocity_calulator(distance, time))
    subtracting_uncertainty = abs(velocity_calulator(distance, time, magnification-magnification_uncertainty) - velocity_calulator(distance, time))
    uncertainty = 0.5 * (adding_uncertainty + subtracting_uncertainty)
    return uncertainty

def uncertainty_radius(velocity_freefall, velocity_uncertainty):
    adding_uncertainty = abs(radius_calculator(velocity_freefall+velocity_uncertainty)-radius_calculator(velocity_freefall))
    subtracting_uncertainty = abs(radius_calculator(velocity_freefall-velocity_uncertainty)-radius_calculator(velocity_freefall))
    uncertainty = 0.5 * (adding_uncertainty + subtracting_uncertainty)
    return uncertainty

def uncertainty_charge(velocity_freefall, velocity_freefall_uncertainty, velocity_upwards, velocity_upwards_uncertainty, radius, radius_uncertainty):
    adding_uncertainty_velocity_freefall = abs(charge_calculator(velocity_freefall + velocity_freefall_uncertainty, velocity_upwards, radius, voltage) - charge_calculator(velocity_freefall,velocity_upwards,radius,voltage))
    subtracting_uncertainty_velocity_freefall = abs(charge_calculator(velocity_freefall - velocity_freefall_uncertainty, velocity_upwards, radius, voltage) - charge_calculator(velocity_freefall, velocity_upwards, radius, voltage))
    total_uncertainty_velocity_freefall = 0.5 * (adding_uncertainty_velocity_freefall + subtracting_uncertainty_velocity_freefall)
    
    adding_uncertainty_velocity_upwards = abs(charge_calculator(velocity_freefall,velocity_upwards + velocity_upwards_uncertainty,radius,voltage,plate_spacing) - charge_calculator(velocity_freefall,velocity_upwards, radius, voltage))
    subtracting_uncertainty_velocity_upwards = abs(charge_calculator(velocity_freefall,velocity_upwards - velocity_upwards_uncertainty,radius,voltage) - charge_calculator(velocity_freefall,velocity_upwards, radius, voltage))
    total_uncertainty_velocity_upwards = 0.5 * (adding_uncertainty_velocity_upwards + subtracting_uncertainty_velocity_upwards)
    
    adding_uncertainty_radius = abs(charge_calculator(velocity_freefall, velocity_upwards, radius + radius_uncertainty, voltage) - charge_calculator(velocity_freefall, velocity_upwards, radius, voltage))
    subtracting_uncertainty_radius = abs(charge_calculator(velocity_freefall, velocity_upwards, radius - radius_uncertainty, voltage) - charge_calculator(velocity_freefall, velocity_upwards, radius, voltage))
    total_uncertainty_radius = 0.5 * (adding_uncertainty_radius + subtracting_uncertainty_radius)
    
    adding_uncertainty_plate_spacing = abs(charge_calculator(velocity_freefall, velocity_upwards, radius, voltage, plate_spacing = plate_spacing + plate_spacing_uncertainty) - charge_calculator(velocity_freefall, velocity_upwards, radius, voltage))
    subtracting_uncertainty_plate_spacing= abs(charge_calculator(velocity_freefall, velocity_upwards, radius, voltage, plate_spacing = plate_spacing - plate_spacing_uncertainty) - charge_calculator(velocity_freefall, velocity_upwards, radius, voltage))
    total_uncertainty_plate_spacing = 0.5 * (adding_uncertainty_plate_spacing + subtracting_uncertainty_plate_spacing)
    
    total_uncertainty = math.sqrt( math.pow(total_uncertainty_velocity_freefall, 2) + math.pow(total_uncertainty_velocity_upwards,2) + math.pow(total_uncertainty_radius,2) + math.pow(total_uncertainty_plate_spacing,2) )
    return total_uncertainty

def uncertainty_charge_c(charge, charge_uncertainty, radius, radius_uncertainty):
    adding_uncertainty_charge = abs(charge_c_calculator(charge + charge_uncertainty, a,radius))
    subtracting_uncertainty_charge = abs(charge_c_calculator(charge - charge_uncertainty,a, radius))
    total_uncertainty_charge = 0.5 * (adding_uncertainty_charge + subtracting_uncertainty_charge)
    
    adding_uncertainty_radius = abs(charge_c_calculator(charge,a,radius + radius_uncertainty))
    subtracting_uncertainty_radius = abs(charge_c_calculator(charge,a,radius - radius_uncertainty))
    total_uncertainty_radius = 0.5 * (adding_uncertainty_radius + subtracting_uncertainty_radius)
    
    total_uncertainty = math.sqrt( math.pow(total_uncertainty_charge, 2) + math.pow(total_uncertainty_radius, 2) )
    return total_uncertainty


#Now the function that does EVERYTHING!
def calculate_unknowns():
    off_distance, off_time, on_distance, on_time = variable_collection()
    
    freefall_velocity = velocity_calulator(off_distance, off_time)
    freefall_velocity_uncertainty = uncertainty_velocity(off_distance,off_time,magnification,magnification_uncertainty)
    
    upwards_velocity = velocity_calulator(on_distance, on_time)
    upwards_velocity_uncertainty = uncertainty_velocity(on_distance,on_time,magnification,magnification_uncertainty)
    
    drop_radius = radius_calculator(freefall_velocity)
    drop_radius_uncertainty = uncertainty_radius(freefall_velocity,freefall_velocity_uncertainty)
    
    charge = charge_calculator(freefall_velocity, upwards_velocity, drop_radius, voltage)
    charge_uncertainty = uncertainty_charge(freefall_velocity,freefall_velocity_uncertainty,upwards_velocity,upwards_velocity_uncertainty,drop_radius,drop_radius_uncertainty)
    
    charge_c = charge_c_calculator(charge, a, drop_radius)
    charge_c_uncertainty = uncertainty_charge_c(charge, charge_uncertainty, drop_radius, drop_radius_uncertainty)
    
    print("\n----------RESULTS---------")
    print("\n\nFreefall Velocity:\t",freefall_velocity,"\tUncertainty:\t", freefall_velocity_uncertainty,
          "\nUpwards Velocity:\t",upwards_velocity,"\tUncertainty:\t",upwards_velocity_uncertainty,
          "\nDrop Radius:\t",drop_radius, "\tUncertainty:\t",drop_radius_uncertainty,
          "\nCharge:\t",charge, "\tUncertainty:\t",charge_uncertainty,
          "\nCharge C:\t",charge_c,"\tUncertainty:\t",charge_c_uncertainty)
    
    
    
calculate_unknowns()