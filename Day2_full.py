import numpy as np

# load data
f = np.loadtxt('Data/day2/input.txt', dtype = str, delimiter=',')

## part 1
invalidID = 0

for line in f:
    # print(line)

    start = int(line.split('-')[0])
    end   = int(line.split('-')[1])

    rangeVals = list(range(start, end))

    for val in rangeVals:
        # for i in range(2,10)

        if len(str(val)) % 2 == 0:
            valLen = int(len(str(val))/2)
        else:
            valLen = 0

        if valLen > 0:
            partDiff = int(str(val)[:valLen]) - int(str(val)[valLen:])
        else:
            partDiff = 'nope'

        if partDiff == 0:
            
            invalidID += val

print(' ')
print('Invalid ID (part 1) = ' + str(invalidID))


## part 2
invalidID = 0
valList = []

for line in f:
    # print(line)

    start = int(line.split('-')[0])
    end   = int(line.split('-')[1])

    rangeVals = list(range(start, end))

    for val in rangeVals:
        for i in range(2,11):
            partDiff = 0
            
            if len(str(val)) % i == 0:
                valLen = int(len(str(val))/i)
            else:
                continue
            
            if i == 2:
                partDiff = int(str(val)[:valLen]) == int(str(val)[valLen:])
            elif i == 3:
                partDiff = int(str(val)[:valLen]) == int(str(val)[valLen:valLen*2]) == int(str(val)[valLen*2:valLen*3])
            elif i == 4:
                partDiff = int(str(val)[:valLen]) == int(str(val)[valLen:valLen*2]) == int(str(val)[valLen*2:valLen*3]) == int(str(val)[valLen*3:valLen*4])
            elif i == 5:
                partDiff = int(str(val)[:valLen]) == int(str(val)[valLen:valLen*2]) == int(str(val)[valLen*2:valLen*3]) == int(str(val)[valLen*3:valLen*4])  == int(str(val)[valLen*4:valLen*5])
            elif i == 6:
                partDiff = int(str(val)[:valLen]) == int(str(val)[valLen:valLen*2]) == int(str(val)[valLen*2:valLen*3]) == int(str(val)[valLen*3:valLen*4])  == int(str(val)[valLen*4:valLen*5])  == int(str(val)[valLen*5:valLen*6])
            elif i == 7:
                partDiff = int(str(val)[:valLen]) == int(str(val)[valLen:valLen*2]) == int(str(val)[valLen*2:valLen*3]) == int(str(val)[valLen*3:valLen*4])  == int(str(val)[valLen*4:valLen*5])  == int(str(val)[valLen*5:valLen*6]) == int(str(val)[valLen*6:valLen*7])
            elif i == 8:
                partDiff = int(str(val)[:valLen]) == int(str(val)[valLen:valLen*2]) == int(str(val)[valLen*2:valLen*3]) == int(str(val)[valLen*3:valLen*4])  == int(str(val)[valLen*4:valLen*5])  == int(str(val)[valLen*5:valLen*6]) == int(str(val)[valLen*6:valLen*7]) == int(str(val)[valLen*7:valLen*8])
            elif i == 9:
                partDiff = int(str(val)[:valLen]) == int(str(val)[valLen:valLen*2]) == int(str(val)[valLen*2:valLen*3]) == int(str(val)[valLen*3:valLen*4])  == int(str(val)[valLen*4:valLen*5])  == int(str(val)[valLen*5:valLen*6]) == int(str(val)[valLen*6:valLen*7]) == int(str(val)[valLen*7:valLen*8]) == int(str(val)[valLen*8:valLen*9])
            elif i == 10:
                partDiff = int(str(val)[:valLen]) == int(str(val)[valLen:valLen*2]) == int(str(val)[valLen*2:valLen*3]) == int(str(val)[valLen*3:valLen*4])  == int(str(val)[valLen*4:valLen*5])  == int(str(val)[valLen*5:valLen*6]) == int(str(val)[valLen*6:valLen*7]) == int(str(val)[valLen*7:valLen*8]) == int(str(val)[valLen*8:valLen*9]) == int(str(val)[valLen*9:valLen*10])
                
            if partDiff == True:
                if val not in valList:
                    valList.append(val)
                    invalidID += val
    
print('Invalid ID (part 2) = ' + str(invalidID))