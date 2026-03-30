import numpy as np

with open('Data/input_day7.txt', 'r') as file:
    lines = file.readlines()


# -------------------------------- Part 1 & 2 ---------------------------------------
update = 0                            # Switch to determine if a line is fully processed
beamLoc = [lines[0].find('S')]        # location of beam
test=np.array(beamLoc)                # copy of beamLoc as np array
numSplit=0                            # counter for number of times a beam is split
beamDimens = np.zeros(len(lines[1]))  # counter for number of dimensions particle flows to specific column
beamDimens[beamLoc] = 1

for i in lines[1:141]:
    if update == 1:
        beamLoc = test

    update = 0
    
    for j in range(0,len(beamLoc)):
        if i[beamLoc[j]]!='.':

            beamDimens[beamLoc[j]+1]+= beamDimens[beamLoc[j]]
            beamDimens[beamLoc[j]-1]+= beamDimens[beamLoc[j]]
            beamDimens[beamLoc[j]] = 0

            test = np.delete(test, test==beamLoc[j])

            if beamLoc[j]-1 not in test:
                test=np.append(test,beamLoc[j]-1)

            if beamLoc[j]+1 not in test:
                test=np.append(test,beamLoc[j]+1)

            update = 1
            numSplit+=1   

print('Number of beam splits = '+str(numSplit))
print('Number of beam splits = '+str(sum(beamDimens)))