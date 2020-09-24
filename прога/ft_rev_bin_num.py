def ft_pow(a, s):
    b = a
    if s > 0:
        for i in range(s - 1):
            a *= b
        return a
    elif s == 0:
        return 1
    for i in range(a):
        a /= b
    return a


def ft_rev_bin_num(x):
    povtor = x
    otvet = 0
    d = 0
    while povtor > 0:
        povtor //= 10
        d += 1
    for digit in range(d):
        otvet += x % 10 * ft_pow(2, digit)
        x //= 10
    return otvet


