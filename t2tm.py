from time import time

def isLeap(y): return (y%4==0 and y%100!=0) or (y%400==0)
def yday(y): return 366 if isLeap(y) else 365
_mday = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
_mday2 = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]

t = int(time())
print(t)
t += 8*60*60 # shift to GTM+0800

d,t = divmod(t,86400)
print(d)

y=1970
while d >= yday(y):
    d -= yday(y)
    y += 1
print(y)

mday = _mday2 if isLeap(y) else _mday

for i in range(11):
    if mday[i] < d <= mday[i+1]:
        M = i + 1
        d = d - mday[i] + 1

print(M)

h,t = divmod(t,3600)
m,t = divmod(t,60)
s = t

print(y,M,d,h,m,s)
