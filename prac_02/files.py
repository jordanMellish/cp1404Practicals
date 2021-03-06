# Program 1
out_file = open('name.txt', 'w')
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

# Program 2
in_file = open('name.txt', 'r')
name = in_file.read().strip()
print('Your name is', name)
in_file.close()

# Program 3
in_file = open('numbers.txt', 'r')
num1 = int(in_file.readline())
num2 = int(in_file.readline())
print(num1 + num2)
in_file.close()

# Program 3 Extension
in_file = open('numbers.txt','r')
total = 0
for line in in_file:
    number = int(line)
    total += number
print('The total is :', total)
in_file.close()
