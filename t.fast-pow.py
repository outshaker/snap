# 使用矩陣快速冪計算費氏數列

import time

def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {(end_time - start_time)*1000:.0f} ms to execute")
        return result
    return wrapper

class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        # return '\n'.join([' '.join([str(x) for x in row]) for row in self.data])
        return str(self.data)

    def __mul__(self, other):
        a = self.data
        b = other.data
        c11 = a[0][0]*b[0][0] + a[0][1]*b[1][0]
        c12 = a[0][0]*b[0][1] + a[0][1]*b[1][1]
        c21 = a[1][0]*b[0][0] + a[1][1]*b[1][0]
        c22 = a[1][0]*b[0][1] + a[1][1]*b[1][1]
        return Matrix([[c11, c12], [c21, c22]])

    def __imul__(self, other):
        a = self.data
        b = other.data
        c11 = a[0][0]*b[0][0] + a[0][1]*b[1][0]
        c12 = a[0][0]*b[0][1] + a[0][1]*b[1][1]
        c21 = a[1][0]*b[0][0] + a[1][1]*b[1][0]
        c22 = a[1][0]*b[0][1] + a[1][1]*b[1][1]
        self.data = [[c11, c12], [c21, c22]]
        return self

    def __pow__(self, power):
        # chatGPT ver
        # if power == 0:
            # return Matrix([[1, 0], [0, 1]])  # 返回單位矩陣
        # elif power == 1:
            # return self  # 返回自身
        # elif power % 2 == 0:
            # m = self ** (power // 2)
            # return m * m
        # else:
            # return self * (self ** (power - 1))

        # 自己實作的迭代版本
        if power == 0:
            return Matrix([[1, 0], [0, 1]])

        elif power > 0:
            cmd = bin(int(power))[3:] # 0b1xxxx
            result = Matrix(self.data)

            # i = 1
            for c in cmd[3:]:
                result *= result
                if c == '1':
                    # i = i * 2 + 1
                    result *= self
                    # print('x2+1', i)
                # else:
                    # i = i *2
                    # print('x2', i)
            return result

        else: # 暫時不實作負數版本
            return None

    # 取得費氏數列 Fn 的值
    def val(self):
        return self.data[0][1]

@timing
def fib(n):
    if n <= 0: return 0
    return (Matrix([[1,1],[1,0]]) ** n).val()

# for i in range(1, 20):
    # print(fib(i))

print(fib(10 ** 3))
print(fib(10 ** 4))
print(fib(10 ** 5))

# 0ms 1ms 16ms chatGPT ver
# 182ms 300 ms 550 ms 自己實作版本 有 print 資訊
# 1ms 0ms 1ms 自己實作版本 無 print 資訊

