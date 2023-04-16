import numpy as np

cube = np.array([[4,9,2],[3,5,7],[8,1,6]])
sum = np.sum(cube[: , 1])
flag = True

for i in range ( 0 , cube.shape[1] ):
    if np.sum ( cube[ : , i ] ) != sum :
        flag = False

for i in range (0 , cube.shape[0]) :
    if np.sum ( cube[i , :] ) != sum :
        flag = False

if flag :
    print('this is magic cube')
else :
    print('this is not magic cube!!')