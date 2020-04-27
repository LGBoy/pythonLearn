s1 = 'hello, world!'
s2 = "hello, world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello, 
world!
"""
print(s1, s2, s3, end='')

s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')
#在\后面还可以跟一个八进制或者十六进制数来表示字符，例如\141和\x61都代表小写字母a，
# 前者是八进制的表示法，后者是十六进制的表示法。也可以在\后面跟Unicode字符编码来表示字符，例如\u9a86\u660a代表的是中文“骆昊”。
s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)
#如果不希望字符串中的\表示转义，我们可以通过在字符串的最前面加上字母r来加以说明。
s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')