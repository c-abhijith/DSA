def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    merged=[]
    i=j=0
    while i < len(left) and j<len(right):
        if left[i]<right[j]:
            merged.append(left[i])
            i +=1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged





arr = [7,2,4,1,9,5,6,3,8]
print(merge_sort(arr))