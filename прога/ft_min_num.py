def ft_min_num(x):
    summ = 9999999
    while x > 0:
        if summ > x % 10:
            summ = x % 10
        x = x // 10
    return summ
