#fill in this blank with the function you gotta use
from math import sqrt

#fill in this blank with the number of variables
number_vars = 2
#insert all your variable uncertainty pairs here
variables = [0.01048313582,0.03418413856]
variable_uncertainties = [0.0005274,0.0017114]
#I was going to make this a lot more interchangeable, but it really is a major pain to do so.
def function_to_use(voltage = variables[0], resistance = variables[1]):
    return voltage/resistance

uncertainty_partial = []
uncertainty_sum = 0

#this is just plug and chug lol
for num in range(number_vars):
    var = variables[num]
    var_uncertainty = variable_uncertainties[num]
    if(num==0):
        uncertainty_partial = (0.5 * (abs(function_to_use(voltage = var+var_uncertainty) - function_to_use(voltage = var)) + abs(function_to_use(voltage = var-var_uncertainty) - function_to_use(voltage = var))))
        uncertainty_sum += pow(uncertainty_partial,2)
    if(num==1):
        uncertainty_partial = (0.5 * (abs(function_to_use(resistance = var+var_uncertainty) - function_to_use(resistance = var)) + abs(function_to_use(resistance = var-var_uncertainty) - function_to_use(resistance = var))))
        uncertainty_sum += pow(uncertainty_partial,2)


uncertainty_sum = sqrt(uncertainty_sum)
print(uncertainty_sum)

#   error using numerical method: 0.0110088432
#  error using analytical method: 0.0110087947
    