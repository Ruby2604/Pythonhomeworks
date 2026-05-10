##Return uncommon elements of lists. Order of elements does not matter.
#input:
#list1 = [1, 1, 2]
#list2 = [2, 3, 4]
#output: [1, 1, 3, 4]

list1 = [1, 1, 2]
list2 = [2, 3 ,4]
a = [i for i in list1 if i not in list2]
b = [i for i in list2 if i not in list1]
print(a + b)
