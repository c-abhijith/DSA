def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j = i-1
        while j>=0 and key<=arr[j]:
            arr[j+1]=arr[j]
            j -=1
        arr[j+1]=key     #time complexity = o(n^2)
                         #space complexity = o(1)
arr=[5,7,1,3,0,2]
insertion_sort(arr)
print(arr)