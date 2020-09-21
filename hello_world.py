# a 变量名 =赋值符'hello world'值
# a='hello world'
# print(a)
#
# # 值类型
# # 3 int  整数
# # str  字符串
# # float 小数
#
#
# l=[1,2,3,4,]
# l[0]=8 # 修改列表
# print(l)
#
# t=(1,2,3,4,5,2)
# # t[0]=9 # 修改元组，报错
# print(t)
#
# s={1,2,3,4,1,2,3,4}
# print(s)
# # print(s[0]) # 无序 ，所以不支持下标访问
#
# a=33
# b='66'
# print(a + int(b)) # 字符串转整数
# print(str(a) + b) # 整数转字符串
#
#
# a=33
# b='6.6'
# print(a + float(b)) # 字符串转整数
# print(str(a) + b)  # 整数转字符串
#
#
# a=True # 布尔类型也是数字  True 1 False 0
# b=99
# print(a + b)
#
# d = {'name':'小旋风','age':18,'name':'小明'}
# print(d)
# d = {'name':'小旋风','age':18}
# print(d['name'])

# l = [1,2,3,4,5,6,7,8]
# print(tuple(l))  # list to tuple
# print(set(l))  # list to set
#
# t = (1,2,3,4,5,6)
# print(list(t))  # tuple to list
# print(set(t))  # tuple to set
#
# s = {1,2,3,4,5,6,7,8,9}
# print(list(s)) # set to list
# print(tuple(s))  # set to tuple
#
# a='ahelog'
# l=['a','6','1']
# t=('a','6','1')
# s={'a','6','1'}
# d={'name':'打灰机','sex':'男'}
#
# print('h' in a)
# print('1' in l)
# print('6' in t)
# print('a' in s)
# print('name' in d)

# money = 10000
#
# if money >=100000:
#     print('打两炮')
#     print('打一炮送一炮')
# else:
#     print('白日做梦')
#
#
# a=100
# if a >= 101:
#     print(a)
# else:
#     print(99)


# money=10000
# if money < 100000:
#     print('拜拜了宁内')
#
# elif money < 1000000:
#     print('打一炮送一炮')
#
# elif money <10000000:
#     print('打一炮送两炮')
#
# elif money <100000000:
#     print('打一辈子炮')
#
#
# a=10
# if a <= 1:
#     print(a-1)
# elif a <= 10:
#     print(a+1)
# elif a <=20:
#     print(a-10)
# else:
#     print(a)


# for i in range(3):
#     print('what are you nong sha lei')
#
# for i in [1,2,3,4,5]:
#     print(i)
#     print('what are you nong sha lei')
#
# for i in [4,5,6,7,8,9]:
#     print(i)
#     print('emp')

# for i in [4,5,6,7,8,9]:
#     print(i)
#     print(i+1)


# print(list(range(66)))
# print(list(range(11,22)))
# print(list(range(11,22,2)))
# print(list(range(11,3,-2)))
# print(list(range(11,2,-3)))
# print(list(range(11,10,-3)))



# i=1
# while i<10:
#     print(i)
#     i += 1
#
# while True:
#     print('小赤佬')

#
# l =[1,2,3,4,3]
# l[0]=10
# print(l)

# t=(1,2,3,4,5,2)
# t[0]=10
# print(t)

# s = {1,2,3,4,1,2,3,4}
# print(s)

# a=10
# b="20"
# print(a + int(b))
# print(str(a) + b)

# a=10
# b="2.9"
# print(a + float(b)) # 字符串转小数
# print(str(a) + b)


# for i in range(1,21):
#     if(i in[4,8,12,18]):
#         continue
#     print(i)


# for i in range(1, 13):
#     if (i == 9):
#         break
#     print(i)


# 逢6过（1，100）
# for i in range(1,101):
#     if(i % 6==0 or i % 10==6):
#         print('过')
#     else:
#         print(i)

# 129
# a=129
# b=a//10
# print(b)
# print(b%10)


# a=129
# b=a//9
# print(b)
# print(b%12)


#
# def div(a,b):
#     if b == 0:
#         print("被除数不能为0")
#     else:
#         print(a/b)
#
# div(1,2)
# div(4,1)
# div(6,14)
#
#
# def div(c,d):
#     if d == 0:
#         print('被除数不能为0')
#     else:
#         print(c/d)
#
# div(20,30)
# div(50,10)
# div(80,200)
#
# def div(a,b):
#     if b == 0:
#         print("被除数不能为0")
#     else:
#         print(a/b)
#
# div(1,2)
# div(4,1)
# div(6,14)

# def beautiful(小红):
#     res = '123'
#     return res
# result = beautiful('')
# print(result)
#
#
# def beautiful(小黑):
#     res = 'black'
#     return res
# result = beautiful('')
# print(result)

# def pas():
#     for i in range(10):
#         print(i)
#     return
# pas()

# def crv(bba):
#     c = [1,2,3,4,5,6,7]
#     return c
#
# result = crv('')
# print(result)


# def x(a,b):
#     return a-b
# print(x(1,2))
#
# def x(a,b=5):
#     return a-b
# print(x(1,5))
#
# def x(a,b):
#     return a*b
# print(x(3,2))
#
# def x(b,a=4):
#     return a/b
# print(x(3,1))

# def c(a=2,b=3):
#     return a+b
# print(c(2,3))
#
# print(c(1,3))
#
# print(c(b=10))
#
# print(c(5,b=14))
#
# print(c(a=14,b=5))

# def qq(*args):
#     print(args)
# qq(1,2,3,4,5,6,7)
#
# def qq(*args,**dada):
#     print(args)
#     print(dada)
# qq(1,2,3,4,5,6,7,a=6,b=4,c=12,d=13)


# def qq(a,*args,b,**dada):
#     print(a)
#     print(b)
#     print(args)
#     print(dada)
#
# qq(1,2,3,4,5,6,7,b=4,c=12)

# def pl(a,b):
#     print(a)
#     print(b)
#     print('测试用例')
#
# def cc(fn,*args,**dada):
#     print('123',args,dada)
#     r = fn(*args,**dada)
#
#     print('',r)
# cc(pl,10,20)


# f=open('333.txt','w')
# f.write('八嘎雅鹿')
# f.close()
#
# f=open('333.txt','r')
# res=f.read()
# print(res)
# f.close()

# for i in range(1,10):
#     for k in range(1,i+1):
#         print(i,'x',k,'=',i*k,end='\t')
#     print()


# def qwe():
#     for i in range(1,10):
#         print(i)
# qwe()

# def we(a,b):
#     return a+b
# c=we(1,2)
# print(c)

# def dda(a,b):
#     print(a)
#     print(b)
#     print('完美')
#     return a,b
# v=dda(1,2)
# print(v)
#
# def dda1(a,b):
#     print(a)
#     print(b)
#     print('完美')
#     return a*b
# def dda2(a,b):
#     print(a)
#     print(b)
#     print('非常完美')
#     return (a+b)
# def yy(dda,*ol,**ool):
#     print('123',ol,ool)
#     g = dda(*ol,**ool)
#     print(g)
# yy(dda1,2,4)
# yy(dda2,6,8)

# c=11
# def zzz():
#     global c
#     c=22
#
# zzz()
# print(c)


# a = 1000
# print(id(a)) # 获取变量内存地址
#
# i = input("666")# 获取控制台输入
# print(i)
#
# print(type(a)) # 获取变量类型
# print(type("199"))
#
# print(isinstance("",int)) # 判断变量类型


# a='1234567890'
# b='6789'

# print(a+b)
# print(a*3)
# print(a[0])
# print(a[3:9]) #截取3-9
# print(a[:4])  #截取1-4
# print(a[5:])  #截取5-0
# print(a[-3:]) #截取最后三位
# print(a[2:-4]) #截取第二位到最后第四位

# print(a[3:-2])
# print(a[2:-1])


# a=' dasdadadas '
# print(a)
# a=a.strip()
# print(a.strip())
# print(a.lstrip())
# print(a.rstrip())
# line = '用户名,账户名，充值金额,预期结果'
# line =line.replace('，',',')
# print(line)
# print(line.split(','))

# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{} x {} = {}'.format(i,j,i*j),end = '\t')
#     print()
#
# for i in range(1,10):
#     for k in range(1,i+1):
#         print(i,'x',k,'=',i*k,end='\t')
#     print()


# l = [1,2,3,4,5,6,7,8]
# # for i in l:
# #     print(i)
#
# l[2]=20
# l.append(9)
# l.insert(3,30)
# l.extend([1,2,3,4,5])
# l.pop()
# l.pop(4)
# l.remove(2)
# l.index(6)
# l.sort()
# l.sort(reverse=True)
#
#
# print(l)



# 字典
# d={'name':'阿西吧','age':'99'}
#
# print(d['name'])
#
# d['name']='小白'
#
# d['sex']='女'
#
# d.pop('sex')
#
#
# d2={'sex':'女'}
#
# d.update(d2)
#
# print(dict(d,addr='上海浦东',phone='13612545698'))


# print(d)


# l=[10,1,35,61,89,36,55]
#
#
# for i in range(len(l)-1,0,-1):
#     for j in range(0,i):
#         if(l[j] > l[j+1]):
#             l[j],l[j+1] = l[j+1],l[j]
#
# print(l)


# class int_sky():
#
#     s = 6
#
#     def feel(self):
#         print(3)
#
#     def good(self):
#         print(4)
#
# xo = int_sky()
# xo.s = 'cool'
# xo.feel()
# xo.good()

# class string():
#     l = [1,2,3,4,5,6]
#     def viva(self):
#         for i in range(10):
#             print(i+2)
#     def ace(self):
#         print('团灭')
# cc = string()
# print(string.l)
# cc.viva()
# cc.ace()


# class str_demo():
#
#     def _init_(self):
#         print('魔法方法')
#
#     def replace(self):
#         print('实例方法')
#         pass
#
#     @classmethod
#     def split(cls):
#         print('类方法')
#
#     @staticmethod
#     def static():
#         print('静态方法')
#
#
# str_demo.split()
# str_demo().replace()
# str_demo.static()
# str_demo().static()

# class str_demo():
#     @classmethod
#     def ab_cd(cls):
#         cls.split()
#         cls.static()
#     @classmethod
#     def split(self):
#         print('ddad')
#
#     @staticmethod
#     def static():
#         print('ertg')
#
#     @staticmethod
#     def static_method():
#         __class__.split()
#         __class__.static()
#
#
# str_demo.ab_cd()
#
#
# class privatedemo():
#     a= None
#
#     def set_a(self,value):
#         self._a =value
#     def get_a(self):
#         return self._a
#
# p=privatedemo()
# p.set_a('hello')
# print(p.get_a())


# class Parent():
#
#     def __init__(self,a):
#         self.a = a
#
#     first_name = "王"
#     __second_name = "五"
#
#     @classmethod
#     def name(cls):
#         print("我叫" + cls.first_name + cls.__second_name)
#
#     def ji_neng(self):
#         print("锁匠")
#
#
# class Son(Parent):
#
#     def __init__(self,a,b):
#         super().__init__(a)
#         self.b = b
#
#     __second_name = "八"
#
#     @classmethod
#     def name(cls):
#         print("我叫" + cls.first_name + cls.__second_name)
#     pass
#
# son = Son()
# print(son.first_name)
# son.ji_neng()




import random

# 指定长度和内容的随机字符串
def str():
    cc=random.choices('1234567890',k=9)
    # print(cc)
    return (''.join(cc))
print(str())

def str(a,b):
    cc=random.choices(a,k=b)
    # print(cc)
    return (''.join(cc))
print(str('1234567890',10))

#随即手机号
def phone():
    l = ['152','189','150','139','138','159']
    random.choice(l)
    s = random.choice(l)
    # print(s)
    x = random.choices("0123456789",k=8)
    # print("".join(x))
    r = "".join(x)
    print(s+r)
phone()

def phone():
    l=['189']
    first = random.choice(l)
    s=random.choice(l)
    second=random.choices("0123456789",k=8)
    r="".join(second)
    print(s+r)
phone()

# 随机姓名
def xingming():
    w = '孙钱杨陈陶穆唐朱龙王黄白'
    s = random.choice(w)
    z = random.choices('里黑黄干去你啊吗的香蕉巴拉麻辣火锅算拉风',k=2)
    o = ''.join(z)
    print(s+o)
xingming()


# 随即id
def id():
    l='www','qqq','eee','rrr','ttt','yyy'
    random.choice(l)
    s=random.choice(l)
    # print(s)
    n = random.choices('里黑黄干去你啊吗的香蕉巴拉麻辣火锅算拉风', k=4)
    # print(''.join(n))
    o = ''.join(n)
    print(s+o)

id()


def xingming():
    w = '孙钱杨陈陶穆唐朱龙王黄白'
    zi = '里黑黄干去你啊吗的香蕉巴拉麻辣火锅算拉风'
    s = random.choice(w)
    zi_chang = random.randint(1,2)
    c = random.choices(zi,k=zi_chang)
    # print(''.join(z))
    o = ''.join(c)
    print(s+o)
xingming()