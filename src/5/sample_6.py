g = 1


def a():
    global g, h
    print(g, h)


def b():
    c = 1

    def bb():
        nonlocal c, d
        print(c, d)


if __name__ == '__main__':
    a()

#     nonlocal c, d
# SyntaxError: no binding for nonlocal 'd' found
