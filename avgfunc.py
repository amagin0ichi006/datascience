#a function that takes in a list of numbers
#calc the moving avg of that list
import matplotlib.pyplot as pl
li = []
def list():
    num = int(input("how many numbers do you need in the list "))
    for i in range(num):
        i = int(input("Put in your number "))
        li.append(i)
    print(li)

list()


#dont forget len counts the range of number
lis = []
def movavg():#Moving average
    unit = int(input("how many units are we using "))
    num = 1
    
    for i in range(len(li) - unit + 1):
            
            window = li[i:i+unit] #this is taking the particular amount of range you want dont forget how for loops work this helps print part of it like you want
            avg = sum(window)/unit  #cuz for loops help generate a particular type of "sequence" how many times you like and this is how you want it done cuz the sequence needed is weird.
            lis.append(avg)         #maybe from now on your first bet is to just print out the specified amount of times you want it out?
    plot = pl.plot(lis)#if you want it to be seen you have to  put the method show
    pl.show()

    print(lis)                            
                             
      
#plot
#pyplot helps keep the plot and other methods       


movavg()

       