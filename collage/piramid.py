rows = int(input('enter the number: '))

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("* " * i)
