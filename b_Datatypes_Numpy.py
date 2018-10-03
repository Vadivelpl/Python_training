# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 14:43:31 2018

@author: PL Vadivel (pv48452)
"""

############### DICTIONARIES ###############
#Dictionary have key value pairs
eng2sp = dict()
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
eng2sp['Zero'] #KEy error. Zero key not present in the dictionary
len(eng2sp)
print(eng2sp.keys()) ; print(eng2sp.values())

#use of function, dictionary and elif
def caught_speeding(speed, is_birthday="False"): #if second parameter is not passed while calling the function, by default it will take False
    a={}
    a["True"]=[65,85]
    a["False"]=[60,80]
    if (speed > a[is_birthday][1]):
        return "Big Ticket"
    elif (speed > a[is_birthday][0]):
        return "Small Ticket"
    else:
        return "No Ticket"
    
caught_speeding(63,"True")
caught_speeding(63,"False")


############### TUPLE ###############
#tuple is similar to list but not mutable. Values cannot be changed. Entire variable has to be rewritten
t = tuple()
t = (4,6,8,10)
t = tuple('leaders')
t[1] = 'f' #returns error


############### SET ###############
#set doesnt have duplicate values. It has unique representation of each value
first_set = set(['a','a','a','b','b','a','c','c','d','a','b']) #not showin in variable explorer
second_set = set(['d','e','d','d','e','f'])
first_set.difference(second_set) # A - B
first_set.intersection(second_set) # A n B
first_set.union(second_set) # A u B


#############################################
############### NUMPY ###############
import numpy as np

#numpy - numpy has 1D vectors or 2D matrices
my_list=[1,2,3]
arr = np.array(my_list) #casting a list into a numpy array
print(arr, type(arr), arr[0])
print(my_list, type(my_list), my_list[0])
my_list+5   # Error
arr+5       # Adds 5 to all elements in arr array
arr*5       # Multiplies 5 to all elements in arr array


a = np.zeros((2,3)) #creating an array of all zeros
b = np.ones((2,2)) #creating an array of all ones
c = np.full((2,2),6) #fill all the elements with 6
d = np.eye(2) #create a 2*2 identity matrix
e = np.random.rand(2,2) #random numbers from a uniform distribution between 0 and 1. create a 2*2 array filled with random numbers
e1= np.random.randn(2,2) #random numbers from a normal distribution
f = np.random.randint(0,3,(2,4)) # create a 2*4 array filled with random numbers - 0 and 2. Start, stop, size
g = np.linspace(0,5,11) #gives 11 evenly spaced points between 0 and 5
h = np.arange(0,11,2) #similar to range function. this returns an array


f = f.reshape(4,2) #reashaping array of a particular dimenstion into another dimension
f[0]
f[0][1]
f[0,1] #Both this line and above line return same result
e1.max() #method to find max element in an array
e1.min() #or np.min(e1) - both are same
e1.argmax() #gives the position of max
e1.argmin() #gives the position of min


e1>0 #This return an array of boolean True / False
e1[e1>0] #This returns elements for whose index inside boolean array is positive
e[:]=3 #This assignment to all element will happen only in np array and not in list
slice_of_e = e[0:2] #This is just a reference to e. if you change slice_of_e, e will also change
e[1]=4
slice_of_e = e[0:2].copy()
e[1]=5
e1[-1:]   # Returns the last row
e1[-1:,1] # Returns the second element in the last row
e1[-1:,0:1] # Returns the first element in the last row


np.add(c,b)
np.subtract(c,b)
np.multiply(c,d)
np.sum(f) #sum of all the elements in f
np.sum(e, axis=0) #sum of all elements in the columns of e. axis=1 -> sum of row elements
np.sum(e, axis=1)
np.sqrt(e)


import random
random.seed(42)
grade = [np.random.rand() for i in range(0,1000)] #generate 1000 random numbers


#Matrix
mat = np.array([[1,2,3],[4,5,6],[7,8,9]]) #creating a matrix / 2D array
print(mat)