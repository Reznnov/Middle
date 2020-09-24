def ft_len_num(x):
    i = 0
    while x > 0:
        x = x // 10
        i += 1
    return i
