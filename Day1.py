from inputFileReader import readFile, solutionPrintOut
import collections
import math

day1a_list = readFile("Input_Files/Day1_1.txt")
day1aresult = 0;
for i in day1a_list:
    day1aresult = day1aresult + int(i)
solutionPrintOut("1", "A", str(day1aresult))

day1blist = [0]
curr = 0
old_i = 0
elementNotFound = True
while True:
    old_i = len(day1blist)
    for i in day1a_list:
        curr = curr + int(i)
        day1blist.append(curr)
    if len(set(day1blist)) != len(day1blist):
        break

for i in range(old_i, len(day1blist)):
    isRepeated = day1blist.count(day1blist[i-1]) > 1
    if isRepeated:
        solutionPrintOut("1", "B", str(day1blist[i-1]))
        break