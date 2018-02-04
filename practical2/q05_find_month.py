import calendar

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

month = int(input("Enter month: "))
year = int(input("Enter year: "))
is_leap_year(year)
if calendar.month_name[month] in ['September', 'April', 'June', 'November']:
    print (calendar.month_name[month] + " " + str(year) + " has 30 days")

elif calendar.month_name[month] in ['January', 'March', 'May', 'July', 'August','October','December']:
    print (calendar.month_name[month] + " " + str(year) + " has 31 days")        

elif calendar.month_name[month] == 'February' and is_leap_year(year) == True:
    print (calendar.month_name[month] + " " + str(year) + " has 29 days")

elif calendar.month_name[month] == 'February' and is_leap_year(year) == False:
    print (calendar.month_name[month] + " " + str(year) + " has 28 days")

else:
    print ("please enter valid date and month")
