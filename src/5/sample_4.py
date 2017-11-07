g = 1


def a(b):
    global g
    g += b
    print(g)

if __name__ == '__main__':
    a(100)
    print(g)