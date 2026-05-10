while True:
    a = int(input('a = '))
    b = int(input('b = '))
    operation = input("Choose: (+, -, *, /)")
    if operation == "+":
        print("a + b =", a + b)
    elif operation == "-":
        print("a - b =", a - b)
    elif operation == "*":
        print("a * b =", a * b)
    elif operation == "/":
        print("a / b =", a / b)
    q = input("Do you want to run again?")
    if q in ["q", "quit", "no", "stop", "n"]:
        break
