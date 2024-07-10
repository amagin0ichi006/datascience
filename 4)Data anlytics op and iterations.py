import numpy as np

#Operations that help with Data analysis

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])

#Summation
print(sum(arr1)) #produces 15
print(sum(arr2))#produces [12 15 18]
print(arr1.sum())#produces 15
print(arr2.sum())#produces 45 the actual sum basically when dealing with dimenmsions and in general it is better to use .sum() if you intend to add everything

#Maximum and Minimum
print(arr1.max())
print(arr1.min())
print(arr2.min())
print(arr2.max())


#What if you want to add colum and rows with each other?
ar2 = np.array([[1,2,3],[4,5,6],[7,8,9],[2,3,2]])
print(ar2)

#adding col axis=0
print(ar2.sum(axis=0))

#adding row axis = 1
print(ar2.sum(axis=1))



#iteration

one_dim = np.array([1,2,3,4,5]) #iterate over this shi blud

#iterating over 1 sequences
for i in one_dim:
    print(i)

two_dim = np.array([[1,2,3],[4,5,6],[7,8,9]])

#iterating over two dim
for i in two_dim:
    for e in i:
        print(e)

#basically if you dont get it the more dimensions added the more nested for loops is added 
        
#if you want to skip that like when in 7 dimensions numpy has an easy way to do this which is (nditer)
for i in np.nditer(two_dim):
    print(i)


#Figuring out the index
for i, e in np.ndenumerate(two_dim):
    print(i,e) #this tell you the position and the number



