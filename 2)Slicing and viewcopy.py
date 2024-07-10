import numpy as np
 
#slicing 1 dimensional array
arr1 = np.array([1,2,3,4,5])
# print(arr1[0:3])   # why didnt it print 4? well python excludes the last stuff and refuses to call it so it minuses it out. thats the entire nature of cutting, oh but it will print the first one though
# print(arr1[0:5:2])  #take it in two steps the fist one handles the list the second deals with the increments

#two dimensional slicing
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2[0,1:3])

#three dimensional slicing
arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[4,2,8]]])
print(arr3[1,0,1:3])

#what if you only want 0 from each element?
arra2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arra2[0:3,0])


#for multidimension
#basically take into account what is dimension is first 
#what inside of the dimension you want
#specifically the number inside that you chose in the second step


#View and copy
#.copy is a method to copy what is in array in a new one, the value of this copy is if you change anything on the original it will not affect ther copied
array = np.array([1,2,3,4])
n_copy = array.copy()
array[3] = 10
print(array)
print(n_copy)  #even thogh array has changed the copy still remains the same.

#view basicaly everything changes unlike copy
array2 = np.array([1,2,3,4])
n2_copy = array2.view()
array2[0] = 10 #even if its n2_copy[0] = 10 it will still change
print(array2)
print(n2_copy)

#a way to check whether its a view or copy is using (.base)