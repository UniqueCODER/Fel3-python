print("Age Classifier \n 6 tries for testing purposes")
count = 0
while 6 > count:
    count += 1
    arr = [input("Name:"), int(input("Age :"))]

    if arr[1] <= 11:
        print(arr[0], "is a Child")
    elif 12 <= arr[1] < 15:
        print(arr[0], "is a Pre-adolescent")
    elif 15 <= arr[1] <= 19:
        print(arr[0], "is an Adolescent")
    elif 19 < arr[1] <= 34:
        print(arr[0], "is an Adult")
    elif 34 < arr[1] <= 59:
        print(arr[0], "is an Middle Age")
    elif 59 < arr[1]:
        print(arr[0], "is an Elderly")

