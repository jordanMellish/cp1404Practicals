from prac_06.guitars import Guitar

name = input("Name:")
year = int(input("Year:"))
cost = int(input("Cost: $"))
guitar = Guitar(name, year, cost)
print(guitar)
