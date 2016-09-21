import numpy as np

Z = np.zeros((6,6))
Z[1,3] =1
Z[2,1] =1
Z[2,3] =1
Z[3,2] =1
Z[3,3] =1
print Z

def iterate(Z):
    N = (Z[0:-2,0:-2] + Z[0:-2,1:-1] +Z[0:-2,2:] +
         Z[1:-1,0:-2]  +Z[1:-1,2:] +
         Z[2:,0:-2] + Z[2:,1:-1] +Z[2:,2:])
    survive = ((N==3) & (Z[1:-1,1:-1]==0))
    birth = (((N==3)|(N==2))&(Z[1:-1,1:-1]==1))
    Z[...] = 0
    Z[1:-1,1:-1][survive|birth] = 1
    return Z

for i in range(0,10):
    Z = iterate(Z)
    print Z
