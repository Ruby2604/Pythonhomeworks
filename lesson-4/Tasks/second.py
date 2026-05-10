#input:
#list1 = [1, 2, 3]
#list2 = [4, 5, 6]
#output: [1, 2, 3, 4, 5, 6]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
a = [n for n in list1 if n not in list2]
b = [n for n in list2 if n not in list1]
print(a + b)


