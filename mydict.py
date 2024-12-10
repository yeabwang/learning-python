customer = {
    "name" : "Yeabsira",
    "age" : 23,
    "is_verified" : True
}

print(customer["name"]) # this method doesn't exist gracefully so inorder to exit gracefully we need to use .get() method
print(customer.get("Name")) # This just show us a null value, 

print(customer.get("birthday", 1990))#additionally we can supply null value to this method so that if the value doesn't exits it will show us that provided value


