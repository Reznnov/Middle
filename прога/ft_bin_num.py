def ft_bin_num(a):
    desit = 1
    it = 0
    while a > 0:
        it += a % 2 * desit
        desit *= 10
        a //= 2
    return it
