"""2. 螺旋の座標を出力するジェネレーターを作ろう.

x=0, y=0 を中心として資格の螺旋を書くための座標を一つずつ返却するジェネレーター
螺旋は反時計回りに回転
sendメソッドで座標の開始座標を指定できる
"""


def spiral(x=0, y=0):
    while True:
        if abs(x) > abs(y):
            if x < 0:
                y -= (abs(y)*2 + 1)
            else:
                y = abs(x)
        elif abs(x) == abs(y):
            if x == 0:
                x -= 1
            elif x < 0 and y >= 0:
                y -= (abs(y) + 1)
            elif x < 0 and y <0:
                x += abs(x)*2
            elif x >= 0 and y < 0:
                y += abs(y)*2
            else:
                x -= (abs(x)*2 + 1)

        yield x, y



if __name__ == '__main__':
    x = 0
    y = 0
    print(x, y)
    g = spiral(x, y)
    for i in range(20):
        a, b = next(g)
        print(a, b)