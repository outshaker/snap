# Newton's Method 牛頓迭代法練習

def test(n):
    # mkf = lambda n: lambda x: x - (x ** 2 - n) / (x * 2) # 原始版本
    # mkf = lambda n: lambda x: (x + n / x) / 2 # 簡化算式
    # f = mkf(n)
    # x = n / 2 # 設定初始值，可以再調整
    # for i in range(10): # 最多迭代 10 次
        # next = f(x)
        # print(x)
        # if abs(x - next) < 1e-6: # 收斂到足夠小，退出
            # return next
        # else:
            # x = next

    mk_delta = lambda n: lambda x: (n / x - x) / 2
    delta = mk_delta(n)

    # e = 1e-6 # 精度，誤差在這以內即可
    # e = 1e-4 # 日常生活精度到小數點以下四位已經足夠
    # e = 5e-1 # 在大數字的情況下只要不要差太多都可以接受，差不多是四捨五入的誤差
    e = 1e-1 # 調高一點

    x = n / 2 # 設定初始值，可以再調整
    # x = 1e-6 # 故意從零附近開始，效果很差
    # x = 1 # 效果還可以

    for i in range(20): # 最多迭代 20 次
        d = delta(x) # 計算修正量
        if abs(d) < e: break # 如果修正量很小表示已經穩定，可以退出
        x += d # 更新 x
        print(f'({i}) x={x}, d={d}')
    print(f'n={n}, x={x}, try {i} times')

test(2)
test(3)
test(7)
test(1e1)
# test(999)
test(1e3)
test(1e5)
test(1e7)

