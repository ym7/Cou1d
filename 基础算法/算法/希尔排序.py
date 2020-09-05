def hell_sort(li):
    gap = len(li)//2
    while gap >=1:
        for i in range(gap,len(li)):
            while i>0:
                if li[i] < li[i-gap]:
                    li[i],li[i-gap] = li[i-gap],li[i]
                    i-=gap
                else:break
        gap//=2
    return li


print(hell_sort(li=[80, 82, 84, 70, 86, 78, 72, 88, 74, 76]))
