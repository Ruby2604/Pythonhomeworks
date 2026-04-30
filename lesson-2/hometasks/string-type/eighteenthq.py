

gap = input("write:")
words = gap.split()
first = words[0]
second = words[-1]
if first == second:
    print("yes")
else:
    print("no")
