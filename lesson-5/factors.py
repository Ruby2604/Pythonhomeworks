#Enter a positive integer: 12
#1 is a factor of 12
#2 is a factor of 12
#3 is a factor of 12
#4 is a factor of 12
#6 is a factor of 12
#12 is a factor of 12


number = int(input("Enter a positive number: "))

 
for num in range(1, number + 1):
    if number % num == 0:
        print(f"{num} is a factor of {number}")
            
