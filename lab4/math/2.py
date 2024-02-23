import math

def trap_area(height,base1,base2):
    trap=(base1+base2)/2*height
    return trap
height=int(input())
base1=int(input())
base2=int(input())
trap=trap_area(height,base1,base2)
print(trap)