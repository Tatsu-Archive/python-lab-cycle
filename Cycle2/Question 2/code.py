# Function to rotate the list by k positions
def rotate_list(l, k):
    return l[-k:] + l[:-k]      # Returns the rotated list

# Function to remove duplicates from the list
def remove_duplicates(l):

    # Using set() to remove duplicates
    return list(set(l))

# Function to evaluate the function f(x) = x^2 - x
def evaluate_function(l):
    return [x**2 - x for x in l]    # Returns the evaluated list                                                                    

# Function to merge two lists   
def merge_lists(l1, l2):    

    # Using sorted() to sort the lists
    l1 = sorted(l1)
    l2 = sorted(l2)

    # Using extend() to merge the lists
    l1.extend(l2)
    return l1

# Main function 
def main():
    # Taking input from the user
    l = input("Enter the list of numbers: ").split()
    k = int(input("Enter the number of positions to rotate: "))

    # Converting the list to integers
    l = [int(x) for x in l]

    # Calling the functions
    l = rotate_list(l, k)
    t = tuple(l)
    l = remove_duplicates(l)
    l = evaluate_function(l)
    l = merge_lists(l, t)

    # Printing the final list
    print("The final list is: ", l)
    
# Calling the main function
main()                    
        