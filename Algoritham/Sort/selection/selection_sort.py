def selection_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                swap = arr[j]
                arr[j]=arr[i]
                arr[i]=swap    #time complexity =o(n^2)
                               #space complexity = o(1)
arr=[4,7,9,0,1,5,2,8,1,6]
selection_sort(arr)
print(arr)