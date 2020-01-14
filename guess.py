from random import sample
from functools import reduce

def checkNumber(s): return all(c in '0123456789' for c in s)
def checkOnce(s): return len(s) == len(set(s))
def countAB(ans, x): return sum(1 if i in set(ans) else 0 for i in x)
def countA(ans, x): return sum(1 if ans[i] == x[i] else 0 for i in range(4))

ans = reduce(lambda x,y: x+y, sample("0123456789", 4), "")
print(ans) # INFO

t = 0
while True:
    x = input("Enter number: ")
    if checkNumber(x) and checkOnce(x):
        a = countA(ans,x)
        b = countAB(ans,x) - a
        t += 1
        print(f"Round {t}: {x} {a}A{b}B")
        if a == 4:
            print("you win!")
            break
    else:
        print("not number or Duplicate numbers appear, please try again")
