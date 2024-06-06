data={
    "name":"Abhijith c",
    "age"  : 21,
    "place":"kerala"
}

for key,value in data.items():
    print(key,"   ",value)
    
                            #name     Abhijith c
                            #age     21
                            #place     kerala
                            
print(data.get("name"))     #Abhijith c
print(data.items())         #dict_items([('name', 'Abhijith c'), ('age', 21), ('place', 'kerala')])
print(data.keys())          #dict_keys(['name', 'age', 'place'])
print(data.values())        #dict_values(['Abhijith c', 21, 'kerala'])



data.pop("name") 
print(data)                 #{'age': 21, 'place': 'kerala'}

data.update({"value":3000})
print(data)                #{'age': 21, 'place': 'kerala', 'value': 3000}


data.values()
print(data)                 #{'age': 21, 'place': 'kerala', 'value': 3000}

