# Hex Ed

import sys


# Build dictionary of direction counts
def map_route(route):
    directions = {}
    directions["n"] = 0
    directions["ne"] = 0
    directions["se"] = 0
    directions["s"] = 0
    directions["sw"] = 0
    directions["nw"] = 0

    max_res = 0
    for x in route:
        directions[x] += 1
        # Calculate distance
        n_s = directions["n"] - directions["s"]
        ne_sw = directions["ne"] - directions["sw"]
        nw_se = directions["nw"] - directions["se"]

        # Really overkill if statment
        if n_s >= 0 and ne_sw >= 0 and nw_se >= 0:
            res = n_s + max(ne_sw, nw_se)
        elif n_s >= 0 and ne_sw >= 0 and nw_se < 0:
            res = ne_sw + max(n_s, abs(nw_se))
        elif n_s >=0 and ne_sw < 0 and nw_se >= 0:
            res = nw_se + max(n_s, abs(ne_sw))
        elif n_s >= 0 and ne_sw < 0 and nw_se < 0:
            res = abs(n_s - max(abs(ne_sw), abs(nw_se)))
        elif n_s < 0 and ne_sw >= 0 and nw_se >= 0:
            res = abs(max(ne_sw, nw_se) - abs(n_s))
        elif n_s < 0 and ne_sw >= 0 and nw_se < 0:
            res = max(ne_sw, abs(n_s)) + abs(nw_se)
        elif n_s < 0 and ne_sw < 0 and nw_se >= 0:
            res = max(nw_se, abs(n_s)) + abs(ne_sw)
        else:
            res = abs(n_s) + max(abs(ne_sw), abs(nw_se))
        if res > max_res:
            max_res = res
    print res, max_res


if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    map_route(f.read().strip().split(','))
