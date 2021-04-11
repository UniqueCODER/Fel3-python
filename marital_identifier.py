print("Marital status Identifier")

info = [input("Enter Name :"), input("Enter Gender :"),
        input("Marital Status\n [A] Single\n [B] Married \n Choice:")]
greeting = "Good Day!"
if info[1].upper() == "M" and (info[2].upper() == "A" or info[2].upper() == "B"):
    print(greeting, ' Mr.', info[0])
elif info[1].upper() == "F" and info[2].upper() == "A":
    print(greeting, " Ms.", info[0])
elif info[1].upper() == "F" and info[2].upper() == "B":
    print(greeting, " Mrs.", info[0])
