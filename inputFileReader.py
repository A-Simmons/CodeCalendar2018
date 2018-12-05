
def readFile(file):
    result = []
    f = open(file, "r")
    for x in f.readlines():
        x = x.rstrip()
        result.append(x)
    return(result)