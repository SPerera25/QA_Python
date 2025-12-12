person = {"Name": "John", "Age": 30, "City": "New York"}

person["Age"] = 31                 # Updates the value for key "Age"                31
person["Country"] = "USA"          # Adds a new key-value pair "Country": "USA"     USA

del person["City"]                 # Deletes the key-value pair with key "City"     New York
person.pop("Age")                  # Removes the key-value pair with key "Age"      31

person.clear()                     # Clears all key-value pairs in the dictionary   {}

person.update({"name": "Bob", "age": 25})        # Updates dictionary with new key-value pairs

print(person)                      # {'name': 'Bob', 'age': 25}