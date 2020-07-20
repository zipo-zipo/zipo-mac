import itertools as its
words = input("请输入想要生成的数字、字母、特殊符号：").strip()
word1 = input("请输入前面的固定字符，若没有直接enter：").strip()
word2 = input("请输入后面的固定字符，若没有直接enter：").strip()
len = int(input("请输入密码的长度，不包含前面和后面的固定字符："))
words = set(words)   #去重
words = ''.join(words)   #拼接
#print(words)
r = its.product(words,repeat=len)
dic = open("passwd.txt",'a')
for i in r:
    dic.write(word1+''.join(i)+word2+"\n")
dic.close()
