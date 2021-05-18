#Create a dictionary named car.

# car = {
#     "brand": "Ford"
#     "model": "Mustang"
#     "year": 1964
# }

#print(model)

#For some get a Syntax error when I run the dict above. 


car = dict(brand="Ford", model="Mustang", year=1964)

model = car.get("model")

print(model)

# This way (above) works great for me

#Items, keys and values

items = car.items()
keys = car.keys()
values = car.values()

print(items, keys, values)







