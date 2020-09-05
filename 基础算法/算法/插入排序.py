def insert_sort(li):
    for i in range(1,len(li)):
        while i > 0:
            if li[i] < li[i-1]:
                li[i],li[i-1] = li[i-1],li[i]
                i-=1
            else:
                break
    return li

print(insert_sort(li=[80, 82, 84, 70, 86, 78, 72, 88, 74, 76]))

