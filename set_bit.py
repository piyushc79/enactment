# Count total set bits in all numbers from 1 to n

def get_msb(n):
    m = 0
    while n > 1:
        n >>= 1
        m += 1
    return m


def get_set_bits(n):
    m = get_msb(n)
    if n == 1:
        return 1
    if n < 1:
        return 0
    x = n - (1 << m)
    return (x + 1) + m*(2**(m-1)) + get_set_bits(x)


if __name__ == "__main__":
    n = 10
    print "Total set bits in all numbers from 1 to {} is {}".format(n, get_set_bits(n))


