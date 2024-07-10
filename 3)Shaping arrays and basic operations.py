import numpy as np 
#Shaping arrays
arrays = np.array([[1,2,3,1],[4,5,6,1],[7,8,9,1]]) #if you want to know its shape the method is .shape (first one tells you how many brackets of dem dimensions there are, the second bracket tells you how much is inside each of those brackets)
print(arrays.shape)
#this will print (3 4) reason being we have 3 brackets and 4 inside it they have 4 numbers

#Now we can reshape arrays if need be 
stu = np.array([19,19,19,20,20,20,21,21,21])
exa = np.array([51,60,57,72,79,91,100,87,92])

exa_sp = stu.reshape(3,3)
print(exa_sp)
#note when your reshaping the two numbers you put into must multiply to give you the amount in the element when it comes to two arrays anyways

#reshaping in 3 dimensional
arr3 = np.array([[[1,2,3,1],[4,5,6,1],[7,8,9,1]],[[1,2,3,1],[4,5,6,1],[7,8,9,1]],[[1,2,3,1],[4,5,6,1],[7,8,9,1]]])
print(arr3.shape)

arr1 = np.array([1,2,3,4,5,6])
ar3 = arr1.reshape(2,3,1)
print(ar3)

#Basic operation on Arrays
#we can create an array within numbers like we do with lists in python using range
a = np.arange(0,10)
print(a) #as you can see works just like how a classic range in python would

#Basic mathematical operations
b = np.array([1,4,5,7,56,5,4,5,6,7])

#adding 
print(a+b)#u could subtract nut nah am not into all that
#(**2) means square

#numpy has its own built in functions like sqrt
print(np.sqrt(a))

#LEARN A FEW OF NUMPY FUNCTIONS THATS AN ORDER!!!!!




#Testing whether values in an array are less than or greater than a given value
A = np.array([1,2,3,4])
print(A<2)