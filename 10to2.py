a = int(input("Enter your integer with the base 10: "))

binary = []
while a != 1 and a != 0:
    b = a % 2
    binary.append(str(b))
    a = int(a / 2)

if a == 1:
    binary.append(1)

correct_binary = binary[::-1]
print(correct_binary)