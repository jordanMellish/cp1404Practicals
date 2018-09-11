from prac_06.guitar import Guitar

guitar = Guitar("Gibson L-5", 1922, 16035.30)
another = Guitar("Another", 2010, 16035.30)

print("{} get_age() - Expected 96. Got {}".format(guitar.name, guitar.get_age()))
print("{} get_age() - Expected 8. Got {}".format(another.name, another.get_age()))
print("{} is_vintage() - Expected True. Got {}".format(guitar.name, guitar.is_vintage()))
print("{} is_vintage() - Expected False. Got {}".format(another.name, another.is_vintage()))
