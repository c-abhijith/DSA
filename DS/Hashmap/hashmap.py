
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)
my_dict = dict(name="Alice", age=30, city="New York")
print(my_dict)

my_dict["gender"] = "Female"
print(my_dict)

print(my_dict.get("age"))


for key in my_dict:
    print(key, my_dict[key])


for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)
    
    
print(len(my_dict)) 

my_dict.clear()
print(my_dict)


