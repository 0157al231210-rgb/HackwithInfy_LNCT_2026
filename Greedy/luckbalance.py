def luckBalance(k, contests):
    # Write your code here
    res = 0
    important = []
    for l,c in contests:
        if c == 0:
            res += l
        else:
            important.append(l)
    important.sort(reverse = True)
    res += sum(important[:k])
    res -= sum(important[k:])
    return res