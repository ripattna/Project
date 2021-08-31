sub1 = int(input("Enter marks of the first subject: "))
sub2 = int(input("Enter marks of the second subject: "))
sub3 = int(input("Enter marks of the third subject: "))
sub4 = int(input("Enter marks of the fourth subject: "))
sub5 = int(input("Enter marks of the fifth subject: "))
avg = int(sub1+sub2+sub3+sub4+sub4)/5
print('Your average is :', avg)
if avg >= 90:
    print("Grade: A")
elif 80 <= avg < 90:
    print("Grade: B")
elif 70 <= avg < 80:
    print("Grade: C")
elif avg >= 60 and 90 < 70:
    print("Grade: D")
else:
    print("Grade: F")