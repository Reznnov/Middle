def ft_len_num(x):
    i = 0
    while x > 0:
        x = x // 10
        i += 1
    return i


def ft_mirror_num(a):
    povtor = a
    chis = ""
    for j in range(ft_len_num(a)):
        chis += str(a % 10)
        a = a // 10
    if int(chis) == povtor:
        return "TRUE"
    else:
        return "FALSE"
