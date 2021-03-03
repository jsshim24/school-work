# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 22:07:44 2021

@author: junse
"""
import numpy as np

data = np.genfromtxt("movieRatingsDeidentified.csv",delimiter=",")

participantmean = np.mean(data,axis=1)       #2
#print(participantmean[-1])

meanofmeans = np.mean(participantmean)          #8

participantmedian = np.median(data,axis=1)      #3

participantsd = np.nanstd(data,axis=1)              #6
meansd = np.mean(participantsd)              #9
#print(participantsd)
#print(np.nanmean(participantsd))

moviemean = np.nanmean(data,axis=0)                 #4
print(moviemean[-14])    
                   
moviemedian = np.median(data,axis=0)            #5

moviesd = np.std(data,axis=0)                #7