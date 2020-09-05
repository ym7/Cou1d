def quick_sort(li,start,end):

    low = start
    high = end

    if low > high:
        return
    mid = li[low]
    while low < high:
        while low < high:
            if li[high] > mid:
                high-=1
            else:
                li[low] = li[high]
                break

        while low < high:
            if li[low] < mid:
                low+=1
            else:
                li[high] = li[low]
                break
        if low == high:
            li[low] =mid
            break
    quick_sort(li,start,high-1)
    quick_sort(li,high+1,end)
    return li
li = [6,1,5,8,2,0,4,9]
print(quick_sort(li=li,start=0,end=len(li)-1))