# InputList = input("Please type your comma seperated list: ")
import math
InputList = "20, 7, 6, 5, 10, 19, 25, 59, 3, 55, 8, 34, 44, 41, 59, 11"

InputList = InputList.split(", ")
InputList =[float(i) for i in InputList]
InputList.sort()
print(InputList)

num = len(InputList)
sum = sum(InputList)

mean = sum/num

if num%2 != 0: #if odd
    median = InputList[((num + 1)/2) - 1]
else:
    median = ( InputList[int(num/2) -1 ] + InputList[int(num/2)] )/2
    
sumOfEachMinusMean = 0;
for value in InputList:
    sumOfEachMinusMean += (value - mean)**2
    
stDev = (sumOfEachMinusMean/(num-1))**(1/2)

print("General: ")
print("mean: ", mean)
print("median: ", median)
print("stDev: ", stDev)
print()



def pthPercentile(percent, InputList):
    location = (percent/100)*(len(InputList)+1)
    if location%1 == 0: #check if its a whole number
        return InputList[int(location)]
    else:
        return InputList[int(math.floor(location)) -1] + ( (location%1)*(InputList[int(math.floor(location))] - InputList[int(math.floor(location) -1)]) )
    
        
        
min = InputList[0]
Q1 = pthPercentile(25,InputList)
Q3 = pthPercentile(75,InputList)
max = InputList.pop()

print("5 Number Summary:")
print("min: ", min)
print("Q1: ", Q1)
print("median: ", median)
print("Q3: ", Q3)
print("max: ", max)
print("---")
print("Interquartile range: ", (Q3 - Q1))

print()

