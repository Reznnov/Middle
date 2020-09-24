def ft_rev_num(a):
    chis = 0
    degit = 0
    while a > 0:
        degit = a % 10
        chis = chis * 10
        chis += degit
        a //= 10
    return chis
        
        
    
