


number = float(input("Enter a number:"))
dev3 = number/3 == 0
dev5 = number/5 == 0
relate = dev3 and dev5
if relate:
    print(f"Yes, {number} is according to the criteria!")
else:
    print(f"No, {number} is not according to the criteria!")
