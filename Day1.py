from inputFileReader import readFile
import collections
import math

day1a_list = readFile("Input_Files/Day1_1.txt")
day1aresult = 0;
for i in day1a_list:
    day1aresult = day1aresult + int(i)
print(day1aresult)

day1blist = [0]
curr = 0
day1bresult = 0
old_i = 0
elementNotFound = True
while True:
    old_i = len(day1blist)
    for i in day1a_list:
        curr = curr + int(i)
        day1blist.append(curr)
    if len(set(day1blist)) != len(day1blist):
        break

print(str(old_i) + " : " + str(len(day1blist)))
for i in range(old_i, len(day1blist)):
    isRepeated = day1blist.count(day1blist[i-1]) > 1
    if isRepeated:
        print(str(i) + ": " + str(isRepeated) + " : " + str(day1blist[i-1]))
        break
