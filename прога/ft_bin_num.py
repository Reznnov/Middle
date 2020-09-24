def ft_len_num(x):
    i = 0
    while x > 0:
        x = x // 10
        i += 1
    return i


def ft_bin_num(a):
    b = ""
    while a > 0:
        b += str(a % 2)
        a = a // 2
    b = b[::-1]
    return int(b)
    
