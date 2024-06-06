
list_data=["apple",100,"elephant",39.9]

list_data.append("Hello")            #output :                      ['apple', 100, 'elephant', 39.9, 'Hello']
list_data.insert(2,1000)

list_data_copy=list_data.copy()     #output of the list_data_copy:  ['apple', 100, 'elephant', 39.9, 'Hello']
list_data_copy.extend(list_data)
count=list_data_copy.count("apple") 

index_value=list_data.index(100)
list_data.pop()



print(count)                        # Its means linke How many count are inthe list value apple  output : 2
print(index_value)                  #1
print("-----------")
print(len(list_data_copy))          #10
print(list_data_copy)               #['apple', 100, 'elephant', 39.9, 'Hello', 'apple', 100, 'elephant', 39.9, 'Hello']
print("list data = ",list_data)     #list data =  ['apple', 100, 1000, 'elephant', 39.9]

list_data.pop(1)
print(list_data)                    # ['apple', 1000, 'elephant', 39.9]

list_data.remove("apple")
print(list_data)                    #['apple', 1000, 'elephant', 39.9]

list_data.reverse()
print(list_data)                  #[39.9, 'elephant', 1000]


sort_value=[1,2,7,4,9,2,3]
sort_value.sort()
print(sort_value)                 #[1, 2, 2, 3, 4, 7, 9]


sort_value.sort(reverse=True)
print(sort_value)                 #[9, 7, 4, 3, 2, 2, 1]


'''
ouput of the method
-------------------


2
1
-----------
12
['apple', 100, 1000, 'elephant', 39.9, 'Hello', 'apple', 100, 1000, 'elephant', 39.9, 'Hello']
list data =  ['apple', 100, 1000, 'elephant', 39.9]
['apple', 1000, 'elephant', 39.9]
[1000, 'elephant', 39.9]
[39.9, 'elephant', 1000]
[1, 2, 2, 3, 4, 7, 9]
[9, 7, 4, 3, 2, 2, 1]

'''