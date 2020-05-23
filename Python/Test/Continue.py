# Skip the iteration if the variable i is 3, but continue with the next iteration:
'''i = 0
while i < 9:
   i += 1
   if i == 3:
      continue
   print(i)'''

for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print('Current Letter :', letter)

var = 10                    # Second Example
while var > 0:
   var = var -1
   if var == 4:
      continue
   print ('Current variable value :', var)
print("Good bye!")