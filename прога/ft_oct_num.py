def ft_bin_num(a):
    desit = 1
    it = 0
    while a > 0:
        it += a % 8 * desit
        desit *= 10
        a //= 8
    return it
