

#greater than 50.8
#between 10 and 20 (inclusive)


a = float(input("Number one:"))
b = float(input("Number two:"))
c = a + b
if c > 50.8:
    print(f"Yes, {c} is greater.")
else:
    print(f"No, {c} is under 50.8")
    if 10 <= c <= 20:
        print(f"Yes, {c} is in the integral.")
    else:
        print(f"No, not eligible!")