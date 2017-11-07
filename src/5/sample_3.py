id = 1
int = 1
a = 1
b = 1


def outer():
    id = 2
    a = 2

    def inner():
        id = 3
        range = 3
        # この記法ができるのは Python3.6 から
        print('id:', id, 'len:', len, 'int:', int, 'range:', range, 'a:', a, 'b:', b)

    inner()

if __name__ == '__main__':
    outer()
