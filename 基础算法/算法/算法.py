'''
二分查找算法
二分查找法实质上是不断地将有序数据集进行对半分割，并检查每个分区的中间元素
'''
li = [1,2,3,4,5,6,7,8,9]

def find(li,item):
    find = False
    mid_index = len(li) // 2
    first_index = 0
    end_index = len(li)-1

    while first_index <= end_index:
        mid_index = (first_index + end_index) // 2

        if li[mid_index] <= item:
            first_index = mid_index + 1
        elif li[mid_index] > item:
            end_index = mid_index - 1
        else:
            find = True
            break
    return find

'''
递归问题：汉诺塔问题
汉诺塔问题不管在任何编程语言里都是经典问题，是采用递归算法的经典案例，该问题可以抽象如下：
一:3根圆柱A，B，C，其中A上面串了n个圆盘
二:这些圆盘从上到下是按从小到大顺序排列的，大的圆盘任何时刻不得位于小的圆盘上面
三:每次移动一个圆盘，最终实现将所有圆盘移动到Ｃ上

'''


def hannota(n, fromit, throughit, toit):
    if n == 1:
        print(f'{fromit} --> {toit}')
    else:
        hannota(n - 1, fromit, toit, throughit)
        print(f'{fromit} --> {toit}')
        hannota(n - 1, throughit, fromit, toit)
hannota(3, 'A', 'B', 'C')

#7次


'''
排序算法
'''

'''
一：冒泡排序
方法：
比较相邻的元素。如果第一个比第二个大，就交换他们两个。
对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。
这步做完后，最后的元素会是最大的数。
针对所有的元素重复以上的步骤，除了最后一个。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
时间复杂度--》最好情况:O(n) 正常情况：O(n**2) 最差情况:O(n**2)
'''
def bubble_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]

# li = [1,5,8,9,4,6,3,2,7]
bubble_sort(li=[1, 5, 8, 9, 4, 6, 3, 2, 7])


'''
二：选择排序
方法：
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
重复第二步，直到所有元素均排序完毕。
'''

def SelectSort(li):
    for j in range(0,len(li) - 1):
        max_index = 0 #最大值下标默认为0
        for i in range(1,len(li)-j):
            if li[max_index] < li[i]:
                max_index = i
            li[len(li)-1],li[max_index] = li[max_index],li[len(li)-1]

    return li

'''
三：插入排序
方法：
将第一待排序序列第一个元素看做一个有序序列，
把第二个元素到最后一个元素当成是未排序序列。
从头到尾依次扫描未排序序列，
将扫描到的每个元素插入有序序列的适当位置。
（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
'''
def InsertSort(li):
    for i in range(1,len(li)):
        while i > 0:
            if li[i] < li[i-1]:
                li[i],li[i-1] = li[i-1],li[i]
                i -= 1
            else:
                break
    return li

'''
四：希尔排序
方法：
先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，
待整个序列中的记录"基本有序"时，再对全体记录进行依次直接插入排序。
gap：增量值或者拆分出来的组数
形状：逐渐变成有序序列
特性：是插入排序增量为gap的序列
'''
def ShellSort(li):
    gap = len(li)//2
    while gap >=1:
        for i in range(gap,len(li)):
            while i >0:
                if li[i] < li[i-gap]:
                    li[i],li[i-gap] = li[i-gap],li[i]
                    i-=gap
                else:
                    break
        gap //= 2
    return li


'''
五：快速排序
原理：将将比基准小的排列在基准左侧，比基准大的排列在基准右侧
方法：
1.将列表中第一个元素设定为基准数字，赋值给mid变量，
2.然后将整个列表中比基准小的数值放在基准的左侧，比基准到的数字放在基准右侧。
3.然后将基准数字左右两侧的序列在根据此方法进行排放。
4.定义两个指针，low指向最左侧，high指向最右侧
5.然后对最右侧指针进行向左移动，移动法则是，如果指针指向的数值比基准小，则将指针指向的数字移动到基准数字原始的位置，否则继续移动指针。
6.如果最右侧指针指向的数值移动到基准位置时，开始移动最左侧指针，将其向右移动，如果该指针指向的数值大于基准则将该数值移动到最右侧指针指向的位置，然后停止移动。
7.如果左右侧指针重复则，将基准放入左右指针重复的位置，则基准左侧为比其小的数值，右侧为比其大的数值。
'''
def sort(alist, start, end):
    low = start
    high = end
    # 递归结束的条件
    if low > high:
        return
    # 基准：最左侧的数值
    mid = alist[low]
    # low和high的关系只能是小于，当等于的时候就要填充mid了
    while low < high:
        while low < high:
            if alist[high] > mid:
                high -= 1
            else:
                alist[low] = alist[high]
                break
        while low < high:
            if alist[low] < mid:
                low += 1
            else:
                alist[high] = alist[low]
                break

        # 当low和high重复的时候，将mid填充
        if low == high:
            alist[low] = mid  # or alist[high] = mid
            break
    # 执行左侧序列
    sort(alist, start, high - 1)
    # 执行右侧序列
    sort(alist, low + 1, end)

    return alist


alist = [6,1,2,7,9,3,4,5,10,8]
print(sort(alist,0,len(alist)-1))


