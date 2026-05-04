sheet = [2487, "love", "truth", 59, "saw"]
a = len(sheet)
b = a // 2
if a % 2 == 0:
    left = sheet[b - 1]
    right = sheet[b]
    print(left, right)
else:
    right = sheet[b]
    print(right)