# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 21:58:34 2022

@author: Manoj
"""
"""
A pendulum wave is a device that has a series of 
pendulums with an increasing time period. When these 
pendulums are released simultaneously it will produce 
the effect of a transverse wave that keeps changing and
 it cycles back to the initial position.
The following program shows pendulum waves and takes pendulum 
as number of input from the user and also asks user for the speed
of wave variable.
"""

#importing libraries
import vpython as vp
import numpy as np

g = 9.9                                     # gravity aceleration
theta_ang = 50*np.pi/180                    # angle
LNTH = []                                   # string length
freq_angular = []                           # angular frequency

valid1 = True
valid2 = True

#input validation loop for no. of pendulum
while valid1:
    #asking number of pendulum for input
    num = int(input('Enter the number of pendulum(1-10): '))
    if (num >= 1) and (num <= 10): 
        valid1 = False      #if the input value satisfys it will break the loop 
        
#input validation loop for frame rate
while valid2:   
    #input for the speed
    frame = int(input('Enter the wave speed (10=slow - 100=fast) : '))
    if (frame>=10) and (frame<=100):
        valid2 = False        #if the input value satisfys it will break the loop
        
        description = "Pendulum waves motion:\n This code shows a pendulum waves with user input option of number of pendulum and speed."

        vp.canvas(height = 800, width = 800, background = vp.color.white, title= description)
        BOB = np.empty(num, vp.sphere)     #empty array for pendulum
        ROD = np.empty(num, vp.cylinder)    #empty array for strings 
        
        #using conditional loop to adjust the pivot position for the pendulum
        if num == 1:
            pivot = vp.vector(0,2,0)            # initial pivot point for the string
        else:
            pivot = vp.vector(0,2,num/num-0.8)  #if more than 1 adjust it by moving on the z direction
            
        roof = vp.box(pos= pivot, size = vp.vector(0.5,0.2,num/1.5), texture = vp.textures.wood)      #roof for string to connect (num/3 to calculate size of roof according to no of pendulum)
        
        for i in range(0, num):                   #loop for the spheres
            L = ((60/(i+50))**2)*g/(4*np.pi*np.pi)        # The lenght of the strings that determinate the angular velocity
            LNTH.append(L)
            w = np.sqrt(g/LNTH[i])              # calculating all the frequency
            freq_angular.append(w)
            pivot = vp.vector(0, 2, i/3)               #updating the pivot point with respect to pendulum
            BOB[i] = vp.sphere(pos=vp.vector(LNTH[i], 0, i/3), radius=0.1, texture = vp.textures.earth)      #creating pendulum spheres according to user input
            ROD[i] = vp.cylinder(pos=pivot, axis = BOB[i].pos-pivot, radius= 0.01, texture = vp.textures.metal) #creating strings w/r to pendulum
        
        for t in np.arange(0, 110, 1/60):             # loop for the movement
            vp.rate(frame)      #frequency of movement
            print(t)            #calculating time
            for i in range(0, num):                 # moving all the spheres in the xy plane
                freq_angular[i] = np.array(freq_angular[i], float)      #initializing angular position
                theta = theta_ang * np.cos(freq_angular[i]*t)   #calculating angular position
                X = LNTH[i]*np.sin(theta_ang * np.cos(freq_angular[i]*t))
                Y = LNTH[i]*(-np.cos(theta_ang * np.cos(freq_angular[i]*t)))
                BOB[i].pos = vp.vector(X, Y, i/3)   #position of pendulum
                ROD[i].axis = BOB[i].pos-ROD[i].pos #position of pendulum string on other end
                
               