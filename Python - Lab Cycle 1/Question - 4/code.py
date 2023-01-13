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
          "1.Print all Substrings\n",
          "2.Print Length n Substrings\n",
          "3.Print Length n Substrings with n Distinct Characters\n",
          "4.Print Length all Palindrome substrings\n",
          "5.Exit!")
    choice = int(input("Enter the Choice:"))

    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    else:
        break
