# def maxSlidingWindow(nums, k):
#         if not nums :
#             return []
#         result = []
#         i = 1
#         j = k + 1
#         max_ = max(nums[:k])
#         result.append(max_)
#         while j <= len(nums):
#             if max_ == nums[i-1]:
#                 max_ = max(nums[i:j])
#                 result.append(max_)
#             elif max_ < nums[j-1]:
#                 max_ = nums[j-1]
#                 result.append(max_)
#             else:
#                 result.append(max_)
#             i += 1
#             j += 1
#         return result
#
#
# re = maxSlidingWindow(nums=[1,3,-1,-3,5,3,6,7],k=3)
# print(re)

# def findNumbers(nums):
#     li = []
#     for i in nums:
#         if i % 2 == 0:
#             li.append(i)
#     print(nums,li)
#
#
#
# findNumbers([12,345,2,6,7896])

# def numJewelsInStones(J, S):
#     li = []
#     try:
#         for i in range(len(S)):
#             if J[i] == S[i]:
#                 li.append(S[i])
#     except Exception as e:
#         return len(li)
#
# print(numJewelsInStones('aA','aAAbbbb'))

# def smallerNumbersThanCurrent(nums):
# #     li = []
# #     out = []
# #
# #     for i in range(len(nums)):# 4次 0
# #         for j in range(i):
# #             if nums[j] > nums[i]:
# #                 li.append(nums[i])
# #     print(li)
# #     out.append(len(li))
# #     return out
# #
# # print(smallerNumbersThanCurrent([8,1,2,2,3]))


# def defangIPaddr(address):
#     address = address.replace('.','[.]')
#     return ('"'+address+'"')
#
# print(defangIPaddr("1.1.1.1"))

# points = [[1,1],[3,4],[-1,0]]
#
# for i in points:
#     # print(i[0])
#     print(points.index(i))

# [1, 1] -> [2, 2] -> [3, 3] -> [3, 4] -> [2, 3] -> [1, 2] -> [0, 1] -> [-1, 0]

# points = [[1,1],[3,4],[-1,0]]
#
# def minTimeToVisitAllPoints(points):
#     c = 0
#     for i in range(len(points) - 1):
#         c += max(abs(points[i + 1][0] - points[i][0]), abs(points[i + 1][1] - points[i][1]))
#     return c
#
#
#
# print(minTimeToVisitAllPoints(points))


# def funcleet(index,nums):
#     target = []
#     for i in range(len(nums)):
#         target.insert(index[i],nums[i])
#
#     return target
#
#
# print(funcleet(nums = [1,2,3,4,0],index = [0,1,2,3,0]))


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#     def kthToLast(self,head,k):
#         vals = []
#         temp = head
#         while temp:
#             vals.append(temp.val)
#             temp = temp.next
#         return vals[k]

# class TreeNode():
#     def __init__(self,x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#     def sortedArrayToBST(self,nums):
#         if not len(nums):
#             return
#         mid = len(nums) // 2
#         root = TreeNode(nums[mid])
#         root.left = self.sortedArrayToBST(nums[: mid])
#         root.right = self.sortedArrayToBST(nums[mid + 1:])
#         return root
#
#
# a = TreeNode()
# a.sortedArrayToBST([-10,-3,0,5,9])


# def funleet(n):
#     li = []
#     for i in range(1,int(n*'9')+1):
#         li.append(i)
#     return li
#
#
#
# print(funleet(1))


# class TreeNode():
#     def __init__(self,x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#     def sortedArrayToBST(self,root):
#         if not len(root):
#             return
#         for i in range(len(root)):
#             root = TreeNode(self.val[i])
#             root.left =self.val[i+1]
#             root.right = self.val[i+2]
#         return root


# def funcleet(coins):
#     res = []
#     for i in coins:
#         nu = (i+1)//2
#         res.append(nu)
#
#     return sum(res)
#
#
# print(funcleet([2,3,10]))


# def funcleet(grid):
#     li = []
#     for i in a:
#         for p in i:
#             if p < 0:
#                 li.append(p)
#     print(len(li))
#     return
#
#
# print(funcleet([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))


# def leet(s):
# #     count = 0
# #     count_L = 0
# #     count_R = 0
# #     for s_ in s:
# #         if s_ == 'L':
# #             count_L += 1
# #         else:
# #             count_R += 1
# #         if count_L == count_R:
# #             count += 1
# #     return count
# #
# #
# # print(leet("RLRRLLRLRL"))


# def leet(s):
#     rightMax = -1
#     for i in reversed(range(len(s))):
#         rightMax, s[i] = max(rightMax, s[i]), rightMax
#     return s
#
#
#
#
# print(leet([17,18,5,4,6,1]))


# class MyStack:
#
#     def __init__(self):
#         self.item = []
#
#     def push(self, x: int) -> None:
#         return self.item.append(x)
#
#     def pop(self) -> int:
#         return self.item.pop()
#
#     def top(self) -> int:
#         return self.item[0]
#
#     def empty(self) -> bool:
#         return self.item == []

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#     def mergeTrees(self,t1,t2):
#         root = None
#
#         t1.root + t2.root
#         t1.left + t2.left
#         t1.right + t2.right

# def leet(matrix):
#     # 所在行最小值
#     minlist = []
#     maxlist = []
#     for oneli in matrix:
#         minnum = min(oneli)
#         minlist.append(minnum)# 3,9,15
#
#
#     # 所在列中最大值
#     bigli = []
#     for i in range(0,len(matrix[0])):
#         lieli = []
#         for oneli in range(len(matrix)):
#             lieli.append(matrix[oneli][i])
#         bigli.append(lieli)
#         # print(bigli)
#
#     for la in bigli:
#         maxnum = max(la)
#         # print(maxnum)
#         maxlist.append(maxnum)
#
#     print(maxlist,minlist)
#     fa = list(set(maxlist).intersection(set(minlist)))[0]
#
#
#
#
#
#     return fa
#
#
# print(leet([[3,7,8],[9,11,13],[15,16,17]]))

# def maximum69Number (num):
# #     x = list(str(num))
# #     for i in range(len(x)):
# #         if x[i] == '6':
# #             x[i] = '9'
# #             break
# #     return int(''.join(x))
# #
# #
# # print(maximum69Number(9669))

#
# def uniqueMorseRepresentations(words):
#     dic = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
#      'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
#      's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
#     l = []
#     for word in words:
#         tem = ''
#         for i in word:
#             tem+=dic[i]
#         l.append(tem)
#
#     return len(set(l))
#
#
# print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))


# def sumZero(n):
#     li = []
#     for i in range(-5,5):
#         li.append(i)
#     print(li)
#
#     return
#
# print(sumZero(5))
# import socket
# import threading
# import subprocess
# # import socketserver
# # socketserver.TCPServer()
# def func():
#     for i in range(6):
#         print('656')
#         print('123')
#
#
#
# if __name__ == '__main__':
#     p = threading.Thread(target=func())
#     p.start()

# import os
# print(os.cpu_count())

# from multiprocessing import Process,Lock
# import os,time
# def work(lock):
#     lock.acquire()
#     print('%s is running' %os.getpid())
#     time.sleep(2)
#     print('%s is done' %os.getpid())
#     lock.release()
# if __name__ == '__main__':
#     lock=Lock()
#     for i in range(3):
#         p=Process(target=work,args=(lock,))
#         p.start()

# def leet(A):
#     new_li=[]
#     fi_li = []
#     for i in A:
#         new_li.append(list(reversed(i)))
#
#     for re in range(len(new_li)):
#         one_li = []
#         for one in new_li[re]:
#             if one == 1:
#                 one_li.append(0)
#             else:
#                 one_li.append(1)
#
#
#         fi_li.append(one_li)
#
#     return fi_li
#
#
# print(leet(A=[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

# def leet(s):
#
#     li = []
#     for i in range(10, 27):
#         p = str(i) + '#'
#         li.append(p)
#     word = 'abcdefjhi'
#     num  ='123456789'
#     words = 'jklmnopqrstuvwxyz'
#
#     first_dic = dict(zip(word,num))
#     second_dic = dict(zip(words,li))
#     if s[0:3:1].isdigit():
#         print('w')
#         chr()
#
#     return
#
# print(leet("10#11#12"))

# def leet(heights):
#     res = 0
#     new_=sorted(heights)
#     for i in range(len(new_)):
#         if heights[i]!=new_[i]:
#             res+=1
#     return res
#
# print(leet([1,1,4,2,1,3]))


# def leet(s):
#     li = []
#     for i in s:
#         if s.count(i)>1:
#             li.append(i)
#     if li:
#         return False
#     return True
#
# print(leet("letcod"))


# def eet(left,right):
#     li = []
#     li.insert(0,left)
#     for i in range(left,right):
#         for j in range(left,right):
#             if i%j
#
#
#     li.append(right)
#     return li
#
#
#
# print(eet(left=1,right=22))

# def func(s):
#     after = s.split(' ')
#     strs = ''
#     for i in after:
#         re_str = ''.join(reversed(i))
#         strs+=' '+re_str
#     strs = strs.replace('#',' ')
#     strs=strs.lstrip()
#     return strs
#
#
# print(func("Let's take LeetCode contest"))
#
# def func(a,b):
#     return max(a,b)
#
# print(func(1,2))

# def func(S):
#     i=0
#     j=len(S)
#     res = []
#     for s in S:
#         if s =='I':
#            res.append(i)
#            i+=1
#         else:
#             res.append(j)
#             j-=1
#     res.append(i)
#     return res

# print(func("IDID"))

# candies=[12,1,12]
# print([g for g in candies])
# from sqlalchemy.orm import sessionmaker
# from test import User
# from test import engine
# # user1 = User(name="jack")
# Session = sessionmaker(engine)
# db_session = Session()
# db_session.add(user1)
# db_session.commit()
# user_list = [
#     User(name='mick'),
#     User(name='justin')
# ]
# db_session.add_all(user_list)
# db_session.commit()
# db_session.close()

# for oneuser in db_session.query(User).all():
#     print(oneuser.name)

# db_session.query(User).filter(User.id == 1).update({"name":'poo'})
# db_session.commit()
# db_session.close()

# db_session.query(User).filter(User.id == 1).delete()
# db_session.commit()
# db_session.close()
# li = ["cat","bt","hat","tree"]

# import collections
# # arr = [-3,0,1,-3,1,1,1,-3,10,0]
# # li = collections.Counter(arr)
# # if len(list(dict.values(li))) == len(list(set(dict.values(li)))):
# #     print(True)
# # else:
# #     print(False)
# def isStraight(nums):
#         for i in range(len(nums)+1):
#             if nums[i]+1== nums[i+1] or nums[i] < nums[i+1] and nums[i] == nums[i+1]:
#                 return True
#             else:
#                 return False
#
# print(isStraight([0,0,2,2,5]))


# a=  10
# print("i am {age}".format(age=a))

# a = [ 'a,1','b,3,22','c,3,4',]
# b = ['a,2','b,1','d,2',]
# # 按每个字符串的第一个值，合并 a 和 b 到 c
# c = ['a,1,2','b,3,22,1','c,3,4','d,2']


# a =[1,2,3,4,5,6]
# print(a[0:-1:2])

# lst = [1,2,4,8,16,32,64,128,256,512,1024,32769,65536,4294967296]
# dic = {}
# for i in lst:
#     len_i = len(str(i))
#     dic.setdefault(len_i,[]).append(i)
# print(dic)
# lst=[[1,2,3],[4,5,6],[7,8,9]]
# new = []
# for i in lst:
#     for b in i:
#         new.append(b)
# print(new)

# a=[7,-8,5,4,0,-2,-5]
# # b = sorted(a,key=lambda x:abs(x),reverse=False)
# # print(b)
# for b in a:
#     c = lambda b:b<0
#     print(c)
# import copy

# a = [1,2,3,[4,5],6]
# b = a
# c = copy.copy(a)
# d = copy.deepcopy(a)
# b.append(10)
# c[3].append(11)
# d[3].append(12)
# print(a)
# print(b)
# print(c)
# print(d)

# [1, 2, 3, [4, 5, 11], 6, 10]
# [1, 2, 3, [4, 5, 11], 6, 10]
# [1, 2, 3, [4, 5, 11], 6]
# [1, 2, 3, [4, 5, 12], 6]
# d={"a":26,"g":20,"e":20,"c":24,"d":23,"f":21,"b":25}
# print(sorted(d.items(),key=lambda x:x[1]))

# a = [1,2,3,4,7,2,9]
# a.sort()
# print(a)
# list1=[1,2,3,5,8,7,11,10]
# list2=[5,15,25,10]
# same = [i for i in list1 if i in list2]
# diff=[i for i in list1+list2 if i not in same]
# print(same)
# print(diff)
# [5, 10]
# [1, 2, 3, 8, 7, 11, 15, 25]


# alist=[3,1,-4,-2]
# li = []
# for i in alist:
#     li.append(abs(i))
# li.sort()
# print(li)
#
# print(sorted([abs(i) for i in alist]))
# print()[pow(i,2) for i in range(1,11)]
# for i in range(5,0,-1)
#     print(i)
# k=1000
# count = 0
# while k>1:
#     print(k)
#     k = k/2
#     count+=1
# print(count)
# alist = [
#     {'name':'a','age':20},
#     {'name':'b','age':30},
#     {'name':'v','age':25}
#         ]
# # print(sorted(alist,key=lambda x:x['age'],reverse=True))
# #
# tupleA = ("a","b","c","d","e")
# tupleB = (1,2,3,4,5)
# print(dict(zip(tupleA,tupleB)))
# numbers = [1,2,3,4]
# numbers.append([5,6,7,8])
# print(numbers)
# print(len(numbers))
# for i in range(2):
#     print(i)
#
# for i in range(4,6):
#     print(i)

# tuplea= (1,2,3,4,5)
# lista = [1,2,3,4,5]
# dica = {'a':1,'b':2,'c':3}
# lista.append(6)
# lista.pop()
# dica['d']=4
# dica.clear()
# names1 = ["Amir","Barry","Chales","Dao"]
# # names2 = names1
# # names3 = names1[:]
# # names2[0] = "Alice"
# # names3[1] = "Bob"
# # sum = 0
# # for ls in (names1,names2,names3):
# #     if ls[0] == "Alice":
# #         sum+=1
# #     if ls[1]=="Bob":
# #         sum+=10
# #         print(sum)

# li = [1,2,3,4,5]
# # import random
# # random.shuffle(li)
# # print(li)

# a ='hello'
# print(a.find('p'))
# print(a.index('o'))

# a = 'aaabbcccd'
# a.count('a')
# a.count('b')
# a.count('c')
# g = sorted(list(set(a)))
# print(dict(zip(g,[a.count('a',a.count('b',a.count('c')))])))
# a='aaabbcccdddde'
# aa=''
# for i in sorted(list(set(a)),key=a.index):
#     aa=aa+i+str(a.count(i))
# print
# all_li = range(1,1001)
# li = []
# for i in all_li:
#     sec = 0
#     for j in range(1,i//2+1):
#         if i % j ==0:
#             sec+=j
#         else:
#             if i == sec:
#                 li.append(i)
#
# print(li)


# def addit(a):
#     try:
#         alist = list(a.replace(',', ''))
#         for i in range(0,len(alist)):
#             sum = alist[i]+alist[i+1]
#             print(sum)
#     except:
#         pass
#     return 0
#
# print(addit("1,2,3"))


#
# def lee(s):
#     n = len(s)
#     for i in range(1, n // 2 + 1):
#         if n % i == 0 and s[:i] * (n // i) == s:
#             return True
#     return False
#
# print(lee("a")
# v='0b1111011'
# print(eval(v))
# v = "011"
# print()

# def fo(n):
#     print(n)
#     n+=1
#     fo(n)
# print(fo(1))
# map(lambda x:x*x,range(10))
# print(list(map(lambda x:x*x,range(10))))

# from functools import reduce
# # 开始的时候将可迭代对象的第一个数和第二个数当成x和y
# # 然后将第一次函数的执行结果当成x，然后再传入一个数当成y
# # 再执行函数
# s=reduce(lambda x,y:x+y,range(101))
# print(s) # 相当于0+1+2+……+99+100


# print ('\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))

# def func1():
#     a=1
#     def inner():
#         return a
#     return inner
# print(func1()())

#
# list_a=[12,213,22,2,2,2,22,2,2,32]
# # ss=[x for x in filter(lambda x:x[0]%2==1,enumerate(list_a))]
# # print(ss)


# import time
# #
# #
# # def frequent(func):
# #     def foo(func,*args,**kwargs):
# #         start = time.time()
# #         func(*args,**kwargs)
# #         end = time.time()
# #         print(end-start)
# #         return
# #     return foo
# #
# #
# # @frequent
# # def add(x):
# #     return pow(int(x),3)
# #
# # print(add(5))


# Definition for a binary tree node.
# def destCity(paths):
#     if paths[0][1] == paths[1][0]:
#         return paths[1][1]
#
#
#     return 0
#
#
# print(destCity(paths = [["B","C"],["D","B"],["C","A"]]))
# from timeit import Timer
#
# def test1():
#     li = []
#     for i in range(100):
#         li.append(i)
#     return li
#
# def test2():
#     return (list(range(100)))
#
# def test():
#     return [i for i in range(100)]
#
#
# if __name__ == '__main__':
#     timer = Timer('test','from __main__ import test')
#     ti = timer.timeit(10000)
#     print(ti)


# class Stack(object):
#     def __init__(self):
#         self.items = []
#     def push(self,item):
#         self.items.append(item)
#     def pop(self):
#         return self.items.pop()
#     def see(self):
#         return self.items
# stack = Stack()
# stack.push([1,2,3,4,5,6,7])
# print(stack.see())
# '''
# 先进先出'''

# '''
# 先进后出
# '''
# class Queue():
#     def __init__(self):
#         self.items = []
#     def addFront(self,item):
#         self.items.insert(0,item)
#     def addBack(self,item):
#         self.items.append(item)
#     def removeFront(self):
#         return self.items.pop()
#     def removeBack(self):
#         return self.items.pop(0)
#     def size(self):
#         return len(self.items)
#     def see(self):
#         print(self.items)
#
# def lee(s):
#     ex  = True
#     q = Queue()
#     for i in s:
#         q.addFront(i)
#     while q.size() > 1 :
#         if q.removeFront() != q.removeBack():
#             ex = False
#             break
#
#     return ex
#
# print(lee('helleh'))

# def wrapper(func):
#     def inner(*args,**kwargs):
#         for i in range(5):
#             func(*args,**kwargs)
#         return func
#     return inner
#
# @wrapper
# def prit():
#     print('i am in')
# prit()

# print([i for i in range(1,101) if i%2==0 ])

# a = (i for i in range(10))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# print(list(map(str,[1,2,3,4,5,6,7,8,9])))
# a = [i for i in ['ss','as','ee']]
# for i in enumerate(a):
#     print(i)
#     print(type(i))
# ip = '127.0.0.1'
# ip= ip.split('.')
# b = []
#
# for i in ip:
#     b.append(bin(int(i))[2:].zfill(8))
# fi = int(''.join(b),2)
# print(fi)

# def ip2int(ip):
#     nums=ip.split('.')
#     # zfill()函数是补0
#     to_bin=[bin(int(i))[2:].zfill(8) for i in nums]
#     return int(''.join(to_bin),2)
# i=ip2int('127.0.0.1')
# print(i)
# a = 'bb'
# def func():
#     global a
#     a = 'nn'
#     print(a)
#
# func()
# print(a)

# def func(a,b=[]):
#     b.append(a)
#     print(b)
#
# func(1)
# func(1)
# func(1)
# func(1)

#
# def foo():
#     li = []
#     for i in range(4):
#         def fun(x):
#             return x*i
#         li.append(fun)
#     return li
#
# print([m(2) for m in foo()])

# collapse = False
# processFunc = collapse and (lambda s:" ".join(s.split())) or (lambda s:s)
# print( processFunc("i\tam\ntest\tobject !"))

# a = 2
#
# def func(s):
#     global a
#     a = s
#
#     print(a)
#
# func(6)
# print(a)
# a=[3,4,1,2,5,6,6,5,4,3,3]
#
# def fun(alist):
#     li = []
#     del_li = []
#     for i in alist:
#         if i not in li:
#             if i not in del_li:
#                 li.append(i)
#         else:
#             del_li.append(i)
#             li.remove(i)
#
#     return li
#
#
# print(fun(a))
# arr=[1,2,3]
# def bar():
#     arr = None
#     arr = arr+[5]
#
# bar()
# print(arr)
# def say_hi(func):
#     def wrapper(*args,**kwargs):
#         print("HI")
#         ret = func(*args,**kwargs)
#         print("BYE")
#         return ret
#     return wrapper
#
#
# def say_yo(func):
#     def wrapper(*args,**kwargs):
#         print("YO")
#         return func(*args,**kwargs)
#     return wrapper
#
# @say_hi
# @say_yo
# def func():
#     print("ROCK & ROLL")
#
#
# func()

# def user(s):
# #     def wrapper(*args,**kwargs):
# #         return s(*args,**kwargs)
# #     return wrapper
# #
# # @user
# # def a1():
# #     print('a1')
# #
# # @user
# # def a2():
# #     print('a2')


# print(a1.__name__)
# def func():
#     try:
#         raise ValueError("wrong whit i")
#     except ValueError as e:
#         print(e)
#     finally:
#         print('Done')

# func()
# for i in range(3):
#     print (i)
#
# alist = [0,1,2]
# for i in alist:
#     print(i+1)
# i = 1
# while i<3:
#     print (i)
#     i+=1
# for i in range(3):
#     print (i+1)

# k = 1
# def fun(s):
#     global k
#     k = s+1
# print(k)
# print(fun(2))
# print(k)

# my_dict = {"a":0,"b":1}
#
# def func(d):
#     d["a"]=1
#     return d
#
# func(my_dict)
# my_dict["c"]=2
# print( my_dict)

# import requests

# res = requests.get(url='hrt/0/96SFMAD-1OS-I-Oo128.mp3').content
# with open('明明就-周杰伦.mp3','wb')as f:
#     f.write(res)

# def calc(a,b,c,d=1,e=2):
# return (a+b)*(c-d)+e

# print (calc(1,2,3,4,5) )# 2
# print( calc(1,2,3)) # 8
# print (calc(1,2)) # Error,
# print (calc(1,2,3,e=4)) # 10
# print (calc(e=4, c=5, a=2,b=3)) #24
# print (calc(1,2,3, d=5,4)) #Error

# def (a,b=[]):

# def add_end(l=[]):
#     l.append("end")
#     return l
#
# add_end([1,2]) # 输出什么
# add_end() # 再次调用输出什么? 为什么

# def foo(*args,**kwargs):
#     print("args=",args)
#     print("kwargs=",kwargs)
#     print("-----------------")
#
# if __name__ =='__main__':
#     foo(1,2,3,4)
#     foo(a=1,b=2,c=3)
#     foo(1,2,3,4,a=1,b=2,c=3)
#     foo("a",1,None,a=1,b="2",c=3)

# def log(func):
#     def wrapper(*args,**kwargs):
#         ret = func()
#         return func
#     return wrapper
#
# @log
# def now():
#     print("2013-12-25")

# class <name>(<Type> arg1, <type> arg2, ...)
# # function <name>(arg1,arg2,...)
# def <name>(arg1, arg2,...)
# def <name>(<type> arg1, <type> arg2...)

# country_counter ={}
#
# def addone(country):
#     if country in country_counter:
#         country_counter[country ]+=1
#     else:
#         country_counter[country ]= 1
#
# addone("China")
# addone("Japan")
# addone("china")
# print(len(country_counter ))

# def doff(arg1, *args):
#     print(args)
#
#
# doff("applea", "bananas", "cherry")

# d = lambda p:p*2
# t = lambda p:p*3
#
# x = 2
# x = d(x)
# x = t(x)
# x = d(x)
#
# print(x)

# def multipliers():
#     return [lambda x:x*i for i in range(4)]
# print([m(2) for m in multipliers()])
# 有一个数据结构如下所示，请编写一个函数从该结构数据中返画由指定的
# 字段和对应的值组成的字典。如果指定字段不存在，则跳过该字段。
#
# data:{
# "time":"2016-08-05T13:13:05",
# "some_id":"ID1234",
# "grp1":{"fld1":1, "fld2":2,},
# "xxx2":{"fld3":0, "fld4":0.4,},
# "fld6":11,
# "fld7": 7,
# "fld46":8
# }
#
# fields:由"|"连接的以 fld 开头的字符串, 如 fld2|fld7|fld29
#
# def select(data,fields):
#     return result
# class Us():
#     def pro(self):
#         print('ok')
#     @property
#     def pros(self):
#         print('ok')
#         return
#
# a = Us()
# a.pros

# import re
# a = 'abccsdsc'
# fi = re.compile('ab*?c',re.S)
# res = re.findall(fi,a)
# print(res)
#
# import random
# import time
# s = time.time()
# print(random.randint(0,100))
# e = time.time()
# print(e-s)
#
# import os
# os.remove('./df.py')

# import json
#
# a = {'name':'信息','age':15}
# af = json.dumps(a,ensure_ascii=False)
# print(af)

# import os
# print(os.listdir('./'))
# for i in os.listdir('./'):
#     if os.path.isdir(i):
#         print(os.listdir(i))

# import os
#
# o1 = 'home'
# o2 = 'myblog'
#
# op = os.path.join('\\',o1,o2)
# print(op) #home\myblog

# str = '<div><h1>hello</h1></div>'
# import re
# reg = '<.*?>'
# fi = re.compile(reg)
# print(re.findall(fi,str))

# import re
# # def reg_email(email):
# #     reg=' ^\w+@[A-Za-z0-9].com'
# #     fi = re.findall(reg,email)
# #     if fi:
# #         print(fi)
# #     else:
# #         print('not regx')
# #
# # reg_email(email='github@163.com')

# import re
# a  ='v_v55'
# print(re.findall(r'^[a-zA-Z]+|_+\d+$',a))
# import time
#
# def whichday(now):
#     print(time.strftime("%Y-%m-%D %h-%M-%S"))
#
# whichday(now=None)

# class Animal():
#     def walk(self,message):
#         print('animal walk %s'%message)
#
# class Person(Animal):
#     def walk(self,message):
#         super(Person, self).walk(message)
#         print('man walk')
#         return
#
# p =Person()
# p.walk('awt')


# class A():
#     names = 'jack'
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def walk(self):
#         print('%s is %s'%(self.name,self.age))
#
# a = A(67)
# # a.walk()
# class Fo(object):
#     # def __new__(cls, *args, **kwargs):
#         # print(cls)
#     age = 18
#     def __init__(self):
#         print('ok')
#
# f =Fo()
# print(f.age)


# class Foo():
#     __age = 18
#     name  ='sd'
#     def func(self):
#         print(self.__age)
#
#
# f = Foo()
# f.func()
# print(f.name)

# class A():
#
#     def walk(self): #实例方法
#         print('walking ')
#
#     @staticmethod #静态方法
#     def sta():
#         print('static func')
#
#
#     @classmethod #类方法
#     def classfunc(self):
#         print('class method')
#
#
#     @property #静态属性
#     def pro(self):
#         return 'property func'
#
#
#     def __privatefunc(self):#私有方法,只有内部访问
#         print('私有方法')
#
#     def forprivatefunc(self):  #内部访问私有方法
#         return self.__privatefunc()
#
#
# a = A()


# class Ani(object):
#     def walk(self):
#         print('still walking')
#
# class Man(Ani):
#     def walk(self):
#         super(Man, self).walk()
#         print('man walking')
#
#
# m  =Man()
# m.walk()

# from collections import Iterable
# print(isinstance(set,Iterable))

# class A():
#     def __init__(self,name):
#         self.__name = name
#         self.age =18
#     def walk(self):
#         print(self.__name)
#
#
# a = A('jack')
# a.walk()
# print(a.age)
# class Single(object):
#     _instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = object.__new__(cls,*args,**kwargs)
#         return cls._instance
#     def __init__(self):
#         pass
#
# s1 = Single()
# s2 = Single()
# print(id(s1) == id(s2))

# from contextlib import contextmanager
# import os

# class W(object):
#     def __init__(self):
#         pass
#
#     def __enter__(self):
#         self.fun()
#         return self
#
#     def __exit__(self, *args, **kwargs):
#         print('退出with语句')
#
#     def fun(self):
#         print('funcis')
#
#
# with W() as w:
#     print('之前')
#     print(w)
#     print('之后')


# @contextmanager
# def func():
#     return 'os'
#
# with func as f :
#     print(f)

# class A():
#     def __init__(self):
#         pass
#     def __call__(self, *args, **kwargs):
#         print('is calling')
#
#
# a = A()
# a()
# print(callable(a))


# class Stack(object):
# #     def __init__(self):
# #         self.items = []
# #
# #     def push(self, item):
# #         self.items.append(item)
# #
# #     def pop(self):
# #         self.items.pop()
# #
# #     def see(self):
# #         print(self.items)


# s = Stack()
# s.push(0)
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
#
# s.see()
#
# s.pop()
# s.see()


# def test():
#     import uuid
#     names = {"name", "web", "python"}
#     ht = HashTable()
#     for key in names:
#         value = uuid.uuid4()
#         ht.add(key, value)
#         print("add 元素", key, value)
#     for key in names:
#         v = ht.get(key)
#         print("get 元素", key, v)
#
# class HashTable(object):
#     def __init__(self):
#         self.dic = {}
#     def add(self,key,value):
#         self.dic[key] = value
#     def get(self,key):
#         return self.dic[key]
#
# test()

# class Queue():
#     def __init__(self):
#         self.items = []
#
#     def enqueue(self, item):
#         self.items.insert(0, item)
#
#     def dequeue(self):
#         return self.items.pop()
#
#     def size(self):
#         return len(self.items)
#
#
# li = [1, 2, 3, 4, 5]
#
# '''因为两个队列，先实例化它们'''
# q1 = Queue()
# q2 = Queue()
#
# for i in li:
#     q1.enqueue(i)  # [5,4,3,2,1]-->insert(0，i)
#     '''先进先出'''
#     # print(q1.dequeue())-->[1,2,3,4,5]
#
# while q1.size() > 0:
#     while q1.size() > 1:
#         item = q1.dequeue()
#         q2.enqueue(item)  # [1,2,3,4,5]
#     print(q1.dequeue())  # [5,4,3,2,1]
#     q1, q2 = q2, q1


# class Node(object):
#     def __init__(self, value, next):
#         self.value = value
#         self.next = next
#
# class Link(object):
#     def reverse(self,pre):
#         if not pre or pre.next:
#             return pre
#         last = None
#         while pre:
#             temp = pre.next
#             pre.next = last
#             last = pre
#             pre = temp
#         return last

# class Context(object):
#     def __int__(self):
#         pass
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         pass
#
#     def do_something(self):
#         print('ok')
#
#
#
# with Context() as ctx:
#     ctx.do_something()

# class Parent(object):
#     x = 1
#
# class Child1(Parent):
#     pass
#
# class Child2(Parent):
#     pass
#
#
# print( Parent.x, Child1.x, Child2.x)
#
# Child1.x = 2
# print (Parent.x, Child1.x, Child2.x)
#
# Parent.x = 3
# print (Parent.x, Child1.x, Child2.x)


# class Singleton:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = object.__new__(cls, *args, **kwargs)
#         return cls._instance
#
#     def __init__(self):
#         pass
#
#
# s1 = Singleton()
# s2 = Singleton()

# class Queue(object):
#     def __init__(self,):
#         self.items = []
#
#     def enqueue(self, item):
#         self.items.insert(0, item)
#
#     def dequeue(self):
#         return self.items.pop()
#
#     def is_empty(self):
#         print(self.items == [])
#
#     def is_full(self):
#         print(len(self.items) > 0)
#     def see(self):
#         print(self.items)
#
# s = Queue()  # 初始化一个大小为2 的队列
# s.see()
# s.is_empty()  # 初始化后, 队列为空, 返回True
# s.enqueue(1)  # 将1 加入队列
# s.enqueue(2)  # 将2 加入队列
# s.is_full()  # 加入了两个元素, 队列已满, 返回True
# s.dequeue()  # 移除一个元素, 返回1
# s.dequeue()  # 移除一个元素, 返回2
# s.is_empty()  # 队列已经为空, 返回True

# from multiprocessing import Pool
# from multiprocessing import Process
# import time
#
# def task(n):
#     print("子进程开始: %s"%n, os.getpid())
#     time.sleep(1)
#     print("子进程结束: %s" % n, os.getpid())
#
# if __name__ == '__main__':
#     p = Pool(5)
#     for i in range(3):
#         p  =Process(target=task,args=(i,))
#         p.start()
#
# import time
# from concurrent.futures import ThreadPoolExecutor
#
#
# def func(n):
#     print(n)
#     time.sleep(1)
#     return n * 10
#
#
# t_lst = []
#
# # 定义一个线程池(默认 不要超过cup个数*5)
# tpool = ThreadPoolExecutor(max_workers=5)
#
# for i in range(20):
#
#     # 传值(开启20个子线程)
#     t = tpool.submit(func, i)
#     t_lst.append(t)
#
# # 相当于 close + join
# tpool.shutdown()
#
# print("主线程")
#
# for t in t_lst:
#     # t.result() 接受返回值
#     print("\033[31m ==== \033[0m", t.result())

#
# from multiprocessing import Process
# def readit(path):
#     with open(str(path),'r')as f:
#         print(f.read())
#
# if __name__ == '__main__':
#     path = './a.txt'
#     t1 = Process(target=readit,args=(path,))
#     t1.start()
#
#
# from concurrent.futures import ThreadPoolExecutor
# def readit(path):
#     with open(str(path),'r')as f:
#         print(f.read())
#
# if __name__ == '__main__':
#     t1 = ThreadPoolExecutor(max_workers=5)
#     t1.submit(readit,'./a.txt')
#     t1.shutdown()

# import socket
#
# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.bind(('127.0.0.1',9090))
#
# sock.listen(5)
# conn,addr = sock.accept()
#
# data = conn.recv(1024)
# print(data)

# from concurrent.futures import ThreadPoolExecutor
# from multiprocessing import Lock
# import time
#
# def func(n):
#     lock.acquire()
#     print(n,'is ok')
#     time.sleep(1)
#     print(n,'is over')
#     lock.release()
#
#
# if __name__ == '__main__':
#     lock = Lock()
#     pool = []
#     t1 = ThreadPoolExecutor(max_workers=5)
#     for i in range(5):
#         onethred=t1.submit(func,i)
#         pool.append(onethred)
#
#     t1.shutdown()

# from multiprocessing import Process
# import time
#
#
# def func(n):
#     print(n,'is ok')
#     time.sleep(1)
#     print(n,'is over')
#
# if __name__ == '__main__':
#     for i in range(3):
#         p1 = Process(target=func,args=(i,),daemon=False)
#         p1.start()
#     print('zhu')

# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if n is None:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
#
# c = consumer()
# produce(c)

# import asyncio
#
# async def hello():
#     print('working')
#     await asyncio.sleep(2)
#     print('over')
#
#
# if __name__ == '__main__':
#     h1 = hello()
#     h2 = hello()
#     h3 = hello()
#     loop = asyncio.get_event_loop()
#     tasks = [asyncio.ensure_future(h1),
#              asyncio.ensure_future(h2),
#              asyncio.ensure_future(h3)
#              ]
#     loop.run_until_complete(asyncio.wait(tasks))
# price[i]=price[j]+res

#
# def destCity(paths):
#     all = set()
#     begin = set()
#     for path in paths:
#         all.add(path[0]) #paths = [["B","C"],["D","B"],["C","A"]]
#         all.add(path[1]) # {'B', 'A', 'C', 'D'}
#         begin.add(path[0])
#
#
#     return (all-begin).pop()
#
#
# print(destCity(paths=[["B","C"],["D","B"],["C","A"]]))
#
# def canBeEqual(target,arr):
#     return sorted(target) == sorted(arr)
#
#
#
#
# print(canBeEqual(target=[809,107,274],arr=[809,274,107]))


# def maxProduct(nums):
#     if len(nums)>2:
#         li = sorted(nums)
#         p = [i-1 for i in li ]
#         num = p[-1]*p[-2]
#         return num
#     else:
#         return (nums[-1]-1)*(nums[0]-1)
#
#
# print(maxProduct([8,8,7,4,2,8,1,7,7]))

#
# def busyStudent(startTime, endTime, queryTime):
#     count = 0
#     for start, end in zip(startTime, endTime):
#         if start <=queryTime and end >= queryTime:
#             count+=1
#     return count
#
# print(busyStudent(startTime=[1,2,3], endTime=[3,2,7], queryTime=4))


# def shuffle(nums, n):
#     res = []
#     head = nums[:n]
#     rear = nums[n:]
#     for k,v in zip(head,rear):
#         res.append(k)
#         res.append(v)
#
#     return res
#
#
#
#
#
#
# print(shuffle([2,5,1,3,4,7], n=3))


# def runningSum(nums):
#     res = []
#     res.append(nums[0])
#     for i in range(1,len(nums)):
#         nums[i]+=nums[i-1]
#         res.append(nums[i])
#
#     return res


# print(runningSum([1,2,3,4]))
# class Node():
#     def __init__(self,item):
#         self.item = item
#         self.right = None
#         self.left = None
#
#
# class Tree(object):
#     def __init__(self):
#         self.root = None
#     def addNode(self,item):
#         node = Node(item)
#         if self.root == None:
#             self.root = node
#             return
#         cur = self.root
#         query = [cur]


# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

# class Node():
#     def __init__(self,data):
#         self.data =  data
#         self.next = None
#
# class Link():
#     def __init__(self):
#         self._head = None
#
#     def addNode(self,item):
#         node = Node(item)
#         node.next = self._head
#         self._head = node

'''爬虫'''
# import requests
# from lxml import etree
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# import pymysql
# import json
# import os
#
# class Spider():
#     def __init__(self):
#         self.items = []
#         self.url = 'http://www.itokoo.com/thread.php?fid=147&page=1'
#         self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
#         self.mongodbv()
#         self.path = os.path.join('./kela/')
#
#
#
#     def get_detial_url(self,pageNum=None):
#             response  = requests.get(url=self.url,headers=self.headers).text
#             tree = etree.HTML(response)
#             tbody = tree.xpath('//*[@id="threadlist"]/tr')
#             data = []
#             for i in tbody:
#                 detail_url = i.xpath("./td[2]/a/@href")
#                 for j in detail_url:
#                     data.append('http://www.itokoo.com/'+j+'\n')
#             with open('./url.txt','w')as f:
#                 f.write(json.dumps(data[11:]))
#             return data[11:]
#
#     def get_content(self,li,timeing):
#         # f = open('./data.txt', mode='a')
#         for i in li:
#             time.sleep(timeing)
#             response = requests.get(url=i,headers=self.headers)
#             response.encoding = "gbk"
#             tree = etree.HTML(response.text)
#
#             images_url = tree.xpath('//*[@id="td_att53416"]/img/@src')
#             images_url = images_url[0].rsplit('?')[0]
#             title = tree.xpath('//*[@id="subject_tpc"]/text()')[0]
#             title = str(str(''.join(title.split(" ")[1:])).split("[")[0])
#             download_url = tree.xpath('//*[@id="read_tpc"]/a[2]/@href')[0]
#             code_for_download = tree.xpath('//*[@id="read_tpc"]/text()')[1]
#
#             context = {
#                 '标题':title,
#                 '下载链接':download_url,
#                 '提取码':code_for_download
#                      }
#             finish_context =  json.dumps(context)+'\n'
#             # f.write(finish_context)
#
#             print('开始解析',title)
#             print('写入MongoDB中')
#             self.mongoInsert(context)
#             self.save_img(title,images_url)
#             break
#         # f.close()
#
#     def save_img(self,title,img):
#         # iamges = requests.get(url=img,headers=self.headers).content
#         # with open('./kela/'+title+'.jpg',mode='wb')as fp:
#         #     fp.write(iamges)
#         if not os.path.exists('./kela/'):
#             os.mkdir('./kela')
#         path  = self.path+title+'.jpg'
#         request.urlretrieve(url=img,filename=path)
#
#     def save_context(self):
#         f=open()
#
#         f.close()
#
#
#     def mongodbv(self):
#         pass
#
#     def mongoInsert(self,context=None):
#         pass
from urllib import request
# import time
# if __name__ == '__main__':
#     s = Spider()
#     the_url_list = s.get_detial_url()
#     print('url解析完毕。。准备开始获取内容')
#     time.sleep(3)
#     print('*'*10,'开始获取内容','*'*10)
#     s.get_content(the_url_list,timeing=0.2)
#     print('提交数据到MongoDB中。。。。。。。。。')
#     s.mongoInsert()
#     print('内容获取完毕，关闭数据库')

# def reverseString(s):
#     i, j = 0, len(s) - 1
#     while i < j:
#         s[i], s[j] = s[j], s[i]
#         i += 1
#         j -= 1
#
#
#
#
# print(reverseString(s=["H","a","n","n","a","h"]))

# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/index')
# def system():
#     return '1'
#
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
# res = (i for i in range(10))
# print(res.send(None))
# print(res.send())
# print(res.__next__())
# print(res.__next__())


# import time
# import datetime
# import random
# import os
# print(time.strftime("%Y-%m-%d %X")) #格式化的时间字符串:'2017-02-15 11:40:53'
# print(datetime.datetime.now())
# def make_code(n):
#     res=''
#     for i in range(n):
#         s1=chr(random.randint(65,90))
#         s2=str(random.randint(0,9))
#         res+=random.choice([s1,s2])
#     return res
#
# import sys
# import time
#
# def progress(percent,width=50):
#     if percent >= 1:
#         percent=1
#     show_str=('[%%-%ds]' %width) %(int(width*percent)*'#')
#     print('\r%s %d%%' %(show_str,int(100*percent)),file=sys.stdout,flush=True,end='')
#
#
# data_size=1025
# recv_size=0
# while recv_size < data_size:
#     time.sleep(0.1) #模拟数据的传输延迟
#     recv_size+=1024 #每次收1024
#
#     percent=recv_size/data_size #接收的比例
#     progress(percent,width=70) #进度条的宽度70


from abc import ABCMeta,abstractmethod


# class Action(metaclass=ABCMeta):
#     def __init__(self):
#         pass
#     @abstractmethod
#     def do(self):
#         print('doit')
#
#
#
# class Man(Action):
#     def do(self):
#         super(Man, self).do()
#     def walk(self):
#         print('walking')
#
# m = Man()
# m.walk()
# m.do()

# class User(object):
#     def login(self):
#         print('login html')
#
#     def register(self):
#         print('register html')
#
#     def save(self):
#         print('personal html')
#
#
# def moon():
#     print('noon')
#
#
# user = User()
#
# if hasattr(user,'loginw'):
#     getattr(user,'login')()
# else:
#     setattr(user,'moon',moon())


# from socket import *
#
# sock = socket(AF_INET,SOCK_STREAM)
# sock.bind(('127.0.0.1',8082))
# sock.listen(5)
# while 1:
#     conn,addddddr =sock.accept()
#     print(addddddr[0])
#
#     while 1:
#         msg = addddddr.recv(1024)
#         print(msg)
#         # mymsg = (input(':>>>'))
#
#         conn.send(msg.upper())
#     conn.close()
#
# sock.close()

# class Queue(object):
#     def __init__(self):
#         self.items = []
#
#     def enqueue(self,arg):
#         self.items.insert(0,arg)
#
#     def dequeue(self):
#         return self.items.pop()
#
#     def isEmpty(self):
#         return self.items == []
#
#     def size(self):
#         return len(self.items)
#
#     def travel(self):
#         print(self.items)
#
# q1 = Queue()
# q2 = Queue()
#
# for i in range(5):
#     q1.enqueue(i)
# q1.travel()
#
#
#
# while 1:
#     item = q1.dequeue()
#     q2.enqueue(item)
#
#     if q1.size() == 0:
#         print(q2.items)
#
#         break


# import queue
#
# class Stack():
#     def __init__(self):
#         self.q1 = queue.Queue()
#         self.q2 = queue.Queue()
#
#     def push(self,item):
#         self.q1.put(item)
#
#     def pop(self):
#         while 1:
#             if self.q1.qsize() == 1:
#                 break
#             self.q2.put(self.q1.get())
#         self.q1,self.q2 = self.q2,self.q1
#
#         return item
#
# o = Stack()
# o.push(1)
# o.push(2)
# o.push(3)
#
# print(o.pop())
# print(o.pop())
# print(o.pop())


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

# a = 1
# name = a
# print(id(a))
# print(id(name))
# del a
#
#
# def func():
#     print(name)
#
# print(id(a))
# print(id(name))
# func()
# import random
# a = [i for i in range(70,90,2)]
# random.shuffle(a)
# print(a)

# def trailingZeros(n):
#     # write your code here, try to do it without arithmetic operators.
#     res = 1
#     for i in range(1, n + 1):
#         res = res * i
#     li = list(reversed((str(res))))
#
#     return li
#
# print(trailingZeros(105))
#
# A=[1,2,3,4]
# B=[2,4,5,6]
# after = A+B
# def SelectSort(li):
#     for j in range(0,len(li)-1):
#         max_index = 0 #最大值下标默认为0
#         for i in range(1,len(li)-j):
#             if li[max_index] < li[i]:
#                 max_index = i
#             li[len(li)-1-j],li[max_index] = li[max_index],li[len(li)-1-j]
#
#     return li
#
#
# print(SelectSort(after))

# def mizz(n):
#     for i in (1,n):
#         if i % 3==0:
#             print('fizz')

# mizz(15)
# def fizzbuzz(n):
#     res = []
#     for i in range(1,n+1):
#         if i % 5 == 0 and i % 3 == 0:
#             res.append('fizz buzz')
#         elif i % 5 == 0:
#             res.append('buzz')
#         elif i % 3 == 0:
#             res.append('fizz')
#         else:
#             res.append(str(i))
#
#     return res
#
# print(fizzbuzz(n=15))
#
#
# def strStr(source, target):
#     if source == '':
#         return 0
#     res = []
#     for i in target:
#         for j in source:
#             if i == j:
#                 res.append(j)
#                 break
#     finish = ''.join(res)
#     if finish == target:
#         return 1
#     else:
#         return -1
#
#
#
#
# print(strStr(source='',target='target'))


# def flatten(nestedList):
#
#     for i in nestedList:
#         if isinstance(i,list):
#             new_li = i
#             flatten(new_li)
#         else:
#             stack.append(i)
#     return stack
#
# print(flatten([1,2,[1,2]]))

# li = [i for i in range(50,100,5)]
# import random
# random.shuffle(li)
# print(li)


li = [50,60, 90, 75, 65, 95, 85, 70, 55, 80]

#
# class SingleTon(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls,'_instance'):
#             SingleTon._instance = object.__new__(cls)
#         return SingleTon._instance
#
#
# a = SingleTon()
# o = SingleTon()
#
# print(a._instance)
# print(o)
#
# class Notsingle(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# c = Notsingle('ss',2)
# d = Notsingle('pp',5)
#
# print(c)
# print(d)

# def func(a,b=[]):
#     b.append(1)
#     print(a,b)
#
# func(2)
# import copy
# a = 2
# b = 3
# print(id(a))
#
# c = copy.deepcopy(a)
#
# # print(id(a))
# print(id(c))

# import json
# class CJsonEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, datetime.date):
#             return obj.strftime('%Y-%m-%d %H:%M:%S')
#         else:
#             return json.JSONEncoder.default(self, obj)
#
#
# import json
# import datetime
#
# a = datetime.datetime.now()
# print(json.dumps(str(a)))
#
# b = json.dumps(a, cls=CJsonEncoder)
# print(b)

# def ipTodec(ip):
#     dec_ips = ip.split('.')
#     bin_ips = ''
#     for el in dec_ips:
#         bin_el = bin(int(el))[2::]
#         bin_ips+=bin_el
#     return bin_ips
#
#
#
#
# ip = '192.16.1.1'
# print(ipTodec(ip))

# dic={"a":24,"g":52,"i":12,"k":33}
# print(sorted(
#     dic.items(),
#     key=lambda x:x[1]
# ))
#
# print(dic.items())
# import os
# print(os.listdir('./'))
# import os
# os.

# def fib(n):
#     a,b = 0,1
#     for _ in range(n):
#         a,b = b,a+b
#     return b
#
# print(fib(10))

# def isValid(s):
#     while '{}' in s or '()' in s or '[]' in s:
#         s = s.replace('{}',' ')
#         s = s.replace('()',' ')
#         s = s.replace('[]',' ')
#
#     return s == ''
#
# print(isValid(s="()"))

# class Node():
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
#
#
# class Link1():
#     def __init__(self):
#         self._head = None
#
#     def add(self,data):
#         node = Node(data)
#         node.next = self._head
#         self._head = node
#
# class Link2():
#     def __init__(self):
#         self._head = None
#
#     def add(self,data):
#         node = Node(data)
#         node.next = self._head
#         self._head = node
#     def megertwo(self,l1,l2):
#         l1 = Link1()
#         l2 = Link2()
#
#
# l1=Link1()
# l2=Link2()
#
# l1.add(1)
# l1.add(2)
# l1.add(4)
#
# l2.add(1)
# l2.add(3)
# l2.add(4)


# nums  = [1,1,2]
# print(len(set(nums)))
# a = 5
# print(8) if a >0 else print(1)

# def func(x:int,Alist:list):
#     print(x)
#
# func('s',Alist=[2,3,4])

# with open('./url.txt','r')as fp:
#     print(fp.xreadlines())

# sorted(dict,key=lambda x:x[1])


# name = 'kelisi'
# name2 = 'kelisi'
# print(id(name))
# print(id(name2))

# import gc
#
#
# class A():
#     def __del__(self):
#         print('被回收了')
#
# a = A()
#
# gc.collect()
# print('\n'.join(['\t'.join(['{}*{}={}'.format(x,y,x*y) for x in range(1,y+1)]) for y in range(1,10)]))

# 递归


# def f(i):
#     if i >= 1:
#         f(i - 1)
#         print(['%dx%d=%d' % (j, i, i * j) for j in range(1, i + 1)])
#
#
# if __name__ == '__main__':
#     f(9)

# a = 's dsds'
# print(a.index('2'))

# print([i % 2 for i in range(10)])
# gli = (i % 2 for i in range(10))
#
# def ma_gli(lis):
#     yield lis
#
#
#
# a = ma_gli(lis=gli)
# print(a.next())
# ma_gli(gli)
# ma_gli(gli)
# for i in gli:
#     print(i)
# def timing(func):
#     def inner(*args,**kwargs):
#         for i in range(10):
#             func(*args,**kwargs)
#         return func
#     return inner
#
# @timing
# def pr():
#     print('jakc')
#
# pr()

# def af(li):
#     for i in li:
#         yield i
#
# g = af(li)
# for i in g:
#     print(g)

# s = 'i\tam\ntest\tobject !'
# print(s)
# arr = [1,2,3]
# def bar():
# 	arr+=[5]
#
# 	bar()
# print(arr)
'''
A.  error
B.  [5]
C. [1,2,3]
D. [1,2,3,5]
'''
# 答案
# print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))  # <map object at 0x101f59748>


# def test():
#     try:
#         raise ValueError("something wrong")
#     except ValueError as e:
#         print("Error occurred")
#         print(e)
#         return
#     finally:
#         print("Done")
#
#
# test()
# def func1():
#     for i in range(3):
#         print(i)
#         a_list = [0, 1, 2]
#
#     for i in a_list:
#         print(i + 1)
#
# def func2():
#     i = 1
#
#     while i < 3:
#         print(i)
#
#         i += 1
#
# def func3():
#     for i in range(3):
#         print(i + 1)
# func1()

# k =1
#
# def f():
#     global k
#     k+=1
#     print(k)
#
# f()
# class A():
#     def walk(self):
#         print('man walk')
#
# class B(A):
#     def walk(self):
#         super(B, self).walk()
#         # print('i walk')
#
# b = B()
# b.walk()
# class Singlto(object):
#     def __init__(self):
#         pass
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls,'_instance'):
#             Singlto._instance = object.__new__(cls)
#         return Singlto._instance
#
#     def __call__(self, *args, **kwargs):
#         print('callit')
# import socket
#
#
# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.bind(('localhost',9000))
# sock.setblocking(False)
# sock.listen(5)
# while 1:
#     try:
#         conn,addr = sock.accept()
#         data = conn.recv(1024)
#         print(conn,addr)
#     except KeyboardInterrupt as e:
#         break
# s1 = 'mabcdabcdabcd'
#
#
# import re
#
# ar  =re.findall(pattern='abc(.*?)abc',string=s1)
# print(ar)
# print(re.match(pattern='abc',string=s1))


# import json
# from json import JSONEncoder
# from datetime import datetime
#
# class ComplexEncoder(JSONEncoder):
#     def default(self, o):
#         if isinstance(o,datetime):
#             return o.strftime('%Y-%m-%d %H:%M:%S')
#         else:
#             return super(ComplexEncoder, self).default(o)
#
# d = {'name':'jack','data':datetime.now()}
#
# print(json.dumps(d,cls=ComplexEncoder))
#
# import socketserver
#
# ar = '<html lang="en" >'
#
# import re
#
# print(re.findall(pattern="lang=\"(.*?)\" >",string=ar)[0])

#
# from flask import Flask,jsonify
#
#
# app = Flask(__name__)
# app.config['DEBUG']=True
#
# @app.route('/index/<id>')
# def homepage(id):
#     return str(id)
#
# if __name__ == '__main__':
#     app.run('localhost',9090)


from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
from multiprocessing.dummy import Pool,Process

# import threading
# a =threading.local()

# from threading import Lock
#
# lock = Lock()
#
# lock.acquire()

# import gevent
#
# def func1():
#     print(1)
#     gevent.sleep(2)
#     print(2)
#
#
# def fun2():
#     print(3)
#     gevent.sleep(1)
#     print(4)
#
# if __name__ == '__main__':
#     g1 = gevent.spawn(func1)
#     g2 = gevent.spawn(fun2)
#     g1.join()
#     g2.join()

# jc = []
# for i in range(10000000):
#     jc.append(i)
# print(jc)

# from turtle import Pen
# pen = Pen()
# for i in range(10):
#     pen.left(100)
#     pen.down(20)
#     pen.right(20)


# def sumtwo(numbers,target):
#     stack = []
#     for i in range(len(numbers)-1):
#         if numbers[i] + numbers[i+1] == target:
#             stack.append(numbers.index(numbers[i]))
#             stack.append(numbers.index(numbers[i+1]))
#
#     return stack
#
# print(sumtwo(numbers=[2,7,7,15],target=9))

# import win32con
# import win32com
# win32com.
# import uuid
# import hashlib
# import time
#
#
# def creat_uuid():
#     return str(uuid.uuid1())
#
#
# print(creat_uuid())
#
#
# def creat_md5():
#     m = hashlib.md5()
#     m.update(str(time.time()).encode())
#     return m.hexdigest()
#
#
# print(creat_md5())

# import queue
#
# class Stack():
#     def __int__(self):
#         self.q1 = queue.Queue()
#         self.q2 = queue.Queue()
#
#     def push(self,data):
#         self.q2.put(self.q1.get())
#
