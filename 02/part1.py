#Open the file
inputFile = open("input.txt", "r")
rawInput = inputFile.readlines()

#loop through each report and cumulutively add the safe reports
# safe = 0
# for report in rawInput:
#     report = report.split(" ")
#     differenceCounter = 0
#     unsafeNums = 0

#     for i in range(1, len(report)):
#         diff = abs(int(report[i]) - int(report[i-1]))
#         if(diff < 1 or diff > 3):
#             unsafeNums += 1

#     if(unsafeNums == 0):
#         safe += 1


unsafeCounter = 0
for report in rawInput:
    report = report.split(" ")
    initiallyPositive = (int(report[0])-int(report[1]) < 0)
    for i in range(0, len(report)-1):
        diff = (int(report[i])-int(report[i+1]))

        # Find whether difference is between 1 and 3
        if(abs(diff) > 3 or abs(diff) < 1):
            unsafeCounter += 1
            break

        # Find if numbers all have the same polarity
        if((diff < 0) != initiallyPositive):
            unsafeCounter += 1
            break
    

print(len(rawInput) - unsafeCounter)