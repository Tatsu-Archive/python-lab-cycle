from tabulate import tabulate

def count_rabbits(n):
    if n == 1 or n == 2:
        return 1
    else:
        return count_rabbits(n-1) + count_rabbits(n-2)


N = int(input("Enter the number of months: "))
heading = ["Month", "Rabbit Pairs"]
data = []
for i in range(1, N+1):
    data.append([i, count_rabbits(i)])

print(tabulate(data, headers=heading, tablefmt="fancy_grid"))

