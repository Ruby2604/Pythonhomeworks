while True:
    password = input("Set a password: ")
    a = len(password)
    if a < 8:
        print("Password is too short.")
        continue

    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        continue
    
    print("Password is strong.")
    break