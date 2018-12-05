from inputFileReader import readFile
import datetime
day4_list = readFile("Input_Files/Day_4_1.txt")
day4_list.sort()

def splitString(line):
    parts = line.split('] ')
    year = parts[0][1:5]
    month = parts[0][6:8]
    day = parts[0][9:11]
    hour = parts[0][12:14]
    minute = parts[0][15:17]
    if parts[1][0] == 'G':
        # Take section after # and before 'space'. SUPER SHIT CODE
        type = line.split("#")[1].split(' ')[0]
    elif parts[1][0] == 'w':
        type = 'wake'
    elif parts[1][0] == 'f':
        type = 'fall'
    else:
        type = 'wtf'
    return int(year), int(month), int(day), int(hour), int(minute), type

## DAY 4 PART A
guards = {}
for line in day4_list:
    year, month, day, hour, minute, type = splitString(line)
    if type != 'wtf':
        if type == 'wake':
            wakeTime = datetime.datetime(year, month, day, hour, minute)
            diff = (wakeTime - fallTime).seconds//60
            guards[currGuard] += diff
            #
        elif type == 'fall':
            fallTime = datetime.datetime(year, month, day, hour, minute)
            #
        else:
            currGuard = type;
            if type not in guards.keys():
                guards[type] = 0

mostAsleepGuard = 0
for key, value in guards.items():
    if value == max(guards.values()):
        mostAsleepGuard = key
print("Most asleep guard is #" + mostAsleepGuard + " with " + str(max(guards.values())) + " minutes slept.")

currGuard = False
minsAsleep = []
for line in day4_list:
    year, month, day, hour, minute, type = splitString(line)
    if type != 'wtf':
        if type == 'wake':
            if currGuard:
                wakeTime = minute
                minsAsleep.extend(range(sleepTime, wakeTime))
        elif type == 'fall':
            if currGuard:
                sleepTime = minute
        elif type == mostAsleepGuard:
            currGuard = True
        else:
            currGuard = False


minSol = max(set(minsAsleep), key=minsAsleep.count)
print("Most common minute asleep is minute " + str(minSol))
print("Part A Solution (guard # * minute) = " + str(int(mostAsleepGuard) * minSol))
print("")
## DAY 4 PART B ##
guards2 = {}
for line in day4_list:
    year, month, day, hour, minute, type = splitString(line)
    if type != 'wtf':
        if type == 'wake':
            wakeTime = minute
            guards2[currGuard].extend(range(fallTime, wakeTime))
            #
        elif type == 'fall':
            fallTime = minute
            #
        else:
            currGuard = type;
            if type not in guards2.keys():
                guards2[type] = []

mostOccurencesValue = 0
mostOccurencesKey = 0
mostOccurencesMinute = 0
for key, value in guards2.items():
    mostComMin = None
    if len(value) > 0:
        mostComMin = max(set(value), key=value.count)
        mostComOcc = value.count(mostComMin)
        if mostComOcc > mostOccurencesValue:
            mostOccurencesValue = mostComOcc
            mostOccurencesKey = key
            mostOccurencesMinute = mostComMin

print(str(mostOccurencesKey) + ": " + str(mostOccurencesMinute) + ": " + str(mostOccurencesValue))
print("Part B Solution: " + str(int(mostOccurencesKey) * mostOccurencesMinute))