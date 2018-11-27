#!/usr/bin/env python3

# Name: Grady Lynch, Frank Entriken
# Student ID: 002297574, 
# Email: grlynch@chapman.edu, 
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: cw11

import matplotlib.pyplot as plt
import numpy as np

def Euler(N):
    
    n = np.linspace(0, 10 * np.pi, N)
    
    k1 = np.zeros(N)
    
    k2 = np.zeros(N)
    k2[0] = 1
    
    d = (10 * np.pi)/N
    
    
    
    for x in range(1, len(k1)):
        k1[x] = k1[x-1] + d*k2[x-1]
        k2[x] = k2[x-1] - d*k1[x-1]

        
    plt.plot(n, k1)
    plt.plot(n, k2)
    
def Heun(N):
    
    n = np.linspace(0, 10 * np.pi, N)
    
    k1 = np.zeros(N)
    k1[0] = 0
    
    k2 = np.zeros(N)
    k2[0] = 1
    
    d = (10 * np.pi)/N
    
    for x in range(1, len(n)):
        #ubar = uk[i-1] + dt*u2k[i-1]
        #upbar = u2k[i-1] - dt*uk[i-1]
        #uk[i] = uk[i-1] + (dt/2)*(u2k[i-1] + upbar)
        #u2k[i] = u2k[i-1] - (dt/2)*(ubar + uk[i-1])
        
        temp1 = k2[x-1] - d*k1[x-1]
        temp2 = k1[x-1] + d*k2[x-1]
        k1[x] = k1[x-1] + (d/2)*(k2[x-1]+temp1)
        k2[x] = k2[x-1] - (d/2)*(temp2+k1[x-1])
        
    plt.plot(n, k1)
    plt.plot(n, k2)
    
def RK2(N):
    
    n = np.linspace(0, 10 * np.pi, N)
    
    k1 = np.zeros(N)
    k1[0] = 0
    
    k2 = np.zeros(N)
    k2[0] = 1
    
    d = (10 * np.pi)/N
    
    x1=0
    y1=0
    x2=0
    y2=0
    
    for x in range(1, len(k1)):   
        x1 = d*k2[x-1]
        x2 = d*(k2[x-1]+x1/2)
        y1 = -d*k1[x-1]
        y2 = -d*(k1[x-1] + y1/2)
        k1[x] = k1[x-1] + x2
        k2[x] = k2[x-1] + y2
        
    plt.plot(n, k1)
    plt.plot(n, k2)
    
def RK4(N):
    
    n = np.linspace(0, 10 * np.pi, N)
    
    k1 = np.zeros(N)
    k1[0] = 0
    
    k2 = np.zeros(N)
    k2[0] = 1
    
    d = (10 * np.pi)/N
    
    x1=0
    y1=0
    x2=0
    y2=0
    x3=0
    y3=0
    x4=0
    y4=0
    
    for x in range(1, len(k1)): 
        x1 = d*k2[x-1]
        x2 = d*(k2[x-1]+x1/2)
        x3 = d*(k2[x-1]+x2/2)
        x4 = d*(k2[x-1]+x3)
        k1[x] = k1[x-1]+(x1+2*x2+2*x3+x4)/6
        y1 = -d*k1[x-1]
        y2 = -d*(k1[x-1]+y1/2)
        y3 = -d*(k1[x-1]+y2/2)
        y4 = -d*(k1[x-1]+y3/3)
        k2[x] = k2[x-1]+(y1+2*y2+2*y3+y4)/6
        
    plt.plot(n, k1)
    plt.plot(n, k2)