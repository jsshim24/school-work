# -*- coding: utf-8 -*-
"""
Created on Tue Mar 2 11:48:18 2021

The medAbDev function below assumes a numpy array input, and returns 
the median absolute deviation of the array.

The function also probably works with a normal python list input, but
I'm not completely sure (didn't make sure) because that isn't 
important.

I couldn't figure out how to numpy array append within a loop, so
I substituted by using a normal python list in the for loop. Feedback
on how to do the former would be greatly appreciated.
"""

import numpy as np

def medAbDev(array):
    writtenBy = "Jun Seob"
    
    median = np.median(array)
    
    deviations = []
    
    for i in array:
        deviations.append(abs(i-median))
    
    devs = np.array([])
    newDevs = np.append(devs,deviations)
    mad = np.median(newDevs)
    
    return mad
        
    
example = np.array([1,3,5,7,9])
example2 = np.array([4.5,3.2,1.5,5.7,9.3,2.2,6.9])
print(medAbDev(example))
print(medAbDev(example2))