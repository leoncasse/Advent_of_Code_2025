import numpy as np

# load data
f = np.loadtxt('Data/day1/Day1_input1.txt', dtype = str)

# initialize list of values (rotation direction and magnitude)
f_dir = []
f_val = []

# seperate number from direction
counter = 0
for i in f:
    counter = counter+1
    f_dir = np.append(f_dir, i[0])
    f_val = np.append(f_val, i[1:])

# initial settings
dial = 50
pwd_p1 = 0

# loop over all codes to find password
for j in range(f_dir.size):
    new_val = int(f_val[j])
    new_dir = f_dir[j]
    
    # if value is more than one full rotation get number of rotations
    if new_val > 99:
        full_rot = int(np.floor(new_val/100)*100)
        new_val = new_val-full_rot

    # check if the dial crosses 0 and adjust
    if new_dir == 'L' and new_val>dial:
        dial = dial+100
    elif new_dir == 'R' and dial+new_val>99:
        dial = dial-100

    # get new dial location
    if f_dir[j]=='L':
        dial = dial-int(new_val)
    else:
        dial = dial+int(new_val)

    if dial == 0:
        pwd_p1 += 1

print(' ')
print('Password (part 1) = ' + str(pwd_p1))

current_position = 50
pass_zero = 0

# loop over all codes to find password
for j in range(f_dir.size):
    landed_passed = 0
    full_rot = 0

    new_val = int(f_val[j])
    new_dir = f_dir[j]

    if new_val > 99:
        full_rot = int(np.floor(new_val/100)*100)
        new_val = new_val-full_rot
        
    if f_dir[j]=='L':
        dial = current_position-int(new_val)
        
    else:
        dial = current_position+int(new_val)
    
    
    if current_position != 0 and not (0 < dial < 100):
         landed_passed = 1

    pass_zero += int(full_rot/100) + landed_passed

    current_position = dial % 100

print('Password (part 2) = '+ str(pass_zero))
