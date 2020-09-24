def ft_rev_num(a):
    chis = 0
    degit = 0
    while a > 0:
        degit = a % 10
        chis = chis * 10
        chis += degit
        a //= 10
    return chis


def ft_mirror_num(x):
    rev = ft_rev_num(x)
    if x == rev:
        return True
    else:
        return False


def ft_mirror_count(b):
    n = 0
    for i in range(1, b + 1):
        if ft_mirror_num(i) is True:
            n += 1
    return n
