# 1207 抽鬼牌
from random import randint

class Poker:
    def __init__(self,suit,number):
        self.s = suit
        self.n = number
    def __str__(self):
        return str(self.s) + str(self.n)
    def __repr__(self):
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
def show(hand, count = 0):
    count = len(hand) if count==0 else count
    for i in range(count):
        print(hand[i].s+hand[i].n, end=" ")
    print("")

# 產生洗好的牌庫
def getDeck():
    # s_list = ["Spade", "Heart", "Dimond", "Club"]
    # s_list = ["S", "H", "D", "C"]
    s_list = ["♠", "♥", "♦", "♣"] # symbol
    n_list = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    deck = [0]*53
    count = 0
    for s in s_list:
        for n in n_list:
            deck[count] = Poker(s,n)
            count += 1
    deck[count] = Poker("Joker","0")

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
    count = 0
    for i in range(len(h)):
        if not h[i].isEmpty():
            hand[count] = h[i]
            count += 1
            if count == n:
                break
    for i in range(count,len(hand)): # 後面填上空值
        hand[i] = Poker("","")

# 打亂手牌順序
def reshuffle(hand, n):
    if n == 0: return
    for i in range(n-1, 2, -1):
        j = randint(0,i)
        hand[i], hand[j] = hand[j], hand[i]
    return

# 建立紀錄表(沒有處理對子)
def mk_log(hand, n):
    log = [-1]*13
    for i in range(n):
        card_n = hand[i].getN()
        if card_n != 14: # 避免鬼牌放進紀錄
            log[card_n-1] = i
    return log

# 遊戲開始
deck = getDeck()
# show(deck)
h1 = [Poker("","")]*27
h2 = [Poker("","")]*26
dispatch(deck, h1, h2)
# show(h1)
# show(h2)

# 去除對子 P1
h1_log = [-1]*13 # 紀錄各點數牌的位置
h1_count = 27
for i in range(len(h1)):
    n = h1[i].getN() # 點數 1-14
    if type(n) is int and n != 14: # 非鬼牌
        if h1_log[n-1] == -1: # 沒有紀錄，把位置放進去
            h1_log[n-1] = i
        else: # 有紀錄，把兩張牌都清除，消除紀錄
            h1[i].clear()
            h1[h1_log[n-1]].clear()
            h1_log[n-1] = -1
            h1_count -= 2

# show(h1)
reset(h1, h1_count)
# show(h1)
reshuffle(h1, h1_count)
h1_log = mk_log(h1, h1_count)
# show(h1, h1_count)

# 去除對子 P2
h2_log = [-1]*13 # 紀錄各點數牌的位置
h2_count = 26
for i in range(len(h2)):
    n = h2[i].getN()
    if type(n) is int and n != 14: # 非鬼牌
        if h2_log[n-1] == -1: # 沒有紀錄，把位置放進去
            h2_log[n-1] = i
        else: # 有紀錄，把兩張牌都清除，消除紀錄
            h2[i].clear()
            h2[h2_log[n-1]].clear()
            h2_log[n-1] = -1
            h2_count -= 2
            
# show(h2)
reset(h2, h2_count)
# show(h2)
reshuffle(h2, h2_count)
h2_log = mk_log(h2, h2_count)
# show(h2,h2_count)

# 判斷遊戲是否結束
def isEnd():
    return hand_count[0] == 0 or hand_count[1] == 0

# 抽對方牌 P1開始，抽P2的牌
hand = [h1, h2]
log = [h1_log, h2_log]
hand_count = [h1_count, h2_count]

turn = 0
actor_id = turn % 2 # 0:P1, 1:P2
other_id = (actor_id+1) % 2

# 變數參照
# hand[actor_id] >> actor_hand
# log[actor_id] >> actor_hand_log
# hand_count[actor_id] >> actor_hand_count
# hand[other_id] >> other_hand
# log[other_id] >> other_hand_log
# hand_count[other_id] >> other_hand_count

while not isEnd(): # 遊戲沒結束就持續
    # print(actor_id, other_id)
    # show(hand[0], hand_count[0])
    # print(hand[0], log[0], hand_count[0])
    # show(hand[1], hand_count[1])
    # print(hand[1], log[1], hand_count[1])

    print(f"turn to player#{actor_id}")
    # 玩家抽一張牌到自己手牌 other > actor
    while True:
        s = input(f"choose [1 to {hand_count[other_id]}]: ") # 輸入抽牌的位置
        if s != "": # 防止空字串
            i = int(s) - 1 
        else:
            i = -1
        if 0<=i and i<=hand_count[other_id]-1: #數字必須符合才能離開
            break

    card = hand[other_id][i] #對手的牌
    card_n = card.getN() # 取得牌的點數
    print(f"card is {card}")

    hand_count[other_id] -= 1 # 對方手牌數量-1
    hand[other_id][i] = Poker("", "") # 去掉對方的牌
    reset(hand[other_id], hand_count[other_id]) # 重整對方的牌

    if type(card_n) is int and card_n != 14: # 非鬼牌
        if log[actor_id][card_n-1] == -1: # 沒有紀錄，無法形成對子，放入手牌
            hand_count[actor_id] += 1 # 自己手牌數量+1
            hand[actor_id][hand_count[actor_id]-1] = card # 放入手牌

        else: # 有紀錄，湊成對子，把牌消掉
            print(f"player#{actor_id} get a pair!")
            loc = log[actor_id][card_n-1] # 手牌中湊成對子的牌的位置
            hand[actor_id][loc] = Poker("", "") # 去掉自己的牌
            reset(hand[actor_id], hand_count[actor_id]) # 重整自己的牌
            hand_count[actor_id] -= 1 # 自己手牌數量-1

    elif type(card_n) is int and card_n == 14: # 抽到鬼牌
        print(f"player#{actor_id} get Joker!!")
        hand_count[actor_id] += 1 # 自己手牌數量+1
        hand[actor_id][hand_count[actor_id]-1] = card # 放入手牌

    show(hand[actor_id], hand_count[actor_id]) # 顯示玩家手牌
    reshuffle(hand[actor_id], hand_count[actor_id]) # 重洗自己的手牌，避免對手可以猜測
    log[actor_id] = mk_log(hand[actor_id], hand_count[actor_id]) # 重新建立自己的紀錄表
    log[other_id] = mk_log(hand[other_id], hand_count[other_id]) # 重新建立對方的紀錄表

    # 切換玩家
    turn += 1
    actor_id = turn % 2 # 0:P1, 1:P2
    other_id = (actor_id+1) % 2

if hand_count[0]==0:
    winner_id = 0
else:
    winner_id = 1
    
print(f"Game is over. Winner is player#{winner_id} !!")

