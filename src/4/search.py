routes = {
    ('a', 'b'): 3,
    ('b', 'c'): 4,
    ('c', 'd'): 10,
    ('d', 'e'): 7,
    ('a', 'f'): 4,
    ('b', 'g'): 6,
    ('c', 'h'): 8,
    ('d', 'i'): 4,
    ('e', 'j'): 10,
    ('f', 'g'): 10,
    ('g', 'h'): 3,
    ('h', 'i'): 9,
    ('i', 'j'): 1,
    ('f', 'k'): 4,
    ('g', 'l'): 3,
    ('h', 'm'): 8,
    ('i', 'n'): 6,
    ('j', 'o'): 9,
    ('k', 'l'): 8,
    ('l', 'm'): 4,
    ('m', 'n'): 7,
    ('n', 'o'): 2,
    ('k', 'p'): 3,
    ('l', 'q'): 9,
    ('m', 'r'): 2,
    ('n', 's'): 6,
    ('o', 't'): 6,
    ('p', 'q'): 6,
    ('q', 'r'): 6,
    ('r', 's'): 4,
    ('s', 't'): 10,
    ('p', 'u'): 3,
    ('q', 'v'): 5,
    ('r', 'w'): 1,
    ('s', 'x'): 10,
    ('t', 'y'): 1,
    ('u', 'v'): 3,
    ('v', 'w'): 5,
    ('w', 'x'): 6,
    ('x', 'y'): 4,
}


def get_next_points(start, all_routes):
    res = {}
    for k, v in all_routes.items():
        if k[0] == start:
            res[k] = v
    return res


def get_reverse_routes(rs):
    res = {}
    for k, v in routes.items():
        r_k = (k[1], k[0])
        res[r_k] = v

    return res


def search_next_route(start, end, path, cost, result, all_routes):
    next_points = get_next_points(start, all_routes)
    for k, v in next_points.items():
        pp = path + k[1]
        cc = cost + v
        if k[1] == end:
            if pp not in result:
                result[pp] = cc
        elif k[1] in path:
            pass
        else:
            search_next_route(k[1], end, pp, cc, result, all_routes)


def search(start, end):
    # 全ルート
    reverse_routes = get_reverse_routes(routes)
    all_routes = routes.copy()
    all_routes.update(reverse_routes)

    # 検索
    result = {}
    search_next_route(start, end, start, 0, result, all_routes)
    return result

if __name__ == "__main__":
    results = search('a', 'y')
    print('len:', len(results))
    print('min:', min((v, k) for k, v in results.items()))
    print('max:', max((v, k) for k, v in results.items()))
