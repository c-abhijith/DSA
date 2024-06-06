def linear_search(arr,value):
    for i in range(len(arr)):
        if arr[i]==search_value:
            return True
    return False
        
                                      #Time complexity o(n)
                                      #Space complexity o(1)
arr_data=[4,6,8,9,1,2,34,23,0]
search_value =1
if linear_search(arr_data,search_value):
    print("The search value is in the array")
else:
    print("The search value is not in the array")
