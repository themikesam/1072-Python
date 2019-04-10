# 123456 -> 654321
# define if x = reverse(x) then we can x is 回文
# give x
# while x is not 回文
# x = x + reverse
# show 最後的回文， 以及加法次數


def reverse(x):
    rX = 0
    rX += x % 10
    x = x // 10
    while x != 0:
        rX *= 10
        rX += x % 10
        x = x // 10
    return rX


def isReverse(x, y):  # 寫一個函式用來判斷是否是自身的回文值
    turn = 1  # 用於記錄回合數
    while x != y:  # 當不等於自身回文值
        print(x, y)
        x = x + y  # 加上自身回文值
        y = reverse(x)  # 記錄新的回文值
        turn += 1  # 回合數加一
    print(x, y)
    
    return turn, x


def main():
    x = int(input())
    print(isReverse(x, reverse(x)))


main()
