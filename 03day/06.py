'''
输入两个正整数，计算它们的最大公约数和最小公倍数。
两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。
'''

x = int(input('x = '))
y = int(input('y = '))
# 如果x大于y就交换x和y的值
if x > y:
    # 通过下面的操作将y的值赋给x, 将x的值赋给y
    x,y = y,x
for i in range(x,0,-1):
    if x % i == 0 and y % i == 0:
        print('%d和%d的最大公约数是%d' % (x,y,i))
        print('%d和%d的最小公倍数是%d' % (x,y,x*y // i))
        break

