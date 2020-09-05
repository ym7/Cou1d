# from timeit import Timer
# import time

# def outter(func):
#     def inner(*args, **kwargs):
#         start = time.time()
#         ret = func(*args, **kwargs)
#         end = time.time()
#         print('Use time:',end-start)
#         return ret
#     return inner


# def buble_sort(alist):
#
#     for i in range(len(alist)-1):
#         if alist[i]>alist[i+1]:
#             alist[i],alist[i+1]=alist[i+1],alist[i]
#             buble_sort(alist)
#
#     return alist

def buble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1-i):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
    return li



print(buble_sort([10,1, 2, 3, 5, 7, 8, 9]))