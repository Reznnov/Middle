def ft_multi_num(x):
    summ = 1
    while x > 0:
        summ *= x % 10
        x = x // 10
    return summ
