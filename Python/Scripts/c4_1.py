class Person:
    n =0
    def __init__(self, name, age):
        print 'initialising '
        self.__name=name
        self.__age=age
        Person.n+=1
    def __del__(self):
        print 'releasing '
        Person.n-=1
    def setname(self,name):
        self.__name = name;
    def dispname(self):
        print 'name=',self.__name
    @staticmethod 
    def numemps():
        return Person.n
  


        
p1=Person('ravi',22)

p1.dispname()

p2=Person('san',21)

p2.dispname()

x = Person.numemps()
print x


          
