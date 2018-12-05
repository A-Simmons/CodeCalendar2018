from inputFileReader import readFile, solutionPrintOut
from string import ascii_lowercase
day5_string = readFile("Input_Files/Day5_1.txt")[0]

## PART A ##
string = day5_string
count = len(string)
while True:
    for c in ascii_lowercase:
        ss = c.lower() + c.upper()
        string = string.replace(ss, "")
        ss = c.upper() + c.lower()
        string = string.replace(ss, "")
    if (len(string) == count):
        break
    else:
        count = len(string)
solutionPrintOut("5", "A", str(count))

## PART B ##
lowestCount = len(day5_string)
for l in ascii_lowercase:
    string = day5_string
    string = string.replace(l.lower(), "")
    string = string.replace(l.upper(), "")
    count = len(string)
    while True:
        for c in ascii_lowercase:
            ss = c.lower() + c.upper()
            string = string.replace(ss, "")
            ss = c.upper() + c.lower()
            string = string.replace(ss, "")
        if (len(string) == count):
            break
        else:
            count = len(string)
    if count < lowestCount:
        lowestCount = count
solutionPrintOut("5", "B", str(lowestCount))
