import matplotlib.pyplot as plt
import numpy as np

import math
def sincurve():
    plt.subplot(2,2,1)
    degrees = range(0,360+1)
    sinValues = [math.sin(math.radians(i)) for i in degrees]
    plt.plot(sinValues)
    plt.xlabel('Degree')
    plt.ylabel('Sin Values')
    plt.title('Sin Curve')
    plt.grid()

def coscurve():
    plt.subplot(2,2,2)
    degrees = range(0,360+1)
    cosValues = [math.cos(math.radians(i)) for i in degrees]
    plt.plot(cosValues)
    plt.xlabel('Degree')
    plt.ylabel('Cos Values')
    plt.title('Cos Curve')
    plt.grid()

def polynomial():
    plt.subplot(2,2,3)
    a = 2.5
    b = 4.5
    step = 0.1
    nstep = int((b-a)/step)
    x = [a+step*i for i in range(nstep+1)]
    y1 = [t**2 for t in x]
    y2 = [t**3 for t in x]
    plt.plot(x, y1, 'ro--', label = 'X vs X**2')
    plt.plot(x, y2, 'b<-', label = 'X vs X**3')
    plt.legend()
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Polynomial Function')
    plt.grid()
    
def exponential():
    plt.subplot(2,2,4)
    x = np.linspace(-1,2,100)
    y1 = np.exp(x)
    plt.plot(x, y1)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Exponential Function')
    plt.grid()


    
def main():
    sincurve()
    coscurve()
    polynomial()
    exponential()
    plt.tight_layout()
    plt.show()

main()
