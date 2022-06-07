def is_leap(year):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def month_no(month):
    months = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
  
    flag = 0
    for i in range(len(months)):
        if month == months[i]:
            month_no = i
            flag = 1
            break
    if flag==0:
        return -1
    else:
        return month_no


def  days_in_month(Year,Month_no):
    """ This function takes Year month no and returns the no of days."""
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    if year < 1 or Month_no < 1 :
        return -1

    if is_leap(Year) and Month_no == 1 :
        return 29
    else:
        return month_days[Month_no]

year = int (input("Enter a year: "))
month = (input("Enter a month's first 3 letters(like jan):")).lower()
month_num = month_no(month) 
days = days_in_month(year,month_num)
if days == -1:
    print("Invalid Year or Invalid month.")
else:
    print(days)

