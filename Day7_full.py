import numpy as np

with open('Data/input_day7.txt', 'r') as file:
    lines = file.readlines()


# -------------------------------- Part 1 ---------------------------------------
counter = 0
update = 0
beamLoc = [lines[0].find('S')]
test=np.array(beamLoc)
numSplit=0
# ttt = lines

for i in lines[1:141]:
    counter+=1

    # if '^' in i:
    #     print('YES')
    # else:
    #     ttt[counter]=ttt[counter-1].replace('^', '.')
    if update == 1:
        beamLoc = test

    update = 0
    
    for j in range(0,len(beamLoc)):
        if i[beamLoc[j]]!='.':

            test= np.delete(test, test==beamLoc[j])

            if beamLoc[j]-1 not in test:
                test=np.append(test,beamLoc[j]-1)
                # ttt[counter] = ttt[counter][:beamLoc[j]-1]+'|'+ttt[counter][beamLoc[j]:]

            if beamLoc[j]+1 not in test:
                test=np.append(test,beamLoc[j]+1)

                # ttt[counter] = ttt[counter][:beamLoc[j]+1]+'|'+ttt[counter][beamLoc[j]+2:]

            update = 1
            numSplit+=1            

# f = open("test.txt", "a")
# for i in ttt:
#     f.writelines(i)
# f.close()
   
print('Number of beam splits = '+str(numSplit))


# -------------------------------- Part 2 ---------------------------------------
