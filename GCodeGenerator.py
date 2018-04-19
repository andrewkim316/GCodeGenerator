import sympy
from sympy import symbols
t = symbols('t')
def generator(x,y,z,duration):
    timeStep = 0.005
    print("N1 G21")
    for l in range(int(duration/timeStep)):
        newX = str(x.subs(t,timeStep))
        newY = str(y.subs(t,timeStep))
        newZ = str(z.subs(t,timeStep))
        timeStep+=0.005
        print("N"+str(l+2)+" X"+newX+" Y"+newY+" Z"+newZ)
generator(2*t,3*t-5,7*t-10,10)