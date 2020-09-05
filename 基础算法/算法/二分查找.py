
def find(li, item):

    first_index = 0
    end_index = len(li) - 1

    while first_index <= end_index:
        mid_index = (first_index + end_index) // 2
        if li[mid_index]==item:
            return li.index(li[mid_index])
        elif li[mid_index]<item:
            first_index = mid_index+1
        else:
            end_index = mid_index -1

    return False


print(find(li=[1,2,3,4,5],item=2))