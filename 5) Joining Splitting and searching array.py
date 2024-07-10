import numpy as np
#joining

#creating 1 dimensional array
array1 = np.array([1,2,3,4,5])
array2 = np.array([6,7,8,9,10])

#this is how you join them together we use concatenate plus note unlike the other instance method this will need double brackets.
join = np.concatenate((array1,array2))
print(join) 

#creating 2 dimension array join rows
array3 = np.array([[1,2,3],[4,5,6]])
array4 = np.array([[7,8,9],[10,11,12]])
row = np.concatenate((array3,array4), axis=1) #dont forget 1 is row so your adding the equivalents row to each other
print(array3)
print(array4)
print(row) 

#Splitting arrays
#one dimensional array
arr = np.array([1,2,3,4,5,6])

#you split by using np.array_split
spl = np.array_split(arr,3)
print(spl)
print(spl[0])
print(spl[1])
print(spl[2])



#searching
#use np.where()
#it can do more than that tho you can also use it to search which one is less than 5
where = np.where(arr > 2)
print(where)
#basically you can set conditions