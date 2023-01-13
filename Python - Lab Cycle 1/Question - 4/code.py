def check_happy(num):
    count = 0
    while num != 1 and count < 100:
        temp, sum = num, 0
        while temp > 0:
            sum += (temp % 10)**2
            temp = temp//10
        num = sum
        count += 1
    if num == 1 and count < 100:
        return True  # Return true if it is a happy number
    else:
        return False  # Return false if the number is a sad number


def range_happy(start, end):
    while start < end:
        if check_happy(start) is True:
            print(start, end=" ")
        start += 1


def n_happy(end):
    count = 0
    while count < end:
        if check_happy(count) is True:
            print(count, end=" ")
        count += 1


while True:
    print("\n\nMAIN MENU\n",
          "1.Check Happy\n",
          "2.Print happy within range\n",
          "3.Print N Happy Numbers\n",
          "4.Exit!")
    choice = int(input("Enter the Choice:"))

    if choice == 1:
        num = int(input("Enter the number to check if Happy: "))
        if check_happy(num) is True:
            print("\nHappy Number!")
        else:
            print("Sad Number!")
    elif choice == 2:
        start = int(input("Enter the Starting No: "))
        end = int(input("Enter the Stopping No: "))
        range_happy(start, end)
    elif choice == 3:
        end = int(input("Enter the Limit: "))
        n_happy(end)
    else:
        break