from inputFileReader import readFile

day2_list = readFile("Input_Files/Day2_1.txt")

## DAY 2 PART A ##
num2s = 0
num3s = 0

# Iterate through items
for line in day2_list:

    # Get unique letters in line
    setLine = set(line)
    # Iterate through all letters and see if there are two of that letter
    for letter in setLine:
        if line.count(letter) == 2:
            num2s = num2s + 1
            # Break loop so as to not count multiple
            break

    for letter in setLine:
        if line.count(letter) == 3:
            num3s = num3s + 1
            break

print("Result Day 2 part a: " + str(num2s*num3s))

## DAY 2 PART B ##

# Iterate through each line
for o_line_index in range(0, len(day2_list)):
    o_line = day2_list[o_line_index]
    # Iterate through the line, removing letter at a time
    for i in range(0, len(o_line)):
        o_line_removed = o_line[:i] + o_line[i+1:]
        # Iterate through each line
        for n_line_index in range(o_line_index+1, len(day2_list)):
            n_line = day2_list[n_line_index]
            n_line_removed = n_line[:i] + n_line[i+1:]
            if (o_line_removed == n_line_removed):
                print(n_line_removed)
