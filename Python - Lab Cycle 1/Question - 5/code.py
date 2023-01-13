def subs(string, n):
    i, j, list = 0, 0, []
    for i in range(0, n+1):
        for j in range(i+1, n+1):
            list.append(string[i:j])
    return list


def subs_length(string, l):
    i, j, list = 0, 0, []
    for i in range(0, len(string)+1):
        for j in range(i+1, len(string)+1):
            if len(string[i:j]) == l:
                list.append(string[i:j])
    return list


def subs_dist_length(string, l, n):
    i, j, list = 0, 0, []
    for i in range(0, len(string)+1):
        for j in range(i+1, len(string)+1):
            s1 = string[i:j]
            # To make the strings unique that is ton delete duplicate characters
            dist = set(s1)
            if (len(dist) == n):
                print(s1, end=",")


def palindrome_subs(string):
    i, j, list = 0, 0, []
    for i in range(0, len(string)+1):
        for j in range(i+1, len(string)+1):
            if string[i:j] == string[::-1]:
                list.append(string[i:j])
    return list


while True:
    print("\n\nMAIN MENU\n",
          "1.Print all possible substrings\n",
          "2.Print substrings of length L\n",
          "3.Print substrings of length L with N distinct letters\n",
          "4.Print Palindrome substrings\n",
          "5.Exit!")
    choice = int(input("\nEnter the Choice:"))
    string = input("Enter the String: ")

    if choice == 1:
        print("\nAll possible substrings are: ")
        list = subs(string, len(string))
        for i in list:
            print(i, end=" ")

    elif choice == 2:
        l = int(input("Enter the length of substring: "))
        print(f"\nSubstrings of length {n} are: ")
        list = subs_length(string, l)
        for i in list:
            print(i, end=" ")

    elif choice == 3:

        n = int(input("Enter the length of substring: "))
        print(f"\nSubstrings of length {n} are: ")
        list = subs_length(string, n)
        for i in list:
            print(i, end=" ")

    elif choice == 4:
        print("\nAll possible substrings are: ")
        list = palindrome_subs(string)
        for i in list:
            print(i, end=" ")

    else:
        break


# k=int(input("Enter the length of the substrings that you want to print:"))
# print("The possible substrings with length",k,"is:")
# subs_with_length(s,k)

# nof_dist=int(input("Enter the number of distinct characters in the substrings"))
# print("The substrings with",k,"length and",nof_dist,"distinct characters are:")
# subs_dist_char_and_length(s,k,nof_dist)


# print("All the palindrome substrings are:")
# print_palindrome_subs(s)
