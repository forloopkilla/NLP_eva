# -*- coding: utf-8 -*-
import os 
os.getcwd()
os.chdir("C:\\Users\jiany\Documents\School\Speech & Textmining\Project_Aufgabe")



text = open('effie.txt')
data = text.read() # turns text into list



len(data)
print(data[1:1000])
