#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:52 2019

@author: swilson5
"""
import math

class Calculator:
    def __init__(self, data):
        self.data = data
        self.length = len(data)
        self.mean = sum(data)/self.length
        data_2 = sorted(data)
        if len(data_2) % 2 == 1:
            self.median = data_2[int((len(data_2)-1)/2)]
        else:
            self.median = (data_2[(len(data_2)/2)]+data[(len(data_2)/2-1)])/2
        squareddiff = [(x-self.mean)**2 for x in data]
        self.variance = sum(squareddiff)/(self.length-1)
        self.stand_dev = math.sqrt(self.variance)
        

    def add_data(self, more_data):
        self.data.extend(more_data)
        
        data = self.data
        self.length = len(data)
        self.mean = sum(data)/self.length
        data_2 = sorted(data)
        if len(data_2) % 2 == 1:
            self.median = data_2[int((len(data_2)-1)/2)]
        else:
            self.median = (data_2[int((len(data_2)/2))]+data_2[int((len(data_2)/2-1))])/2
        squareddiff = [(x-self.mean)**2 for x in data]
        self.variance = sum(squareddiff)/self.length
        self.stand_dev = math.sqrt(self.variance)   
        
    def remove_data(self, data_to_remove):
        for data in data_to_remove:
            self.data.remove(data)
            
        data = self.data
        self.length = len(data)
        self.mean = sum(data)/self.length
        data_2 = sorted(data)
        if len(data_2) % 2 == 1:
            self.median = data_2[int((len(data_2)-1)/2)]
        else:
            self.median = (data_2[int((len(data_2)/2))]+data_2[int((len(data_2)/2-1))])/2
        squareddiff = [(x-self.mean)**2 for x in data]
        self.variance = sum(squareddiff)/self.length
        self.stand_dev = math.sqrt(self.variance)
