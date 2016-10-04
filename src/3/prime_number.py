"""素数を返すジェネレーターを作ろう.

素数とは、自明な正の約数（1 と自分自身）以外に約数を持たない自然数であり、1 でない数のことである。
つまり、正の約数の個数が 2 である自然数のことである。
例えば、2 は、正の約数が 1, 2 のみなので素数である。
一方で 91 は、正の約数が 1, 7, 13, 91 なので素数でない。
素数でない 2 以上の自然数を合成数と呼ぶ。
また、特に 2 でない素数は奇数であり、奇素数と呼ぶ。
十進法表示では、2, 5 以外の素数は、一の位が 1, 3, 7, 9 のいずれかである。
"""

import math


def prime_gen(start=2):
    """素数を返すジェネレーター.
    総当り版
    """
    while True:
        flg_prime = True
        for i in range(2, start):
            if start % i == 0:
                flg_prime = False
                break
        res = start
        start += 1
        if flg_prime:
            yield res


prime_list = []


def prime_gen_list(start=2):
    """素数を返すジェネレーター.
    総当りしない版
    """
    while True:
        flg_prime = True
        for prime in prime_list:
            if start % prime == 0:
                flg_prime = False
                break
        res = start
        start += 1
        if flg_prime:
            prime_list.append(res)
            yield res


def prime_gen_eratosthenes(start=2):
    """素数を返すジェネレーター.
    エラトステネスの篩版

    wikipediaより
    指定された整数x以下の全ての素数を発見するアルゴリズム。右のアニメーションでは以下のステップにそって2 から 120 までの数に含まれる素数をさがしている。
    ステップ 1[ソースを編集]
    探索リストに2からxまでの整数を昇順で入れる。
    ステップ 2[ソースを編集]
    探索リストの先頭の数を素数リストに移動し、その倍数を探索リストから篩い落とす。
    ステップ 3[ソースを編集]
    上記の篩い落とし操作を探索リストの先頭値がxの平方根に達するまで行う。
    ステップ 4[ソースを編集]
    探索リストに残った数を素数リストに移動して処理終了。
    """
    s_list = list(range(2, start+1))
    end_num = math.sqrt(start)
    while True:
        x = s_list.pop(0)
        yield x
        if x > end_num:
            break
        for idx, s in enumerate(s_list):
            if s % x == 0:
                s_list.pop(idx)
    for res in s_list:
        yield res



if __name__=='__main__':
    # スタートする数値を指定
    max = 1000
    # g = prime_gen()
    # g = prime_gen_list()
    g = prime_gen_eratosthenes(max)
    print(g)
    # 1000までの素数
    while True:
        try:
            a = next(g)
        except:
            break
        if a > max:
            break
        print('answer=', a)