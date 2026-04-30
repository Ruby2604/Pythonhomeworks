

words = input("List some words here:")
sep1 = words.split()
sep = input("How to separate them:")
result = sep.join(sep1)
print(f"Here is the result: {result}")
