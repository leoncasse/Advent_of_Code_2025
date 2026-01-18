import numpy as np

f = np.loadtxt('Data/input_day5.txt', dtype = str)

fresh = f[:174]
ingredients = f[174:]

valList = []
numFresh = 0
numSpoil = 0

# ------------------------------------- PART 1 --------------------------------------------
for i in ingredients:
    ingredient = int(i)

    for f in fresh:
        low = int(f.split('-')[0])
        high = int(f.split('-')[1])

        if ingredient >= low and ingredient <=high:
            numFresh+=1
            break 

print('Number of fresh ingredients: ' + str(numFresh))


# ------------------------------------- PART 2 --------------------------------------------
counter = 0
numFresh_IDS = 0
tmp=1
c2 = 0

while tmp>0:   # check if after all corrections there are any residual overlapping ranges
    c2+=1
    tmp=0
    counter=0

    print('Reloop: '+ str(c2))

    for i in fresh:
        counter += 1
        
        left = int(i.split('-')[0])
        right = int(i.split('-')[1])

        for j in np.delete(fresh, counter-1):  

            low = int(j.split('-')[0])
            high = int(j.split('-')[1])

            if left>=low and right<=high:
                fresh =  np.delete(fresh, counter-1)  
                counter = counter-1
                break

            if (left>=low and left<=high):
                left = high+1
                right = max(left, right)

                fresh[counter-1]=str(left)+'-'+str(right)

                tmp+=1

            if (right <= high and right >= low):
                right = low-1
                left = min(right, left)

                fresh[counter-1]=str(left)+'-'+str(right)

                tmp+=1

for i in fresh:
    left = int(i.split('-')[0])
    right = int(i.split('-')[1])
    numFresh_IDS += (right+1-left)

print('Total number of fresh IDs: ' + str(numFresh_IDS))