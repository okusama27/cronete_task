# - 引数に与えた数だけ対象の関数を繰り返し実行するデコレータ
# repeat
# を作ってみましょう
#
# python
# >> > @repeat(3)
# def test(msg):
#     print(msg)
#
# >> > test('a')
# a
# a
# a


def repeat(num):
    def _repeat(f):
        @wraps(f)
        def _wrap(*args, **kwargs):
            for _ in range(num):
                f(*args, **kwargs)
        return _wrap
    return _repeat


@repeat(3)
def test(msg):
    print(msg)


if __name__ == '__main__':
    test('くろのて勉強会')
