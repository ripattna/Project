def functioncall(x=0,y=0):
    " learn fun"
    print "inside function";
    print "The values passed to function are %d and %d" % (x,y);
    return (x+1,y+1);

print "Executing first line in Body";
(a,b)=functioncall();
print "The value of the Variables is %d and %d" % (a,b);
a=10;
(a,b)=functioncall(a);
print "The value of the Variables is %d and %d" % (a,b);
a=10; b= 20;
(a,b)=functioncall(a,b);
print "The value of the Variables is %d and %d" % (a,b);
(a,b)=functioncall(x=4)
print "The value of the Variables is %d and %d" % (a,b);
(a,b)=functioncall(y=5)
print "The value of the Variables is %d and %d" % (a,b);
(a,b)=functioncall(y=10,x=20)
print "The value of the Variables is %d and %d" % (a,b);
(a,b)=functioncall(10,y=20)
print "The value of the Variables is %d and %d" % (a,b);


#got multiple values for keyword argument 'x'
#print "The value of the Variables is %d and %d" % (a,b);
#(a,b)=functioncall(10,x=20)
#print "The value of the Variables is %d and %d" % (a,b);

#below error
#(a,b)=functioncall(x=10,40)
#print "The value of the Variables is %d and %d" % (a,b);
