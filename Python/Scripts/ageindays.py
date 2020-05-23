import datetime
by=int(input('birth yr'))
bm=int(input('birth month'))
bd=int(input('birth day'))
dob = datetime.date(by,bm,bd)
todaydate = datetime.date.today()
print todaydate - dob
