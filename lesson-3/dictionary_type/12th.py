##12. **Count Value Occurrences**: Given a dictionary, count how many times a specific value appears across the keys.


sheet = {"name": "Ruby", 
         "surname": "Sobirjonova", 
         "age": 18}

a = list(sheet.values())
b = a.count(sheet["age"])
print(b)