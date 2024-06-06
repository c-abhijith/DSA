def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                                                #time complexity = o(n^2)
                                                #space complexity =o(1)
arr=[7,4,5,1,2,0,9,6,3]
bubble_sort(arr)
print(arr)