#def invest(amount, rate, years):

#For example, calling _invest(100, .05, 4)_ should print the following:

#year 1: $105.00
#year 2: $110.25
#year 3: $115.76
#year 4: $121.55



def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f"year {year}: ${amount:.3f}")
amount = float(input("Enter the initial amount: "))
rate = float(input("Enter an annual percentage rate: "))
years = int(input("Enter the number of years: "))
invest(amount, rate, years)