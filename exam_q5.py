import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline
from scipy.optimize import newton
import matplotlib.pyplot as plt


# Importing textfile containing required data
theta = np.loadtxt("httpstheory.tifr.res.in.kulkarnidata.txt.txt")[:, 0]
d = np.loadtxt("httpstheory.tifr.res.in.kulkarnidata.txt.txt")[:, 1]
x_axis = np.linspace(0.1, 10, 100)
cubic_spline = InterpolatedUnivariateSpline(theta, d, k=3)

# Defining function for (a)
def interpolationfunction(arbtheta):
    return cubic_spline(arbtheta)

# Defining function for (c)
def interpolation3704(arbtheta):
    return cubic_spline(arbtheta)-370.4

# Plotting graph for (b)
plt.scatter(theta, d, label='Given Data Points')
plt.plot(x_axis, interpolationfunction(x_axis), label='Interpolation using Cubic Spline')
plt.legend()
plt.title("Theorist's data and my interpolated curve")
plt.xlabel('θ (arbitary units)')
plt.ylabel('d (arbitary units)')
plt.show()

# Finding θ at d=370.4 (c)
root = newton(interpolation3704,0.1)
print(' Required value of θ for d=370.4 is : ', root)
