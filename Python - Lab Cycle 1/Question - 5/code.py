# Function to print all the possible substrings
def all_subs(string, n):
    i, j = 0, 0
    for i in range(0, n+1):
        for j in range(i+1, n+1):
            print(string[i:j], end=" ")  # To print all the substrings


# Function to print all possible substrings of length n
def subs_with_length(s, n):
    i, j = 0, 0
    l = len(s)
    for i in range(0, l+1):
        for j in range(i+1, l+1):
            # To store the substring values to check if the length is equal to n
            s1 = s[i:j]
            if (len(s1) == n):
                print(s1, end=",")


# Function to print all possible substings of length n with c distinct characters
def subs_dist_char_and_length(s, n, c):
    i, j = 0, 0
    l = len(s)
    for i in range(0, l+1):
        for j in range(i+1, l+1):
            s1 = s[i:j]
            # To make the strings unique that is ton delete duplicate characters
            dist = set(s1)
            if (len(dist) == n):
                print(s1, end=",")


# Function to print all palindrome substrings
def print_palindrome_subs(s):
    i, j = 0, 0
    l = len(s)
    for i in range(0, l+1):
        for j in range(i+1, l+1):
            s1 = s[i:j]
            s2 = s1[::-1]  # To reverse the substring
            if (s2 == s1):
                print(s1, end=",")


while True:
    print("\n\nMAIN MENU\n",
          "1.Check Happy\n",
          "2.Print happy within range\n",
          "3.Print N Happy Numbers\n",
          "4.Exit!")
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


string = input("Enter the String:")
print("All possible substrings are:")
all_subs(string, len(string))

# k=int(input("Enter the length of the substrings that you want to print:"))
# print("The possible substrings with length",k,"is:")
# subs_with_length(s,k)

# nof_dist=int(input("Enter the number of distinct characters in the substrings"))
# print("The substrings with",k,"length and",nof_dist,"distinct characters are:")
# subs_dist_char_and_length(s,k,nof_dist)


# print("All the palindrome substrings are:")
# print_palindrome_subs(s)
