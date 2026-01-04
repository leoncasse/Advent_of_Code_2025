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
pwd_p2 = 0
pass_zero = 0
test = 0
test2 = 0
test3 = 0

# loop over all codes to find password
for j in range(f_dir.size):

    print('Iteration '+str(j))
    new_val = int(f_val[j])
    new_dir = f_dir[j]
    
    # if value is more than one full rotation get number of rotations
    if new_val > 99:
        print(new_val)
        full_rot = int(np.floor(new_val/100)*100)
        new_val = new_val-full_rot
        pass_zero += int(full_rot/100)   # count the number of times the dial passes 0
        
        print(int(full_rot/100))

        # if dial == 0 and new_val == 0:
                # pass_zero -= 1   # count the number of times the dial passes 0

        
    # check if the dial crosses 0 and adjust
    if new_dir == 'L' and new_val>dial:
        dial = dial+100
        pass_zero += 1       # count the number of times the dial passes 0
        test += 1
    elif new_dir == 'R' and dial+new_val>99:
        dial = dial-100
        test += 1
        # if dial+int(new_val)>0:
        pass_zero += 1   # count the number of times the dial passes 0

    # get new dial location
    if f_dir[j]=='L':
        dial = dial-int(new_val)
        if dial == 0:
            test2 += 1
            pass_zero += 1
    else:
        dial = dial+int(new_val)
        if dial == 0:
            test3 += 1

    # print(dial)
    # print(pass_zero)


    if dial == 0:
        pwd_p1 += 1
        test += 1

pwd_p2 = pass_zero

print('Password = ' + str(pwd_p1))
print('Passing 0 = ' + str(pass_zero))
print(' ')
print('Password using new method = ' + str(int(pwd_p2)))
print(test2)
print(test3)

current_position = 50
pwd_p1 = 0
pwd_p2 = 0
pass_zero = 0
alreadyZero = 0
landed_passed = 0

# loop over all codes to find password
for j in range(f_dir.size):
    landed_passed = 0
    full_rot = 0
    print('Iteration '+str(j))

    new_val = int(f_val[j])
    new_dir = f_dir[j]

    if new_val > 99:
        full_rot = int(np.floor(new_val/100)*100)
        new_val = new_val-full_rot
        
        print(int(full_rot/100))

        if current_position == 0:
            alreadyZero += 1

    if f_dir[j]=='L':
        dial = current_position-int(new_val)
        
    else:
        dial = current_position+int(new_val)
    
    
    if current_position != 0 and not (0 < dial < 100):
         landed_passed = 1

    pass_zero += int(full_rot/100) + landed_passed

    current_position = dial % 100

print(pass_zero)
print('alreadyZero = '+ str(alreadyZero))
