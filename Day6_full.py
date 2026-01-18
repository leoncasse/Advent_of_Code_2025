import numpy as np
import pandas as pd

f = pd.read_csv('Data/input_day6.txt', sep='\s+', header=None)  # load as pandas dataframe with whitespace as seperator

# -------------------------------- Part 1 ---------------------------------------
grandTotal = 0

# loop over all columns in dataframe and add if "+"" or multiply if "*""
for i in f:
    if f[i][4]=='*':
        calcMul=int(f[i][0])*int(f[i][1])*int(f[i][2])*int(f[i][3])
        grandTotal += calcMul

    else:
        calcSum=f[i][0:4].astype(int).sum()
        grandTotal += calcSum


print('The grand total (part 1) = ' + str(grandTotal))



# -------------------------------- Part 2 ---------------------------------------
# load raw data without any processing
with open('Data/input_day6.txt', 'r') as file:
    lines_list = file.readlines()

# First get list of all operators (* or +)
operators = lines_list[4].split(' ')  
operators = list(filter(lambda x: x != '' and x !='\n', operators))

counter = len(operators)  # get number of operators

# set constants
grandTotal = 0   # final total
value1=''        # value of first row
value2=''        # value of second row
value3=''        # value of third row
value4=''        # value of fourth row
addSum=0         # initialize sum value to 0
addMult=1        # initialize multiplication value to 1

len_lines = len(lines_list[0])

# Loop over all columns
for i in range(len_lines-2, -1, -1):


    operator = operators[counter-1]

    value1=lines_list[0][i]
    value2=lines_list[1][i]
    value3=lines_list[2][i]
    value4=lines_list[3][i]
    
    totValue = value1+value2+value3+value4   # combine all values into a single string

    if value1 == value2 == value3 == value4 == ' ':   # when all columns are empty add to total
        if operator=='*': 
            grandTotal+=addMult
        else:
            grandTotal+=addSum

        counter -= 1
        
        # reset sum and multiplication values
        addMult=1
        addSum=0

    else:                                                  # add (* or +) of columns together
            if operator=='*':
                addMult *= int(totValue)
            else:
                addSum += int(totValue)



# repeat addition one more time as first line in txt is not empty
if operator=='*':
    grandTotal+=addMult
else:
    grandTotal+=addSum

print('The grand total (part 2) = ' + str(grandTotal))