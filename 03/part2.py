import re

inputFile = open("input.txt", "r")
rawInput = inputFile.read()

def regexMultipleTotal(x):
    x = re.findall("mul\((\d{1,3}),(\d{1,3})\)", x)
    total = 0
    for i in x:
        total += (int(i[0]) * int(i[1]))
    return total


multiply = True
end = False
dontPosition = 0
doPosition = 0
enabledMultiplications = []
while(not end):
    if(multiply == True):
        if(rawInput[doPosition:].find("don't()") != -1):
            dontPosition = (rawInput[doPosition:].find("don't()")+7+doPosition)
            enabledMultiplications.append(rawInput[doPosition:dontPosition]) 
        else:
            enabledMultiplications.append(rawInput[doPosition:])
            end = True
    else:
        if((rawInput[dontPosition:].find("do()") != -1)):
            doPosition = (rawInput[dontPosition:].find("do()")+4+dontPosition)
        else:
            end = True
    multiply = not multiply


total = 0
for mult in enabledMultiplications:
    total += regexMultipleTotal(mult)
print(total)
