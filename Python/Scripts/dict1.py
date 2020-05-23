# dictionary is key : value pairs - mutable - unordered -
# value need to be accessed by  key
# key acts as index
# key has to be numeric or str -- value can be any Data type

d1={'vijay':33000,'anand':445555,'manju':737733, 'sandhya':83838, 'ravi':36363}


print d1['manju']

for i in d1:
    print i, d1[i]
    print

print len(d1)

print d1

print d1.keys()
print d1.values()


print 'manju' in d1

d1.pop('sandhya')
print d1
d1.clear()

print d1

        
