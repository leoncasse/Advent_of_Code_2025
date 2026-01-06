import numpy as np

f = np.loadtxt('Data/input_day4.txt', dtype = str)
f = np.char.replace(f, '@', '1')
f = np.char.replace(f, '.', '0')

f2 = '0'*136
f = np.hstack([f2,f,f2])

accessible = 0

for i in range(1,len(f)-1):
    above  = f[i-1]
    middle = f[i]
    below  = f[i+1]

    for j in range(0,len(middle)):
        a_l = a_m = a_r = m_l = m_r = b_l = b_m = b_r = 0
        if middle[j] == '1':

            if j == 0:
                a_m = above[j]
                a_r = above[j+1] 
                   
                m_r = middle[j+1]

                b_m = below[j]
                b_r = below[j+1]

            elif j == len(middle)-1:
                a_m = above[j]
                a_l = above[j-1] 
                   
                m_l = middle[j-1]

                b_m = below[j]
                b_l = below[j-1]
                
            else:
                a_l = above[j-1]
                a_m = above[j]
                a_r = above[j+1]

                m_l = middle[j-1]
                m_r = middle[j+1]

                b_l = below[j-1]
                b_m = below[j]
                b_r = below[j+1]
                
            if int(a_l) + int(a_m) + int(a_r) + int(m_l) + int(m_r) + int(b_l) + int(b_m) + int(b_r) < 4:
                accessible += 1

print(' ')
print('Accessible stacks: ' + str(accessible))