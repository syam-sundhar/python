import csv

with open("Book1.csv", "w", newline="") as file:
    write = csv.writer(file)

    write.writerow(['name', 'age', 'roll'])
    write.writerows([
        ['syam', 20, '25B11'],
        ['sundhar', 30, '25B11']
    ])