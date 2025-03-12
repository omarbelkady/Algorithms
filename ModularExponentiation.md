function ModularExponentiation(base, exponent, mod):
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exponent = exponent // 2
    return result