def subs(string, n):  # function for finding all possible substrings
    i, j, list = 0, 0, []
    for i in range(0, n+1):  # uses two nested loops to find all the possible substrings
        for j in range(i+1, n+1):
            # slices the strings to extract the substring and appends it to a list
            list.append(string[i:j])
    return list


def subs_length(string, l):  # function for finding substring with a specific length
    i, j, list = 0, 0, []
    for i in range(0, len(string)+1):  # uses two nested loops to find all the possible substrings
        for j in range(i+1, len(string)+1):
            # checks if the sliced substring has required length and appends into a list
            if len(string[i:j]) == l:
                list.append(string[i:j])
    return list


# function for finding substring with a specific length and has x distinct characters
def subs_dist_length(string, l, n):
    i, j, list = 0, 0, []
    for i in range(0, len(string)+1):
        # uses two nested loops to find all the possible substrings
        for j in range(i+1, len(string)+1):
            sub = string[i:j]
            if len(sub) == l:  # checks if the sliced substring has required length
                # uses set to get the no of distinct chars in the substring and checks it against the user input
                if len(set(sub)) == n:
                    list.append(sub)
    return list


# function for finding substring with max length and has x distinct characters
def subs_dist_max_length(string, n):
    i, j, list = 0, 0, []
    for i in range(0, len(string)+1):
        # uses two nested loops to find all the possible substrings
        for j in range(i+1, len(string)+1):
            temp = string[i:j]
            dist = set(temp)
            if len(dist) == n:  # uses set to get the no of distinct chars in the substring and checks it against the user input
                list.append(temp)

    # using max it uses len function as key inside the list and finds the longest substring, and takes the length of that
    long = len(max(list, key=len))
    for i in list:
        if len(i) == long:  # checks if the longest string length recieved against all the substrings inside the list and prints it
            print(i, end=" ")


def palindrome_subs(string):  # function for finding palindrome substrings
    i, j, list = 0, 0, []
    for i in range(0, len(string)+1):
        # uses two nested loops to find all the possible substrings
        for j in range(i+1, len(string)+1):
            sub = string[i:j]
            # checks if the substring recieved is same as the revese of the substring
            if sub == sub[::-1]:
                list.append(sub)  # appends to list if so
    return list

string = input("Enter the String: ")
while True:  # main menu loop
    print("\n\nMAIN MENU\n",
          "1.Print all possible substrings\n",
          "2.Print substrings of length L\n",
          "3.Print substrings of length L with N distinct letters\n",
          "4.Print substrings of max length with N distinct letters\n",
          "5.Print Palindrome substrings\n",
          "6.Exit!")

    choice = int(input("\nEnter the Choice:"))
    if choice in [1, 2, 3, 4, 5]:

        if len(string) > 2:  # check for the string entered(if length is less than 2, program ends, because there is no substring for 1 letter strings)
            if choice == 1:
                print("\nAll possible substrings are: ")
                list = subs(string, len(string))
                for i in list:
                    print(i, end=" ")

            elif choice == 2:
                l = int(input("Enter the length of substring: "))
                print(f"\nSubstrings of length {l} are: ")
                list = subs_length(string, l)
                for i in list:
                    print(i, end=" ")

            elif choice == 3:
                n = int(input("Enter the number of distinct letters: "))
                l = int(input("Enter the length of substring: "))
                print(
                    f"\nSubstrings of length {l} and {n} distinct letters are: ")
                list = subs_dist_length(string, l, n)
                for i in list:
                    print(i, end=" ")

            elif choice == 4:
                n = int(input("Enter the number of distinct letters: "))
                print(
                    f"\nSubstrings of max length and {n} distinct letters are: ")
                subs_dist_max_length(string, n)

            elif choice == 5:
                print("\nAll palindrome substrings are: ")
                list = palindrome_subs(string)
                for i in list:
                    print(i, end=" ")

        else:
            print("Error!, Please enter atleast 1 letter string!!")
            break
    else:
        print("Come Back Later!")
        break
