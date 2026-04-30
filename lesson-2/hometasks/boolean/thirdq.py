

#positive and even

a = float(input("Prompt number:"))
positive = a > 0
even = a/2 == 0
comb = positive and even
if comb:
    print(f"True, {a} relates.")
else:
    print(f"No, {a} doesn't match.")
    