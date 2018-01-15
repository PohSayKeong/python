name = str(input("Enter name:"))
hours = float(input("Enter number of hours worked weekly:"))
pay = float(input("Enter hourly pay rate:"))
cpf = float(input("Enter CPF contribution rate(%):"))
gross = hours * pay
contrib = cpf/100 * gross
net = gross - contrib

print("Payroll statement for {0}".format(name))
print("Number of hours worked in week: {0}".format(int(hours)))
print("Hourly pay rate: ${0:.2f}".format(pay))
print("Gross pay = ${0:.2f}".format(gross))
print("CPF contribution at 20% = ${0:.2f}".format(contrib))
print("Net pay = ${0:.2f}".format(net))
