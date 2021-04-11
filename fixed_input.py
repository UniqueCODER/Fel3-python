

print("Fixed log-ins up-to 3 tries")
counter = 1
while counter <= 3:
    username = input("Username:")
    password = input("Password:")

    if username.upper() == "ADMIN" and password.upper() == "AA123":
        print("CORRECT USERNAME AND PASSWORD")
        break

    else:
        print("WRONG INPUT")
        print(counter, "try out of 3")
        counter += 1
