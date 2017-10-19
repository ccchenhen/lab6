#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 10:19:10 2017

@author: xg7
"""

# Week 6 Lab Q1
class Student:
    
    def __init__(self, name = "", of_class = "", major = ""):
        self.name = name
        self.of_class = of_class
        self.major = major
        self.knowledge = 0
        
    #setter
    def setName(self, name):
        self.name = name
    
    def setOfClass(self, of_class):
        self.of_class = of_class
        
    def setMajor(self, major):
        self.major = major
    
   #getter
    def getName(self):
        return self.name
   
    def getOfClass(self):
        return self.of_class
    
    def getMajor(self):
        return self.major
    
    def getKnowledge(self):
        return self.knowledge
    
    #method
    def study(self, time):
        self.knowledge += (1 + self.knowledge*time) 
   

        