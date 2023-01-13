def employee_details():
    name = input("Enter the Employee Name: ")
    code = input("Enter the Employee Code: ")
    basic_pay = int(input("Enter the Basic Pay: "))
    list = [name, code, main(basic_pay)]
    return list


def main(basic_pay):
    if basic_pay < 10000:
        DA = 0.05
        HRA = 0.025
        MA = 500
        PT = 20
        PF = 0.08
        IT = 0

    elif basic_pay > 10000 and basic_pay < 30000:
        DA = 0.075
        HRA = 0.05
        MA = 2500
        PT = 60
        PF = 0.08
        IT = 0

    elif basic_pay > 30000 and basic_pay < 50000:
        DA = 0.11
        HRA = 0.075
        MA = 5000
        PT = 60
        PF = 0.11
        IT = 0.11

    else:
        DA = 0.25
        HRA = 0.11
        MA = 7000
        PT = 80
        PF = 0.12
        IT = 0.20

    return calc(basic_pay, DA, HRA, MA, PT, PF, IT)


def calc(basic_pay, DA, HRA, MA, PT, PF, IT):
    GS = basic_pay+basic_pay*DA+basic_pay*HRA+MA
    DED = PT+basic_pay*PF+basic_pay*IT
    return net_Salary(GS, DED)


def net_Salary(GS, DED):
    net = GS-DED
    return net


list = employee_details()
print("\nEmployee Name:", list[0], "\nEmployee Code: ",
      list[1], "\nNet Salary: ", list[2], "\n")
