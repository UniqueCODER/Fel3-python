counter = 1
while True:

    print("Generated number: ", int(counter))
    number_gen = int(input("Please enter number: "))

    if counter == number_gen:
        print("IT'S A MATCH")
        True
        break
    else:
        print("WRONG INPUT")
        False
        counter += 2
