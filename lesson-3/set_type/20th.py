set1 = {248, 398, 28, 374, 93, 93, 29}
set2 = {398, 93, 209, 32, 18}
set3 = set1.intersection(set2)
if set3 == {}:
    print("they do not have elements in common.")
else:
    print(f"{set3}")