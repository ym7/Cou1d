# a = [1,3,-1,-3,5,3,6,7]
# print(max(a[2:5]))

#

# nums = [555,901,482,1771]
# li = []
# for i in nums:
#     num = str(i)
#     if len(num)%2==0:
#         li.append(num)
#
#
# print(len(li))

# S = 'aAAbbbb'
# J = 'aA'

#
# try:
#     for i in range(len(S)):
#         if J[i] == S[i]:
#             li.append(S[i])
#
# except Exception as e:
#     print(len(li))
#     pass

# for x in J:
#     print(x)
#     a = S.count(x)
#     li.append(a)
# print(sum(li))

# points = [[1,1],[3,4],[-1,0]]
# li = []
# for i in points:
#     if points[0][0] < points[1][0]:
#         se_point = points[0][1]+1
#         new_point = points[0][0]+1
#         print(se_point,new_point)
#
#
#
#
#
# for i in points:
#     print(i[0])

# se_point = points[0][1]+1
# new_point = points[0][0]+1
# print(se_point,new_point) # [2,2]


# i[0],i[1]


# a = [-10,-3,0,5,9,1,9]
# print(len(a))
# new = a[len(a)//2]
# print(3**10)

# print(2//2)

# a = [[-1]]
# li = []
# for i in a:
#     for p in i:
#         if p<0:
#             li.append(p)
# print(len(li))


# a = "LLLLRRRR"
# p = a.split('L')
# l = []
# for i in p:
#     if i != '':
#         l.append(i)
#
# print(len(l))

# a = "LLLLRRRR"
# for i in a.split('L'):


# for i in range(len(a)):
# s = "We are happy."
# s = s.replace(' ','%20')
# print(s)

# a = [[1,10,4,2],
#      [9,3,8,7],
#      [15,16,17,12]
#      ]


# a = 'LOVELY'
# print(a.lower())
# mosi = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# wrod = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#
# l = []
# for i in wrod:
#      l.append(i.lower())
#
#
# dic = dict(zip(l,mosi))
# print(dic)
# import asyncio
# import time
#
#
# async def fun1():
#     print('downloading.......')
#     await asyncio.sleep(3)
#     print('download ok')
#
# async def func2():
#     print('func2 wasdownloading....')
#     await asyncio.sleep(2)
#     print('fun2 ok')
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     tak1 = loop.create_task(fun1())
#     tak2 = loop.create_task(func2())
#     loop.run_until_complete(asyncio.wait([tak1,tak2]))
# a = "1,2,3"
# a = a.replace(',','')
#
# print(list(a))
# c = [(1,),(2,),(3,) ]
# c[1] = 5
# print(c)
# A = [1, 2, [3, 4, ["434", ...]]]
# B= [ ]
# for i in A:
#     if not isinstance(i,list):
#         B.append(i)
#     else:
#         for c in i:
#             if not isinstance(c,list):
#                 B.append(c)
#             else:
#                 for m in c:
#                     B.append(m)

# print(B)

# lst = [1,2,4,8,16,32,64,128,256,512,1024,32769,65536,4294967296]


# def kidsWithCandies(candies,extraCandies):
#     maxs = max(candies)
#     li = []
#     for i in candies:
#         li.append(i+extraCandies >= maxs)
#     return li
#
# print(kidsWithCandies(candies=[2,3,5,1,3],extraCandies=3))


# def lee(s,c):
#     for i in range(len(s)):
#         if s[i] == 'e':
#
#     return 0
#
# print(lee("loveleetcode",'e'))

# from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()
#
#
# class User(Base):
#     __tablename__ = 'user'
#     from sqlalchemy import String, Integer, Column
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(32), index=True)
#
#
# from sqlalchemy import create_engine
#
# engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/dbtest?charset=utf8")
#
# Base.metadata.create_all(engine)
# class U(object):
#     a= '1'
#     b= '2'
#     def __init__(self):
#         self.name = 'jack'
#         self.age = 18
#
# u= U()
# print(u.__dict__)


# def leet(num1,num2):
# #     li = []
# #     for i in num1:
# #         if i in num2:
# #             li.append(i)
# #     return li
# #
# # print(leet([4,9,5],[9,4,9,8,4]))

# def singleNumber(nums):
#     r = 0
#     for i in nums:
#         r ^= i
#
#     return r
#
#
# print(singleNumber([4,1,2,1,2]))

# import collections
# def countCharacters(words, chars):
#     ans = 0
#     cnt = collections.Counter(chars)
#     for i in words:
#         c = collections.Counter(i)
#         if all([c[i] <= cnt[i] for i in c]):
#             ans+=len(i)
#
#     return ans
#
#
# print(countCharacters(["cat","bt","hat","tree"], 'atach'))
# import collections
# def lee(arr):
#     li = collections.Counter(arr)
#     return len(list(dict.values(li))) == len(list(set(dict.values(li))))
#
#
# print(lee([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))

# target = 9

# from abc import abstractmethod,ABCMeta
# class Payment(metaclass=ABCMeta):
#     @abstractmethod
#     def pay(self,money):
#         raise TypeError
#
#
#
# class Ali(Payment):
#     def pay(self,money):
#         print('ali pay%d'%money)
#
# class Wechat(Payment):
#     def pay(self,money):
#         print('wechat %d'%money)
#
# class Apple(Payment):
#     def pay(self,money):
#         print('apple %d'%money)

# class Single(object):
#     def __new__(cls, *args, **kwargs):
#         print('newinit')
#         if not hasattr(cls,"_instance"):
#             cls._instance = super(Single, cls).__new__(cls)
#         return cls._instance
#     def __init__(self):
#         print('singleinit')
#
#
# a = Single()
# print(id(a))
# key = "AAA",'BB','C',"DD",'EEE'
# dic={"AAA":100,"ssss":2000}
# print('c' in dic.keys())
# mydict = {'a':1,'b':2}
# onekey = 'a'
# print(mydict[onekey])
# print(mydict.__getitem__(onekey))

# alist = [2,2,8,4,1,6,6]
# T=sorted(set(alist), key=alist.index)
# print(T)
# a=[3,4,1,2,5,6,6,5,4,3,3]
# a.sort()
# print(list(set(a)))
#
# with open('./a.txt', 'r')as f:
#     print(f.read())

# import socket
#
# client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# client.connect(('127.0.0.1',9090))
# cover = str(input(">say>>:"))
# s = cover.encode('utf-8')
# client.send(s)
#
# data = client.recv(1024)
#
#
#
# for j in range(1,len(paths)):
#     for i in range(len(paths)):
#         if paths[i][-1] == paths[j][0]


# from flask import Fkas
# a = '[KELAGIRLS克拉女神]2018-11-05 诺雅 明艳动人[25+1P/417M]'
# print(str(str(''.join(a.split(" ")[1:])).split("[")[0]))

# class Camera(object):
#     def __init__(self,camera):
#         self.camera = camera
#     def open(self):
#         print(self.camera,'启动')
#     def close(self):
#         print(self.camera,'关闭')
#
#
# class Backend():
#     def __init__(self):
#         self.start = self.start()
#         self.login_or_not = False
#
#     def user_info(self):
#         print('请登录')
#         username = str(input('用户名：'))
#         password = str(input('密码：'))
#         user_info = User(username,password)
#         user_info.create_user()
#
#     @login_requried
#     def start(self,*args):
#         self.user_info()
#         print('开始控制摄像头')
#         control_object = Camera(*args)
#         return control_object
#
#     def set_work_data(self,timing):
#         if self.login_or_not:
#             import time
#             print('设置摄像头工作为',timing,'小时')
#             print('摄像头将在','','关闭')
#             try:
#                 while time.time()==time.time()+timing:
#                     self.start().close()
#             except Exception as e:
#                 print(e)
#         print('你不是管理员，不能这是摄像头关闭时间')
#
#     def close_the_system(self):
#         self.start().close()
#
#
#     def _login_requried(func):
#         def inner(*args, **kwargs):
#             ret = func
#             return ret
#         return inner
#
# import json
# class User():
#     def __init__(self,username,password):
#         self.username = username
#         self.password = password
#
#     def create_user(self):
#         user_obj = {
#             '用户名':self.username,
#             '密码':self.password
#         }
#         with open('./normaluser.txt','w')as f:
#             f.write(json.dumps(user_obj))
#
#     def create_superuser(self):
#         user_obj = {
#             '用户名': self.username,
#             '密码': self.password
#         }
#         with open('./VIPuser.txt', 'w')as f:
#             f.write(json.dumps(user_obj))

#
#
# from socket import *
#
# conn  = socket(AF_INET,SOCK_STREAM)
# sock = conn.connect(('127.0.0.1',8082))
#
# while True:                             #新增通信循环,客户端可以不断发收消息
#     msg=input('>>: ').strip()
#     if len(msg) == 0:continue
#     sock.send(msg.encode('utf-8'))         #发消息,说话(只能发送字节类型)
#
#     feedback=sock.recv(1024)                           #收消息,听话
#     print(feedback.decode('utf-8'))
#
# sock.close()                                       #挂电话

# from socket import *
#
# server =  socket(AF_INET,SOCK_STREAM)
#
# server.bind(('localhost',9000))
#
# while True:
#     conn,addr = server.accept()
#     if addr == 0:break
#     print(addr)
#     conn.send()

# import asyncio
# import time
#
#
# async def m1():
#         print('m1 data1')
#         await asyncio.sleep(2)
#         print('m1 data2')
#
#
# async def m2():
#     print('m2 data1')
#     await asyncio.sleep(2)
#     print('m2 data2')
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait([m1(),m2()]))


# from collections import Counter
#
#
# data = [str(i)+'a' for i in range(10)]
#
#
# print(Counter(data))
# map = "g fmnc wms bgblr rpylqjyrc gr zw fylbdic."

# words = [chr(i) for i in range(97,123)]
# word1 = words[0::1]
# word2 = words[2::]
#
# word2.append('y')
# word2.append('z')
#
# print(word1)
# print(word2)
#
#
#
# for i in range(len(word1)):
#     map = map.replace(word1[i],word2[i])
#
#
# print(map)

# class Queue(object):
#     def __init__(self):
#         self.items = []
#     def enqueue(self,arg):
#         self.items.insert(0,arg)
#     def dequeue(self):
#         return self.items.pop()
#     def size(self):
#         return len(self.items)
#     def travel(self):
#         print(self.items)
#
# class Stack(object):
#     def __init__(self):
#         self.q1 = Queue()
#         self.q2 = Queue()
#
#     def push(self,item):
#         self.q1.enqueue(item)
#
#
#     def pop(self):
#         while 1:
#             if self.q1.size()==1:
#                 item = self.q1.dequeue()
#                 break
#             self.q2.enqueue(self.q1.dequeue())
#         self.q1,self.q2=self.q2,self.q1
#
#         return item
#
# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
#
# print(s.pop())
# print(s.pop())
# print(s.pop())

# def sta(source, target):
#     return source.join(' ')
#
#
# print(sta(source='source', target='target'))

# ad = []
# a = 1
# if type(a) == int:
#     print('ok')
from time import sleep


# async def func():
#     for i in [1,2,3]:
#         await asyncio.sleep(1)
#         print(i)
#
# async def func1():
#     for i in ['a','b','c']:
#         await asyncio.sleep(1)
#         print(i)
#
# if __name__ == '__main__':
#     import asyncio
#     task = asyncio.wait([func1(),func()])
#     asyncio.run(task)
# import copy
#
# a = 'a'
# print(id(a))
#
# b = copy.copy(a)
# c = copy.deepcopy(a)
# print(id(b))
# print(id(c))
# a  = 'b'
# print(id(b))
# print(id(c))
# import copy
#
# a=[1,2,3,[4,5],6]
#
# b = copy.deepcopy(a)
# b[-2].append(8)
#
# print(b)
# print(a)
# from functools import reduce
# print((reduce(lambda x,y:y+x,[1,2,3,4,5])))

# ar = (i for i in range(20))
#
# print(ar.__iter__())
# print(ar.__next__())
# print(ar.__next__())
# print(ar.__next__())

# def may(*args,**kwargs):
#     def inner(func,*args,**kwargs):
#         print(7)
#         ret = func
#         print(2)
#         return ret
#     return inner
#
#
# @may(44)
# def fun():
#     print('a')
#
# fun()
# import random
# a  = [i for i in range(10)]
# random.shuffle(a)
# print(a)

# class M():
#     def __call__(self, *args, **kwargs):
#         print('2')
#     def _name(self):
#         print('name')
#     def fu(self):
#         return self._name()
#     @staticmethod
#     def ma():
#         print('2')
#
#     @classmethod
#     def am(self):
#         print('ad')
#
# M.am()

# class Singto(object):
#     def __init__(self):
#         pass
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls,'_instance'):
#             Singto._instance = object.__new__(cls)
#         return Singto._instance
#     def fun(self):
#         print('nameit')
#
# s1 = Singto()
# s2 = Singto()
# s1.fun()
# s2.fun()
# print(id(s1))
# print(id(s2))


# class Method(object):
#
#     def __enter__(self):
#         print('ok start')
#         return self.do_it()
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         # del self
#         pass
#
#     def do_it(self):
#         print('jcak is ')
#
#     def __del__(self):
#         print('deling')
# with Method() as fp:
#     print(fp)

# import requests
# session = requests.session()
# session.get()