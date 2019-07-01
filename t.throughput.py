# simulation of throughput
import math
from random import random

def poisson(lam):
    L, k, p = math.exp(-lam), 1, random()
    while p > L:
        k = k + 1
        p = p * random()
    return k -1

def throughput_sec(lam): # lam = mean of times per sec
    return poisson(lam)
    
def throughput_min(lam): # lam = mean of times per min
    return sum([throughput_sec(lam/60) for i in range(60)])

def throughput_hour(lam): # lam = mean of times per hour
    return sum([throughput_sec(lam/3600) for i in range(3600)])

print("throughput of hours")
for i in range(50):
    print(throughput_hour(126.1))
    
print("throughput of mins")
for i in range(50):
    print(throughput_min(2.1)) # 126.1 / 60
    
print("throughput of sec")
for i in range(50):
    print(throughput_sec(0.035)) # 126.1 /3600
    
input("press enter to leave")
