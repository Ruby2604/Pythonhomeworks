##10. **Get Key-Value Pair**: Given a dictionary and a key, retrieve the key-value pair if the key exists.


sheet = {"name": "Ruby", 
         "surname": "Sobirjonova", 
         "age": 18}

if "age" in sheet:
    print("age:", sheet["age"])
else:
    print("the is not such a key.")