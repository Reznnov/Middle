def ft_max_num(x):
    summ = 0
    while x > 0:
        if summ < x % 10:
            summ = x % 10
        x = x // 10
    return summ


def ft_min_num(y):
    summ = 9999999
    while y > 0:
        if summ > y % 10:
            summ = y % 10
        y = y // 10
    return summ


def ft_second_max_num(a):
    maxx = ft_max_num(a)
    minn = ft_min_num(a)
    itog = -1
    for i in str(a):
        if maxx > int(i) > minn:
            if itog < int(i):
                itog = int(i)
    if itog == -1:
        return maxx
    else:
        return itog
