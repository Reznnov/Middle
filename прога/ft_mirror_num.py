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
        return "TRUE"
    else:
        return "FALSE"
