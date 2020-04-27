'''
输出100以内所有的素数。
素数指的是只能被1和自身整除的正整数（不包括1）。
'''

for x in range(2,101):
    for j in range(2,x):
        if x % j == 0:
            break
    else:
        print(x,end=',')