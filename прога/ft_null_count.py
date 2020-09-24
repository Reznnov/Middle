def ft_null_count(x):
    coll = 0
    for i in str(x):
        if int(i) == 0:
            coll += 1
    return coll
