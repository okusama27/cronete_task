# - 今までに入力された数値の合計, 平均, 中央値を算出する 関数 summary を作ってみましょう
# >>> s = summary_factory()
# >>> s
# <function summary_factory.<locals>.summary at 0x1040e9510>
# >>> s(1)
# {'median': 1, 'avarage': 1.0, 'total': 1}
# >>> s(5)
# {'median': 3.0, 'avarage': 3.0, 'total': 6}
# >>> s(10)
# {'median': 5, 'avarage': 5.333333333333333, 'total': 16}
# >>> s(20)
# {'median': 7.5, 'avarage': 9.0, 'total': 36}
# >>> s(6)
# {'median': 6, 'avarage': 8.4, 'total': 42}
# >>> s(2)
# {'median': 5.5, 'avarage': 7.333333333333333, 'total': 44}
# >>> s(6)
# {'median': 6, 'avarage': 7.142857142857143, 'total': 50}
# >>> s(10)
# {'median': 6.0, 'avarage': 7.5, 'total': 60}
# >>> s(20)
# {'median': 6, 'avarage': 8.88888888888889, 'total': 80}

from statistics import mean
from statistics import median


def summary_factory():
    items = []

    def summary(num):
        items.append(num)
        total = sum(items)
        avarage = mean(items)
        median_ = median(items)

        print({'median': median_,
               'avarage': avarage,
               'total': total})
    return summary


if __name__ == '__main__':
    s = summary_factory()
    s(1)
    s(5)
    s(10)
    s(20)