#Open the file
inputFile = open("input.txt", "r")
rawInput = inputFile.readlines()

unsafeCounter = 0
for report in rawInput:
    report = report.split(" ")
    initiallyPositive = (int(report[0])-int(report[1]) < 0)
    validity = True

    for i in range(0, len(report)-1):
        diff = (int(report[i])-int(report[i+1]))

        # Find whether difference is between 1 and 3
        if(abs(diff) > 3 or abs(diff) < 1):
            validity = False
            break

        # Find if numbers all have the same polarity
        if((diff < 0) != initiallyPositive):
            validity = False
            break
    
    if(not validity):
        dampenedValidity = True
        for i in range(0, len(report)-1):
            diff = (int(report[i])-int(report[i+1]))
            # Find whether difference is between 1 and 3
            if(abs(diff) > 3 or abs(diff) < 1):
                dampenedValidity = False
                break

            # Find if numbers all have the same polarity
            if((diff < 0) != initiallyPositive):
                dampenedValidity = False
                break

        
        
        if(dampenedValidity == False):
            unsafeCounter += 1

print(len(rawInput) - unsafeCounter)