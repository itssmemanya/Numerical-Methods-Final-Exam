import numpy as np
from scipy.integrate import romberg
# I will be using romberg integration
import matplotlib.pyplot as plt

# Defining given function
def rho(x):
    return (3/(4*np.pi))*((1+x**2)**(-5/2))
def integrand(x):
    return 3*((1+x**2)**(-5/2))*(x**2)

x_axis = np.linspace(-10, 10, 101)
new_x = np.linspace(0, 10, 51)
integral = np.linspace(0, 0, 51)
mass = np.linspace(0, 0, 101)
# Plotting rho vs x
rho1=rho(x_axis)
plt.plot(x_axis, rho1)
plt.title('Given function')
plt.xlabel('x')
plt.ylabel('ρ')
plt.show()

# Since the gien function is spherically symmetric and I have changed integrand for volume integration

# Plotting new integrand vs x
rho2=integrand(x_axis)
plt.plot(x_axis, rho2)
plt.title('New function')
plt.xlabel('x')
plt.ylabel('Integrand')
plt.show()

# Calculating integral
for i in range (0 ,51):
    integral[i]=romberg(integrand,0,new_x[i])
    mass[i+50]=integral[i]
    mass[51-i-1]=integral[i]

# Plotting final integral
plt.plot(new_x, integral)
plt.title('Integral')
plt.xlabel('x')
plt.ylabel('Integral')
plt.show()

#Finally plotting mass vx s
plt.plot(x_axis, mass,  label='Mass enclosed from distance 0 to x ')
plt.title('Final graph for the question')
plt.xlabel('x (m)')
plt.ylabel('Mass (kg) ')
plt.show()



                        
