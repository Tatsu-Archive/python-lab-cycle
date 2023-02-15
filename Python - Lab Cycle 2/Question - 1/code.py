def rabbit_pair(n):
    current_month = 1
    adult_pair = 0
    child_pair = 1
    total_pair = 1

    while current_month < n:
        if current_month == 3:
            newadult_pair = child_pair
            newchild_pair = adult_pair + child_pair
            total_pair += adult_pair + child_pair

            adult_pair += newadult_pair
            child_pair += newchild_pair

            current_month += 1

        else:
            current_month += 1

    print('\nAdult Pair: ', adult_pair,
          '\nChild Pair: ', child_pair,
          '\nTotal Pair: ', total_pair)


n = int(input("Enter the number of months: "))
rabbit_pair(n)
