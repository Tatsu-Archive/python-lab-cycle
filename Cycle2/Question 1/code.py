from tabulate import tabulate # module to print table

# function for finding the number of rabbit pairs
def count_rabbits(n):
    if n == 1 or n == 2:
        return 1
    else:
        return count_rabbits(n-1) + count_rabbits(n-2)


N = int(input("Enter the number of months: ")) # input for number of months
heading = ["Month", "Rabbit Pairs"]
data = []
for i in range(1, N+1): # loop to append the data to the list
    data.append([i, count_rabbits(i)])

print(tabulate(data, headers=heading, tablefmt="fancy_grid")) # prints the table

