import math 

def degree_rad(degree):
    radian=degree*(math.pi/180)
    return radian
degree=int(input())
radian=degree_rad(degree)
print(radian)
    
