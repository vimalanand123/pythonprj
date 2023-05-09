#list = []
#no_of_elements = int(input('enter some val'))
#print('no_of_elements',no_of_elements)
#
#for i in range(no_of_elements):
#	element	=	int(input())
#	list.append(element)
#i = 0
#for i in range(no_of_elements):
#	print(list[i])
from collections import namedtuple
from ctypes.wintypes import BOOL
from curses import ACS_DARROW
import numbers
from queue import Empty
from typing import Type, no_type_check

import re
from xml.sax.handler import feature_external_ges
import numpy
#def bitwise_separation():
#    fpga_input  =   input('enter the input')
#    fpga_input  =   fpga_input[2:]
#    fpga_input  =   bin(int(fpga_input))
#    no_of_rows =    int(input("enter the no of rows"))
#    list    =   []
#    for i in range(no_of_rows):
#        inlist =    []
#        bit_start   =   int(input("enter start"))
#        bit_end   =   int(input("enter end"))
#        inlist.append(bit_start)
#        inlist.append(bit_end)
#        list.append(inlist)
#        print(fpga_input[bit_start:(bit_end+1)])
#
#bitwise_separation()
#student = namedtuple("student",['age','year','marks','height'])
#fields  =   input()
#col1,col2,col3,col4    =   fields.split()
#print("fields are ",col1,col2,col3,col4,sep=" ")
#no_of_students =    int(input())
#for i in range(no_of_students):
#    input('enter the corresponding columns')
#
str =   "hello world"
print("The string str : %s"%(str)) # prints The string str : Hello 

# using triple quotes  
print("""They said, What's there?""")  
  
# escaping single quotes  
print('They said, What\'s going on?')  
  
# escaping double quotes  
print("They said, \"What's going on?\"")  

print(r"C:\\Users\\DEVANSH SHARMA\\Python32")  

# Using Curly braces  
print("{} and {} both are the best friend".format("Devansh","Abhishek"))  
  
#Positional Argument  
print("{1} and {0} best players ".format("Virat","Rohit"))  
  
#Keyword Argument  
print("{b},{a},{c}".format(a = "James", b = "Peter", c = "Ricky"))  

Integer = 10;    
Float = 1.290    
String = "Devansh"    
print("Hi I am Integer ... My value is %d\nHi I am float ... My value is %f\nHi I am string ... My value is %s"%(Float,Integer,String))  

# list example in detail  
emp = [ "John", 102, "USA"]       
Dep1 = [ "CS",10]    
Dep2 = [ "IT",11]      
HOD_CS = [ 10,"Mr. Holding"]      
HOD_IT = [11, "Mr. Bewon"]      
print("printing employee data ...")      
print(" Name : %s, ID: %d, Country: %s" %(emp[0], emp[1], emp[2]))      
print("printing departments ...")     
print("Department 1:\nName: %s, ID: %d\n Department 2:\n Name: %s, ID: %s"%( Dep1[0], Dep2[1], Dep2[0], Dep2[1]))      
print("HOD Details ....")      
print("CS HOD Name: %s, Id: %d" %(HOD_CS[1], HOD_CS[0]))      
print("IT HOD Name: %s, Id: %d" %(HOD_IT[1], HOD_IT[0]))      
print(type(emp), type(Dep1), type(Dep2), type(HOD_CS), type(HOD_IT))  

# Python program to show how slicing works in Python tuples    
# Creating a tuple    
tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Objects")    
# Using slicing to access elements of the tuple    
print("Elements between indices 1 and 3: ", tuple_[1:3])    
# Using negative indexing in slicing    
print("Elements between indices 0 and -4: ", tuple_[::-2])    
# Printing the entire tuple by using the default start and end values.     
print("Entire tuple: ", tuple_[:])   
    
numbers=    [100,123,66,7788,3451,459,341,456]

for number in numbers:
    if(number<=237):
        if(number%2==0):
            print(number)
else:
    Empty

members_re  =   []
for member in dir(re):
    if "find" in member:
        members_re.append(member)

print(sorted(members_re))

test =  [1,0]
print("test is %s"%type(test))
print(BOOL(test[0]),BOOL(test[1]),sep='\n')

other = "\t hi"
print(other,ascii(other))

def my_function(a,b):
    return(a+b)

list1 = ["apple","banana","grape"]
list2 = ["is a fruit","is veg","non-veg"]

result = map(my_function,list1,list2)

print(result,list(result))

nat_num = numpy.array([1],ndmin = 1)
print("enter the array no")
for lop_var in range(18):
    nat_num.append(int(input()))

print(nat_num)