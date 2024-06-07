def campingDay():
    l, p, v = map(int, input().split())
    count = 0
    if 1 < l < p < v:
        count += 1
        full = v // p
        remain_day = v % p
        fullday = (full) * l
        remain = min(l, remain_day)

        asn = fullday + remain
        print(f"case {count}: {asn}")
    else:
        print("")


campingDay()
