# sets are list of distinct or non duplicate values - values cannot be accessed by index
# s1 = set(1,'vijay,33.33)
# s1={22,44.44}
# list []  tuple ()   set {}

s1={1,2,3,4}
print len(s1)
print max(s1)
print sum(s1)
#print s1[0] error 
s1.add(5)
print s1
s1.remove(3)
print s1

# s1={1,2,4,5}
s2={4,5}
print s1.issubset(s2)
print s2.issubset(s1)
print s1.issuperset(s2)
print s1==s2
print s1!=s2

s1={1,2,3}
s2={3,4,5}
print s1 | s2
print s1 & s2
print s1 - s2
print s1.union(s2)  # 1,2,3,4,5
print s1.intersection(s2) # 3
print s1.difference(s2) # 12 

s3={2,33,33,2,55}
print s3  # removes duplicates 

