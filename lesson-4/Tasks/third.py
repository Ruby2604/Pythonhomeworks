#input:
#list1 = [1, 1, 2, 3, 4, 2]
#list2 = [1, 3, 4, 5]
#output: [2, 2, 5]


list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
a = [n for n in list1 if n not in list2]
b = [n for n in list2 if n not in list1]
print(a + b)