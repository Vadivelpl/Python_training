# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 15:02:43 2018

@author: PL Vadivel (pv48452)
"""
#Python is a case sensitive language

############### Integers ###############
2 ** 4          # 2 to the power of 4
61 / 2          # classic division. returns with decimal points
61 // 2         # "floor" division
5 % 2           # modulus function. return the remainder
1 in [1,2,3]    # in operator
1 == '1'        # returns false as it is comparing an integer to a string
1 != 1          # checking for not equal. Returns false as they are equal
# clear or Ctrl+L to  Clear the console
a = 3.75 ; type(a)
b = int(3.75)   #converting float to integer. similarly you can convert to float or str
type(b)
type('3.75') ;  
type(str(a))
float(3) 
float('string')


############### Strings ###############
s = 'Hi my Name is CITI. #name #citi #123'
t = '123'
# No need to declare the data type of the variable in the beginning. Varaible takes the data type while value is assigned
# Variable names should not start with numbers or special characters. use underscore for variable with many words(preferred) 
# Type variable name and press tab to know the methods that can be applied on the variable of that datatype
s.isdigit() ; t.isdigit()
s.lower()                   # This only prints in the console. does not update the value of s
s.upper()                   # Prints in the console only when the current line is run
print (s.upper())           # Prints in the console even when batch of lines are run
s = s.lower()
s.split('#')                # Returns a list. This can be used to extract hashtags from a tweet
tweet = s.split('#')[0]     # Accessing the 0th element in the list.
tweet + 'What\'s your name?' # Concatenate two strings. Include escape character \ if your string contains apostrophe
'Citi '*3 #Citi will be repeated 3 times
'Citi ' * 'Blr' #error. subtraction, multipication, division between two strings will return error

############### List ###############
num = [1,3,5]                   # Creating a list of integers
string_list1 = ['a','c','b']    # Creating a list of strings
string_list1.append('d')        # in built functions of list updates the list automatically. no need to assign again
string_list1.sort()
string_list1.reverse()
#view the changes directly in variable explorer in Spyder. size/shape of the variable, contents can be viewed directly


############### Print statements ###############
print('tweet:',tweet,'I am ', 200,' years old')
name = 'CITI' ; Age = 200   # Two lines of code written in single line using semi colon
print('my age is {} and my name is {}'.format(Age,name)) #value of num and name will get printed within curly braces
print('I am {two}. my age is {one} and my name is {two}'.format(one=200,two=name)) #no need to worry about the order of the format parameters
print(num[0])


############### Datetime ###############
import datetime                                 # Importing a library
time1 = datetime.datetime.now()                 # System time
time2 = datetime.datetime.now()                 # System time
diff = time2-time1
diff.days * 86400 + diff.seconds                # Converting time to seconds
divmod(diff.days * 86400 + diff.seconds, 60)[0] # Converting difference in datetime into minutes


############### General ###############
help(divmod)   # To know more about the function
help("".split) # To know more about the methods
type(s)        # To know the data type of a variable


############### To get working directory ###############
import os
os.getcwd() #get current working directory
os.chdir('C:/Vadivel/Knowledge/python_codes') #change current working directory


############### While loop / For loop / map / filter ###############
#for loop
for x in range(5): #default start for range is 0 if not mentioned specifically. only stop is given
    print("i value is {}".format(x))
    
for x in range(1,5,2): #start, stop, increment/step
    print("i value is {}".format(x))    #indendation is important. ends at stop-1
    
#while loop
i=0
while i<5:
    print("i value is {}".format(i))
    i=i+1
    
seq = range(1,8,3) #increment by step 2 - prints [1,4,7]
for i in seq:
    print(i)

#map
def times2(var): return var*2 #this will also work. entire function in one line. if next line is used, then there should be indentation
list(map(times2,seq)) #map function passes each element in seq(list) to times2(function). Thus map function can be used in place of for loops
#map will return a list of output which the times2 function returns
list(map(lambda var: var*2,seq)) #how function can be replaced by lamda expression. 

#filter
list(filter(lambda num: num%2==0, seq)) #filter function filters out element from the sequence based on a condition

