import datetime
from datetime import date
print("enter your birth date: ")
date1=datetime.date(int(input()),int(input()),int(input()))
date2=date.today()
date3=(date2-date1)
print("Congratulations you have lived for "+str(date3.days)+" days")