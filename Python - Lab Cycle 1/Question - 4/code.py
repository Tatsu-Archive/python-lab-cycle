def check_happy(num): #function for checking is happy
    count = 0 #for checking how many times it looped
    while num != 1 and count < 100: #if number = 1, then its happy u dont have to run it again on loop
        temp, sum = num, 0 
        while temp > 0: #runs loop until temp reaches 0
            sum += (temp % 10)**2 #adds the squared reminder to sum
            temp = temp//10
        num = sum #gives the final sum to num
        count += 1 #increases the count for loop
    if num == 1 and count < 100: #condition for happy number
        return True  # Return true if it is a happy number
    else:
        return False  # Return false if the number is a sad number


def range_happy(start, end): #function for finding happy number within a range
    while start < end: #loop runs till the start value is lower than end
        if check_happy(start) is True: #checks is the start value is happy and print it if it is 
            print(start, end=" ")
        start += 1 #goes to the second number


def n_happy(end): #function for finding n happy numbers
    count = 0 #variable for keeping track of how many numbers printed
    while count < end: 
        if check_happy(count) is True: #checks is the value is happy and print it if it is 
            print(count, end=" ")
        count += 1 #goes to the second number


while True: #main menu runs forever until user exits
    print("\n\nMAIN MENU\n",
          "1.Check Happy\n",
          "2.Print happy within range\n",
          "3.Print N Happy Numbers\n",
          "4.Exit!")
    choice = int(input("Enter the Choice:"))

    if choice == 1: 
        num = int(input("Enter the number to check if Happy: ")) #variable for checking if happy num
        if check_happy(num) is True:
            print("\nHappy Number!")
        else:
            print("Sad Number!")
    elif choice == 2:
        start = int(input("Enter the Starting No: "))   #variable for starting value
        end = int(input("Enter the Stopping No: ")) #variable for ending value
        range_happy(start, end)
    elif choice == 3:
        end = int(input("Enter the Limit: ")) #variable for ending value
        n_happy(end)
    else:
        break #breaks out the while loop and exits the program