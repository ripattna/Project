class Person:
    ''' This is Person Class for learning '''
    def setname(self,name):
        ''' this is setname method of person class'''
        self.name = name;  #self.name is instance var 
    def dispname(self):
        print 'name=',self.name

p1 = Person()  
p1.setname('vijay')  # setname(p1,'vijay') 
p1.dispname()  # dispname(p1)

p1.name='anand'
print p1.name

print dir(Person)
print dir(p1)

help(Person)
help(p1)


#Person.name  # error as name is instance var not class var
#Person.dispname() # method dispname() must be called with Person instance


