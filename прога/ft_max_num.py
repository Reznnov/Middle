def ft_max_num(x):
    summ = 0
    while x > 0:
        if summ < x % 10:
            summ = x % 10
        x = x // 10
    return summ
