import panda as pd

#Lets explore a datasets that has its entries missing this stuff is important for a couple of reasons one of the resons is when you form a graph of it if some are missing it will to in the graph causing some form of inconsistency

df2 = pd.read_csv("datasets/data2.csv")
print(df2) 

#if you wanna remove anything that gots na .dropna()
print(df2.dropna())#usually you should always put them in variable to make use of

# #if you wanna fill it
# df2.fillna(10,inplace=True)
# print(df2)

df2['Bicycle'].fillna(11,inplace=True)
print(df2) #right now it wont work as intended due to u already filling it but yh this i think is its exact syntax 



#finding Mean Median and Mode
#.mean()
#.mode()[0] the [0] make sure its a number
#.median()


#matplotlib with pandas
import matplotlib.pyplot as plt
#plot
df2.plot()

#show
df2.show()