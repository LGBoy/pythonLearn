'''
生成斐波那契数列的前20个数
斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，
形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。
'''
one = 1
two = 1
three = 0
for x in range(1,21):
    if x == 1 or x == 2:
        print(1,end=",")
    else:
        three = one + two
        one = two
        two = three
        print(three,end=",")
