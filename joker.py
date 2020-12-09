# 1207 抽鬼牌
from random import randint

class Poker:
    def __init__(self,suit,number):
        self.s = suit
        self.n = number
    def __str__(self):
        return str(self.s) + str(self.n)
    
    def clear(self):
        self.s = ""
        self.n = ""
    def getN(self):
        if self.s == "Joker": return 14
        n_list = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        n = 0
        for i in range(len(n_list)):
            if self.n == n_list[i]:
                n = i+1
                break
        return n
    def isEmpty(self):
        return self.s == "" and self.n == ""

# 顯示手牌
def show(hand, cout = 0):
    cout = len(hand) if cout==0 else cout
    for i in range(cout):
        print(hand[i],end=" ")
    print("")

def getDeck():
    # s_list = ["Spade", "Heart", "Dimond", "Club"]
    s_list = ["S", "H", "D", "C"]
    n_list = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    deck = [0]*53
    cout = 0
    for s in s_list:
        for n in n_list:
            deck[cout] = Poker(s,n)
            cout += 1
    deck[cout] = Poker("Joker","0")

    for i in range(len(deck)-1, 2,-1):
        j = randint(0,i)
        deck[i], deck[j] = deck[j], deck[i]
    return deck

# 發牌給雙方玩家
def dispatch(deck, h1, h2):
    for i in range(len(deck)):
        if i%2 == 0:
            h1[i//2] = deck[i]
        else:
            h2[(i-1)//2] = deck[i]

# 重置手牌順序(空白牌往後)
def reset(hand, n):
    h = hand # 儲存原始資料，hand資料會被蓋掉
    cout = 0
    for i in range(len(h)):
        if not h[i].isEmpty():
            hand[cout] = h[i]
            cout += 1
            if cout == n:
                break
    for i in range(cout+1,len(hand)): # 後面填上空值
        hand[i] = Poker("","")

# 打亂手牌順序
def reshuffle(hand, n):
    if n == 0: return
    for i in range(n-1, 2):
        j = randint(0,i)
        hand[i], hand[j] = hand[j], hand[i]
    return

# 建立紀錄表(沒有處理對子)
def mk_log(hand, n):
    log = [-1]*13
    for i in range(n):
        card_n = hand[i].getN()
        log[card_n-1] = i
    return log

# 遊戲開始
deck = getDeck()
show(deck)
h1 = [Poker("","")]*27
h2 = [Poker("","")]*26
dispatch(deck, h1, h2)
show(h1)
show(h2)

# 去除對子 P1
h1_log = [-1]*13 # 紀錄各點數牌的位置
h1_cout = 27
for i in range(len(h1)):
    n = h1[i].getN() # 點數 1-14
    if type(n) is int and n != 14: # 非鬼牌
        if h1_log[n-1] == -1: # 沒有紀錄，把位置放進去
            h1_log[n-1] = i
        else: # 有紀錄，把兩張牌都清除，消除紀錄
            h1[i].clear()
            h1[h1_log[n-1]].clear()
            h1_log[n-1] = -1
            h1_cout -= 2

show(h1)
reset(h1, h1_cout)
show(h1)
reshuffle(h1, h1_cout)
show(h1)

# 去除對子 P2
h2_log = [-1]*13 # 紀錄各點數牌的位置
h2_cout = 26
for i in range(len(h2)):
    n = h2[i].getN()
    if type(n) is int and n != 14: # 非鬼牌
        if h2_log[n-1] == -1: # 沒有紀錄，把位置放進去
            h2_log[n-1] = i
        else: # 有紀錄，把兩張牌都清除，消除紀錄
            h2[i].clear()
            h2[h2_log[n-1]].clear()
            h2_log[n-1] = -1
            h2_cout -= 2
            
show(h2)
reset(h2, h2_cout)
show(h2)
reshuffle(h2, h2_cout)
show(h2)

# 判斷遊戲是否結束
def isEnd():
    return h1_cout == 0 or h2_cout == 0

# 抽對方牌 P1開始，抽P2的牌
hand = [h1, h2]
log = [h1_log, h2_log]
hand_cout = [h1_cout, h2_cout]

turn = 0
actor_id = turn % 2 # 0:P1, 1:P2
other_id = (acter_id+1) % 2

actor_hand = hand[actor_id]
actor_hand_log = log[actor_id]
actor_hand_cout = hand_cout[actor_id]
other_hand = hand[other_id]
other_hand_log = log[other_id]
other_hand_cout = hand_cout[other_id]

# while not isEnd():

# 抽一張牌到 other > actor
i = int(input(f"choose [1 to {other_hand_cout}]: ")) - 1
card = other_hand[i]
card_n = card.getN()
if type(card_n) is int and card_n != 14: # 非鬼牌
    if actor_hand_log[card_n-1] == -1: # 沒有紀錄，無法形成對子，放入手牌
        hand_cout[actor_id] += 1 # 手牌數量+1
        hand[actor_id][hand_cout[actor_id]] = card # 放入手牌
        log[actor_id][card_n-1] = hand_cout[actor_id] # 更新紀錄表
        
        reshuffle(hand[actor_id], hand_cout[actor_id]) # 重洗手牌
        log[actor_id] = mk_log(hand[actor_id], hand_cout[actor_id]) # 重新建立

    else: # 有紀錄，湊成對子，把牌消掉
        hand_cout[actor_id] -= 1 #手牌數量-1
        loc = log[actor_id][card_n] # 手牌中湊成對子的牌的位置
        hand[actor_id][loc].clear() # 清掉牌
        log[actor_id][card_n-1] = -1 #更新紀錄表

elif type(card_n) is int and card_n == 14: # 鬼牌