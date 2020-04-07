"""
猜数字游戏

Version: 0.1
Author: 骆昊
"""
import random
answer = random.randint(1,100)
count = 0
while True:
    count += 1
    number = int(input("请输入："))
    if answer < number :
        print('da yi dian ')
    elif answer > number :
        print('xiao yi dian')
    else:
        print('da dui le')
        break
print('你总共猜了%d' % count)
if count > 7:
    print('你的智商余额明显不足')





