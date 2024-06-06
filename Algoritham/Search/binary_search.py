def binary_search(arr,target):
    low=0
    high = len(arr)-1
    while low <= high:
        mid = (high+low)//2
        if arr[mid]==target:
            return True
        elif arr[mid]<target:
            low = mid
        else:
            high=mid
    return False                   #time complextiy = o(log n)
                                   #space complexity = o(1)
arr=[1,2,3,4,5,6,7,8,9]
target_value=8
if binary_search(arr,target_value):
    print("The value is fount in the array")
else:
    print("The value is not found in the array")