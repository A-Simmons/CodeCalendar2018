from inputFileReader import readFile, solutionPrintOut
import numpy
numpy.set_printoptions(threshold=numpy.inf)

def getDataFromLine(line):
    parts = line.split(" ")
    location = parts[2]
    x = int(location.split(",")[0])
    y = int(location.split(",")[1][:-1])
    size = parts[3]
    lenX = int(size.split("x")[0])
    lenY = int(size.split("x")[1])
    return(x+1, y+1,lenX, lenY)

day3_list = readFile("Input_Files/Day3_1.txt")

## DAY 3 PART A ##
n = 1000;
clothMatrix = numpy.zeros((n,n), dtype=object)

for line in day3_list:
    x, y, lenX, lenY = getDataFromLine(line)
    clothMatrix[x:x+lenX,y:y+lenY] += 1
solutionPrintOut("3", "A", str(numpy.count_nonzero(clothMatrix > 1)))

## DAY 3 PART B ##
for line in day3_list:
    x, y, lenX, lenY = getDataFromLine(line)
    if numpy.count_nonzero( clothMatrix[x:x+lenX,y:y+lenY] > 1 ) == 0:
        solutionPrintOut("3", "B", str(line[1:5]))


