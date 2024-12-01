import numpy as np

# Splits input.txt into 2 arrays for sorting and comparison
inputFile = open("input.txt", "r");
locIDs = inputFile.readlines()

list1 = []
list2 = []

for pair in locIDs:
    nums = pair.split()
    list1.append(int(nums[0]))
    list2.append(int(nums[1]))

# Sorts each array
list1 = np.sort(list1)
list2 = np.sort(list2)

# Compares each value and cumulatively adds distance of each value pair to a variable
totalDistance = 0

for i in range(0, len(list1)):
    totalDistance += abs(list1[i] - list2[i])
    
print(totalDistance)