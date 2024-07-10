#Hypothesis is basically a way to detect change using null(never changes). It's to see if a claim we make is true or not by comparing it to previous data of that same state

#hypothesis is basically good for data analytics intrepretation as it helps us make use of a data to make whatever claim we want and verify it
#as a data analyst this is an indispensable tool in your arsenal to draw use of.

#Example: Imagine you’re researching whether more parents today believe electronics and social media cause their teenagers’ lack of sleep 
#previous compared to years. Hypothesis testing is your trusted ally in verifying this claim.



import random
from scipy import stats

#previous sample data
#
# prev_sample = 0.66


#Current sample data
# rand_sample = 1160


# random.seed(9)
# variableName = [random.choice(["Yes","No"]) for i in range(rand_sample)]
# percentage_of_agreed = 0
# for i in variableName:
#     if i == "Yes":              #This seems like a much easier way to calculate it "sample_yes = sum(1 for val in sample_data if val == "yes") 
#         percentage_of_agreed += 1
# print(percentage_of_agreed)      
# #do not forget "for i in range()" helps you repeat the tasks any number of times you want to being friendly with integers
# mean = percentage_of_agreed/rand_sample
# mean = round(mean,2)
# std = (prev_sample * (1-prev_sample))/rand_sample ** 0.5
# zscore = round((mean - prev_sample)/std,2)
# print(zscore)
# p_value = 1-stats.norm.cdf(zscore) #this helps calculate grEATER DAN as d default withou 1- is less than
# print(p_value)

#You forgot to verify your assumption sample size and shi





#new sample
#Imagine you’re researching whether more parents today believe electronics and social media cause their teenagers’ lack of sleep 
#previous compared to years. Hypothesis testing is your trusted ally in verifying this claim



null = 0.5
q = 1-null
data = round(137/238,4)
sd = round(((null*q)/238)**0.5,5) #apparently theres a difference between 1/2 and 0.5 the bottom line is 0.5 is the right one
z = round((data -  null)/ sd,2)

value = 1-stats.norm.cdf(z)#this shows greater than actually 
print(value)





#confidence interval
#we need a certain amount of confidence in whatever we want to draw or conclude theres a certain way this can be done using maths especially the 60 95, 99.8 rule
#it doesnt tell us exactly but gives us a range of value to follow we will see how this is done

sampleSize = 25
sampleData = [random.uniform(63,115)] #used to generate a number within  the range set
import numpy as np
mean = np.mean(sampleData)
std = np.std(sampleData, ddof=1)
z = 1.98
marginError = z * (std)/(sampleSize**0.5)
ans = (mean + marginError )