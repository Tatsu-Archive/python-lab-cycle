def sum_digits(num): #function to find the sum of the digits
    sum = 0
    while num != 0:
        sum += num % 10 #extracting the digits and adding them to sum
        num = num//10 #doing floor division to remove the extracted digit from variable

    return sum #returning the value


def reverse(num): #function to find the reverse of the number
    rev = 0
    while num != 0:
        rev = (rev*10)+num % 10 #reverse variable is multiplied by 10 to keep the places and the extracted digit is added
        num = num//10 #floor division to remove the extracted digit
    return rev #returning the value
 

def sum_places(num): #function to find the difference b/w the oddplace num and evenplace num
    prododd = 1
    prodeven = 1
    pos = 1 #variable for keeping track of the position
    while num != 0:
        if pos % 2 == 0: #if position is even, it gets mulitplied to even prod variable
            prodeven *= num % 10
        else:
            prododd *= num % 10 #if position is odd, it gets mulitplied to odd prod variable
        num = num//10
        pos += 1 #updating the position
    return prododd-prodeven #returning the subtracted value


num = int(input("Enter the number to find: ")) 
print(f"Sum of digits of {num}: {sum_digits(num)}")
print(f"Revese of {num}: {reverse(num)}")  #function call
print(f"Difference of nos at odd and nos at even: {sum_places(num)}")
