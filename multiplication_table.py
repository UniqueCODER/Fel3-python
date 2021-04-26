table = int(input("Display table number: "))

if 1 > table or table > 10:
    print("Please try again")
    table = int(input("Display table number: "))

for value in range(1, 11):
    print(table, 'x', value, '=', table * value)
