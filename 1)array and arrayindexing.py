import numpy as np

array = np.array([1,2,3,4])
# print(array)


# array is usually dtype or some shi like that 1 dimesional array is the example given 2 dimensional array is a little bit more complex as it has another one of this[], this is how multidimesional arrays are covered actually this is used in machine learning and ai 

arr2 = np.array([[1,2,3],[1,3,3]])

#think of it as one bracket stores the last dimension present, thats how it is for all of them yes, 1 bracket stores the dimension


arr3 = np.array([[[1,2,3],[1,3,3]],[[1,2,3],[1,3,3]]])

#ndim is what you use to check its dimension 

# print(arr3.ndim)  #will print its 3 dimension


#given an array any dimension you want ndmin

new = np.array(5,ndmin=4)





#Array indexing is accessing an array element.

#perform operations using the index
# print(array[0] + array[3])

#give me arr3 9 pls

#indexing  a 2 dimensional array means the first parameter gets you its position dimension the second parameter gets you what it is inside it
# print(arr2[1,1])

#indexing a 3 dimensional array
ar3ind = np.array([[[1,2,3],[1,3,3]],[[4,5,6],[7,8,9]]]) #it has three parameters in indexing
#the first number corresponds with its dimension  which is [[1,2,3],[1,3,3]] and [[4,5,6],[7,8,9]] if we chose 0 we end up with the 1st one
#the second number corresponds to which one among its dimension  [[1,2,3],[1,3,3]] we chose 1 so we end up with [1,2,3]
#the third number prints out the one you are looking for exactly, [1,2,3] now which one in it exactly is what the last one does
#you explained this better in your notes. but the various dimensions represents the parameters
print(ar3ind[0,1,2])


four_dim_array = np.array([[[[1, 2], [3, 4]],
                            [[5, 6], [7, 8]],
                            [[9, 10], [11, 12]]],

                           [[[13, 14], [15, 16]],
                            [[17, 18], [19, 20]],
                            [[21, 22], [23, 24]]],

                           [[[25, 26], [27, 28]],
                            [[29, 30], [31, 32]],
                            [[33, 34], [35, 36]]]])


#try finding it as a play test

