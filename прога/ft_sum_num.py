def ft_sum_num(x):
    summ = 0
    while x > 0:
        summ += x % 10
        x = x // 10
    return summ
