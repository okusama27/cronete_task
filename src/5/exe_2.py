# """
#   >>> byte_factory = factory({'B': 1, 'KB': 1024, 'MB': 1024**2, 'GB': 1024**3, 'TB': 1024**4, 'PB': 1024**5})
#   >>> byte_factory('30GB')  # 30GB は 何Byte か
#   32212254720  # byte
#
#   >>> second_factory = factory({'S': 1, 'M': 60, 'H': 3600, 'D': 3600*24, 'W': 3600*24*7})
#   >>> second_factory('5H')  # 5時間 は 何秒 か
#   18000  # 秒
#
#
# - 引数に与えた数だけ対象の関数を繰り返し実行するデコレータ repeat を作ってみましょ
# """
import re
prog = re.compile('([0-9]+)([a-zA-Z]+)')


def factory_(unit_list={}):
    def calc(input_):
        p = prog.match(input_)
        num = p.group(1)
        unit = p.group(2)
        statm = unit_list[unit]
        print('statm=', statm)

        answer = int(num) * int(statm)
        print('answer=', answer)
    return calc


if __name__ == '__main__':
    byte_factory = factory_({'B': 1, 'KB': 1024, 'MB': 1024 ** 2, 'GB': 1024 ** 3, 'TB': 1024 ** 4, 'PB': 1024 ** 5})
    answer1 = byte_factory('30GB')

    second_factory = factory_({'S': 1, 'M': 60, 'H': 3600, 'D': 3600 * 24, 'W': 3600 * 24 * 7})
    answer2 = second_factory('5H')