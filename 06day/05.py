'''
实现计算求最大公约数和最小公倍数的函数。
'''
def gcd(x,y):
    """求最大公约数"""
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x,y)


print(gcd(1,2))
print(lcm(1,2))