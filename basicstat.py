from scipy import stats
import numpy as np
list = []

def store():
    num = int(input("How many numbers are you looking to store "))
    for i in range(num):
        i = int(input("Place number in "))
        list.append(i)
    print(list)
store()

def mean():
    global avg
    add = sum(list)
    avg = add/len(list)
    print(avg)

def median():
    mid = np.median(list)
    print(mid)
#  mid = int(len(list)%2)
#  num = 0
#  Length = int(len(list)/2)
#  for i in range(Length):
#     num = i =+ 1
#     if mid == 0:
#         add = list[num] + list[num+1]
#         print(add/2)
#     else:
#         print(list[num])
#         break



def mode():
   ans = stats.mode(list)
   print(ans)
    


def var():
    lit = []
    avg = np.mean(list)
    for i in list:
        var = ((i-avg)**2)
        lit.append(var)
        add = np.sum(lit)
        ans = add/len(list)-1
        sqr = ans**1/2


    print(f"i think this is its variance: {ans} and the sd is {sqr}")
#the way you be calling some of this things after u already did them like mean again, i think oop fixes that to reduces redundancy
var()



