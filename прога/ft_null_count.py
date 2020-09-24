def ft_null_count(x):
    coll = 0
    degit = 0
    while x > 0:
        degit = x % 10
        if degit == 0:
            coll += 1
        x //= 10
    return coll
