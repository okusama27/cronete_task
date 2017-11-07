def pile_factory(start=0):
    def pile(num):
        nonlocal start # nonlocalの指定が必須
        start += num
        print(start)
    return pile


pile1 = pile_factory(2)
pile2 = pile_factory(3)

pile1(3)
pile1(3)
pile1(3)
pile2(2)
pile2(2)
pile2(2)
a = pile_factory(2)
