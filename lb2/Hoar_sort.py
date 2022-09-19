import random

def hoar_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        q = random.choice(arr)
        left = []
        middle = []
        right = []
        for elem in arr:
            if elem < q:
                left.append(elem) 
            elif elem > q: 
                right.append(elem) 
            else: 
                middle.append(elem)
        print(middle)
        return hoar_sort(left) + middle + hoar_sort(right)


print(hoar_sort([5,1,4,3,2,2]))