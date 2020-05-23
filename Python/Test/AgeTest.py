import datetime
# from datetime import datetime
now=datetime.datetime.now()
print('Current time with Sec:', now)
by = int(input('Please enter Birth Year:'))
bm = int(input('Please enter Birth Month:'))
bd = int(input('Please enter Birth Date:'))
dob = datetime.date(by,bm,bd)
print('Your BOB:',dob)
today = datetime.date.today()
print("Today's Date:",today)
days_lv = today-dob
print('Your Days of living is:',days_lv)
days_in_year = 365.242199
# age=int((date.today() - dob).days / days_in_year)
age = int(days_lv.days/days_in_year)
daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
totalDays = round(days_lv.days%days_in_year)
sum = 0
months = 0
for (item, i) in enumerate(daysInMonth, start=1):
    if(sum + i > totalDays):
        months = item-1
        break
    sum = sum + i
# print('sum :: ', sum)
print('Your Age is:', age, ' Years', months, ' Months', int(totalDays-sum), ' days')
