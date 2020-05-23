# define Python user-defined exceptions

class InsufBal(Exception):
   """Raised when the input value is too small"""
   def __init__(self,msg,amt):
      Exception.__init__(self)
      self.msg=msg
      self.amt=amt

# our main program
# user guesses a number until he/she gets it right

# you need to guess this number

balance=15000

while True:
   try:
       amt= int(input("Enter amt to withdraw: "))
       if balance - amt < 10000:
           #raise InsufBal -msg & amt must have default values ;otherwise error
           raise InsufBal('insuficient balance',amt)
       break
   except InsufBal as e:
      print e.msg
      print e.amt
 

print("Congratulations! withdraw completed.")

