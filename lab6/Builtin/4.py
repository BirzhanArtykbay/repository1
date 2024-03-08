import math
import time
num = float(input())
time = float(input())
t = time/1000
time.sleep(t)
print(f"Square root of {num} after {time} miliseconds is {math.sqrt(num)}")