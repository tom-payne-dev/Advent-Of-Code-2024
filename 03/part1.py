import re

inputFile = open("input.txt", "r")
rawInput = inputFile.read()

x = re.findall("mul\((\d{1,3}),(\d{1,3})\)", rawInput)

total = 0
for i in x:
    total += (int(i[0]) * int(i[1]))

print(total)