
def SelectSort(li):
    for j in range(0,len(li)-1):
        max_index = 0 #最大值下标默认为0
        for i in range(1,len(li)-j):
            if li[max_index] < li[i]:
                max_index = i
            li[len(li)-1-j],li[max_index] = li[max_index],li[len(li)-1-j]

    return li



print(SelectSort([5,2,7,3,8,1,9,4]))