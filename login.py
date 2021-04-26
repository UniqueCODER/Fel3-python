
counter = 1
while True:
    username = input("Username:")
    password = input("Password:")

    if username == "USER123" and password == "PASS456":
        print("CORRECT USERNAME AND PASSWORD")
        True
        break
    else:
        print("WRONG INPUT")
        print("tries",counter)
        False
        counter += 1
