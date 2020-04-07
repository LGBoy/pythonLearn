'''
输出99乘法表
'''
for i in range(1,10):
    for j in range(1,1+i):
        print('%d * %d = %d' % (j,i,i*j),end='\t')
    print()
