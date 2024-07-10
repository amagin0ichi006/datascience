import numpy as np 
#sorting
#In numpy we have a function called sort is sorts it from an ascending to descending order

#sort 2 diimensional array

arr2 = np.array([[91,-45,5], [8,-3,4]])
sort = np.sort(arr2)
print(sort)

#we just dont have to numbers in array
bool_array = np.array([True,False,True,False])
bo_sorted = np.sort(bool_array)
print(bo_sorted)

#searchsorted