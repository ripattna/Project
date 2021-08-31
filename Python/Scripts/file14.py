fp=open('empbin.dat','wb')
fp.write('vijayendra kulkarni')
a=100
b=233.55
fp.write(a)
fp.write(b)
fp.close()
fp=open('empbin.dat','rb')
print fp.read()
fp.close()

Traceback (most recent call last):
  File "file14.py", line 5, in <module>
    fp.write(a)
TypeError: must be string or buffer, not int
