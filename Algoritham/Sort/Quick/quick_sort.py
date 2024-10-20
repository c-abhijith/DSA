def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivote = arr[len(arr)//2]
    left = [i for i in arr if i < pivote]
    middle = [i for i in arr if i == pivote]
    right = [i for i in arr if i > pivote]

    return quick_sort(left) + middle + quick_sort(right)


arr=[5,7,1,2,9,0,8,6]
print(quick_sort(arr))