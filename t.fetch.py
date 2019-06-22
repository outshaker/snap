from time import time, sleep
from random import randint

def fix_time(): # return base_t, fix_t
    this_t = time()
    if 0 <= this_t % T <= T - 1: # make fix_t 1~61
        base_t = this_t - this_t % T # bast_t % T == 0
        fix_t = T - this_t % T
    else:
        base_t = int(this_t)
        # base_t = this_t - this_t % T # bast_t % T == 0
        fix_t = 1 + this_t % T
    return base_t, fix_t

def delay(): # make 0~1000 ms delay
    d = randint(0,1000)/1000
    # print("delay %.3f s" % d)
    return sleep(d)

T = 5 # 60, 30, 20, 15, 12, 10, 6, 5, 4, 3, 2, 1
print("fetch service start")
this_t = time()
base_t, fix_t = fix_time()
base_t = base_t - base_t%T
print("t=%.3f (%.3f), base=%.3f, fix=%.3f #init" % (this_t, this_t%T, base_t, fix_t))
cout = 0
while True:
    last_t = time()
    print("t=%.3f (%.3f), base=%.3f, d=%.3f #exec" % (last_t, last_t%T, base_t, last_t-base_t))
    delay()
    cout = cout + 1
    if cout == 6: # fix_time counter 
        cout = 0
        base_t, fix_t = fix_time()
        print("t=%.3f (%.3f), base=%.3f, fix=%.3f" % (last_t, last_t%T, base_t, fix_t))
        sleep(fix_t)
    else:
        base_t = int(last_t) # set next_base
        # print("t=%.3f (%.3f), base=%.3f #sleep" % (last_t, last_t%T, base_t))
        sleep(5)
