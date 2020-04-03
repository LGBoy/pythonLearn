"""
比较运算符和逻辑运算符

逻辑运算符有三个
 and
 or
 not 运算符的后面会跟上一个布尔值，它的作用是得到与该布尔值相反的值，也就是说，
 后面的布尔值如果是True运算结果就是False，而后面的布尔值如果是False则运算结果就是True。
"""

flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print("flag0 = ", flag0)
print("flag1 = ", flag1)
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
print(flag1 is True)
print(flag1 is not True)