#Password Checker**
#Task: Create a simple password checker.
#- Ask the user to enter a password. 
#- If the password is shorter than 8 characters, print "Password is too short." 
#- If the password doesn’t contain at least one uppercase letter, print "Password must contain an uppercase letter.". 
#- If the password meets both criteria, print "Password is strong."


password = input("Set a password: ")
a = len(password)

while True:
    if a < 8:
        print("Password is too short.")

        if not any(char.isupper() for char in password):
            print("Password must contain at least one uppercase letter.")
            continue

        if a <= 8 and any(char.isupper() for char in password):
            print("Password is strong.")
            break