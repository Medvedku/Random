import numpy as np

## Element parameters 
Coor = np.array([[0, 0], [3, 1], [3.5, 3.2], [0.5, 3]])
t = 1    #thickness
E = 1
mju = 0.3
ro = 1

## Loading parameters 
P = [0, 0, 0, 0, 2, 2, 0, 0] #concetrated load
b = [0, -1]
tn = [-1, 0]

## Constitutive relationship
CStress = (E / (1+mju)) * np.array([
    [1/(1-mju),   mju/(1-mju), 0],
    [mju/(1-mju), 1/(1-mju),   0],
    [0,           0,         1/2] ])

CStrain = (E / ((1+mju)*(1-2*mju))) * np.array([
    [1-mju,   mju,   0],
    [mju,   1-mju,   0],
    [0,         0,   (1-2*mju)/2] ])

Cc = CStress

## Step 1 - Stiffness matrix
#  Shape Functions

def N1(xi, eta):
    return (1-xi) * (1-eta) / 4
def N2(xi, eta):
    return (1+xi) * (1-eta) / 4
def N3(xi, eta):
    return (1+xi) * (1+eta) / 4
def N4(xi, eta):
    return (1-xi) * (1-eta) / 4
#Ni = [N1, N2, N3, N4]

# # Coordinate Mapping
# x = 0
# y = 0
# for i in range(4):
#     x += Ni[i]*Coor[i,1]
#     x += Ni[i]*Coor[i,2]
# CoordMap = [x, y]

# N matrix
def N_m(xi, eta):
    N_matrix = np.array([
        [N1(xi, eta),           0, N2(xi, eta),           0, N3(xi, eta),           0, N4(xi, eta),           0 ],
        [          0, N1(xi, eta),           0, N2(xi, eta),           0, N3(xi, eta),           0, N4(xi, eta) ] ])
    return N_m

# Jacobian Matrix
def Jac():
    pass

# B matrix


pass