''' 
    This will create the information about the python array modules
'''

import array as arr

# create array
arr1 = arr.array("i",[1,2,3,4])
arr2 = arr.array("d",[1.2,2.3,3.4,4.5,5.5])
arr3 = arr.array('u',["a","b","c","d"])

#type
print(arr1.typecode)   # i
print(arr2.typecode)   # d 
print(arr3.typecode)   # u

#display datas
print(arr1)            # array('i', [1, 2, 3, 4])
print(arr2)            # array('d', [1.2, 2.3, 3.4, 4.5, 5.5])
print(arr3)            # array('u', 'abcd')

#length of arrays
print(len(arr1))       # 4
print(len(arr2))       # 5
print(len(arr3))       # 4

for i in range(len(arr1)-1):
    print(arr1[i])
    
arr1.append(500)      #output =  array('i', [1, 2, 3, 4, 500])
print(arr1)

