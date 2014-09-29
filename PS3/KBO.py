#
#  KBO.py
#  Kibble & Berkshire Orbit
#
#  Created by Jiang, Minzhi on 09-24-14.
#

import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

def kepler_equation(T, e, t):
    return lambda phi : (T/2./np.pi*(phi-e*np.sin(phi)) - t)

def get_time(length, num):
    t = np.arange(num, dtype=float)
    t = t/(num-1)*length
    return t

def get_orbit(phi, a, e, T):
    x = a*(np.cos(phi)-e)
    y = a*np.sqrt(1.-e**2)*np.sin(phi)
    return x, y


if __name__ == "__main__":
    T = 1.
    e = 0.55
    a = 1.
    length = 4.
    num = 1000
    
    t = get_time(length, num)
    guess = np.zeros(num)
    phi =  fsolve(kepler_equation(T, e, t), guess)
    
    x,y = get_orbit(phi, a, e, T)
    
    plt.plot(t, x, '.b', markersize = 1)
    plt.xlabel('t[yr]')
    plt.ylabel('x[AU]')
    plt.title('x vs t')
    plt.savefig('ps3_prb4_x_t.png', dpi=180)
    plt.clf()
    
    plt.plot(t, y, '.b', markersize = 1)
    plt.xlabel('t[yr]')
    plt.ylabel('y[AU]')
    plt.title('y vs t')
    plt.savefig('ps3_prb4_y_t.png', dpi=180)
    plt.clf()

    plt.plot(x, y, '.b', markersize = 1)
    plt.xlabel('x[AU]')
    plt.ylabel('y[AU]')
    plt.title('orbit')
    plt.savefig('ps3_prb4_orbit.png', dpi=180)
    plt.clf()
