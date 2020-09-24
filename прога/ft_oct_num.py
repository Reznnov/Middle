def ft_len_num(x):
    i = 0
    while x > 0:
        x = x // 10
        i += 1
    return i


def ft_oct_num(z):
    dlin = ft_len_num(z)
    vrem = 0
    obrat = 0
    raz = 1
    decit = 1
    second_dlin = ft_len_num(vrem)
    for c in range(dlin):
        decit *= 10
    while z > 0:
        vrem += z % 8 * decit
        z = z // 8
        decit //= 10
    for g in range(second_dlin):
        raz *= 10
    while vrem > 0:
        obrat += vrem % 10 * second_dlin
        vrem //= 10
        second_dlin //= 10
    return obrat


print(ft_oct_num(100))
