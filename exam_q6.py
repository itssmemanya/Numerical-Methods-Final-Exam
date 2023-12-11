import numpy as np
import matplotlib.pyplot as plt

# Declaring Constants
lambdaval = 2.5
t0 = 0
tf = 10
n0 = 40
step=0.01

t=[0]
n=[n0]
stepn=0
nnext=0

# I will run a loop from t=0 to 10 s
while t[-1]<tf:
    stepn=-1*lambdaval*step*n[-1]  # dn=-lambda dt n
    nnext=n[-1]+stepn              # finding next value of n
    n.append(nnext)
    t.append(t[-1]+step)

# Finally plotting the graph
plt.scatter(t,n)
plt.title(' n vs t graph')
plt.xlabel('t (s)')
plt.ylabel('n (cm-3)')
plt.show()
    
