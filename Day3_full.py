import numpy as np

f = np.loadtxt('Data/input_day3.txt', dtype = str)

# Part 1
totVal = 0
for line in f:

    f_len = len(line)
    val1 = 0
    
    for i in range(0, f_len-1):

        new_val = int(line[i])

        if new_val>val1:
            val1 = new_val
            max_idx = i
        else:
            continue

    val2 = 0

    for j in range(max_idx+1, f_len):
        new_val = int(line[j])

        if new_val>val2:
            val2 = new_val
            max_idx = j
        else:
            continue
        
    val = str(val1)+str(val2)
    totVal += int(val)

print(' ')
print('Total Joltage (part 1) = ' + str(totVal))


#-----------------------------------------------------------------------------------#
## Part 2
totVal = 0

for line in f:
    val = ''
    val1 = 0
    max_idx = -1
    
    f_len = len(line)

    for totNums in range(0,12):
        val1 = 0
        rightBuffer = f_len-(12-totNums)

        for test in range(max_idx+1, rightBuffer+1):
            new_val = int(line[test])

            if new_val>val1:
                val1 = new_val
                max_idx = test
            else:
                continue

        val = val+str(val1)
    totVal += int(val)

print('Total Joltage (part 2) = ' + str(totVal))