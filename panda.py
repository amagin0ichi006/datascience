#the main functions of panda is analyzing, exploring and manipulating dataset

#datasets and dataframes
import pandas as pd
#types of vehice and record the type of vehicle they sell
datasets = {                #how you create datasets
    'vehicle': ["car", "Bicycle", "Truck"],
    'in_stock': [10,20,13]
}

#create dataframe with panda
data_frame = pd.DataFrame(datasets)
print(data_frame)

#call what you want using .loc[] make sure u put your extra bracket if you want more input it will give u the words at 0 and the words at 2
print(data_frame.loc[[1, 2]])#to find what you are looking for withs its index start at zero

#slice
print(data_frame[0:3])

#you see those indexing number we can change it to what we want
dataset2 = {
    "Cake"  : ['vanilla', 'red velvet', 'chocolate'], 
    "Price" : [2500,3001,2100]
}
data = pd.DataFrame(dataset2,index=["monday", "tuesday", "wenesday"])
print(data.loc[["monday","wenesday"]])




#series are like rows
import pandas as pd
a = [10, 40, 60]
s_eries = pd.Series(a)
print(s_eries)

#.loc to locate it
print(s_eries.loc[0])

#change d same
ser = pd.Series(a, index=["monday", "tuesday", "wenesday"])
print(ser)

# index is what we use to change its naming






#Now we are going to import some excel!!
df = pd.read_csv('pandas/datasets/data1.csv')
print(df)

#YOU CAN DO the same fun stuff you do on dataframes and dataseries here




#what we will talk on is the head() and tail() function in pandas

print(df.head(2))#gives u the top with the parameter of how many

print(df.tail(2))#gives you parameter starting from the bottom


#finally we have .info() which me personally use to check which is null or not meaning which one has no data frame in it don't forget about the cleaning
print(df.info())

#plotting
# import matplotlib.pyplot as plt
# df.plot()
# plt.show()