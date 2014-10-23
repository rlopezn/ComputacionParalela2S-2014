__author__ = 'cluster'
import math
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


def fitness(x,y,z):
    # x^2 * sen(yz) + xy sen (log z)
    a= (x*x*math.sin(y*z)) + x*y*math.sin(math.log(z))
    return a

def grafica():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X, Y, Z = axes3d.get_test_data(0.05)
    ax.plot_surface(X, Y, Z, rstride=3, cstride=8, alpha=0.3)
    # cset = ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
    # cset = ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
    # cset = ax.contourf(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)

    ax.set_xlabel('X')
    ax.set_xlim(-40, 40)
    ax.set_ylabel('Y')
    ax.set_ylim(-40, 40)
    ax.set_zlabel('Z')
    ax.set_zlim(-100, 100)

    plt.show()


def main():
    print fitness(1,2,3)
    grafica()



main()
