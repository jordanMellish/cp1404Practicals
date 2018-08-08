total_cost = 0

number = int(input("Number of items: "))
while number < 0:
    print("Invalid number of items!")
    number = int(input("Number of items:"))
for i in range(number):
    item_cost = float(input('Price of item: $'))
    total_cost += item_cost
if total_cost > 100:
    total_cost *= 0.9

print('Total price for {} items is ${:.2f}'.format(number, total_cost))
