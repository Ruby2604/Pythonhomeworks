import os

FILE_NAME = "employees.txt"

def menu():
    while True:
        print("\n--- Employee Records Manager ---")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            with open(FILE_NAME, "a") as f:
                eid = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                pos = input("Enter Position: ")
                sal = input("Enter Salary: ")
                f.write(f"{eid}, {name}, {pos}, {sal}\n")
            print("Record added successfully.")

        elif choice == '2':
            if os.path.exists(FILE_NAME):
                with open(FILE_NAME, "r") as f:
                    print("\nID | Name | Position | Salary")
                    print("-" * 30)
                    print(f.read())
            else:
                print("No records found.")

        elif choice == '3':
            search_id = input("Enter ID to search: ")
            found = False
            if os.path.exists(FILE_NAME):
                with open(FILE_NAME, "r") as f:
                    for line in f:
                        if line.startswith(search_id + ","):
                            print("Record Found:", line.strip())
                            found = True
                            break
            if not found: print("Record not found.")

        elif choice == '4':
            search_id = input("Enter ID to update: ")
            records = []
            found = False
            if os.path.exists(FILE_NAME):
                with open(FILE_NAME, "r") as f:
                    records = f.readlines()
                with open(FILE_NAME, "w") as f:
                    for line in records:
                        if line.startswith(search_id + ","):
                            name = input("Enter New Name: ")
                            pos = input("Enter New Position: ")
                            sal = input("Enter New Salary: ")
                            f.write(f"{search_id}, {name}, {pos}, {sal}\n")
                            found = True
                        else:
                            f.write(line)
            print("Updated successfully." if found else "ID not found.")

        elif choice == '5':
            search_id = input("Enter ID to delete: ")
            if os.path.exists(FILE_NAME):
                with open(FILE_NAME, "r") as f:
                    records = f.readlines()
                with open(FILE_NAME, "w") as f:
                    for line in records:
                        if not line.startswith(search_id + ","):
                            f.write(line)
                print("Record deleted.")

        elif choice == '6':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()