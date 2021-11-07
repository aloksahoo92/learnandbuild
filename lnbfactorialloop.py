'''
4. Calculate the Factorial of the number
● Take a minimum of 5 inputs from the user in the form of numbers
● Find the sum of all positive numbers entered by the user.
● As soon as the user enters a negative number, break the input process
● Then display the factorial of all positive numbers in the form of lists.
● File name must be in lnbfactorialloop.py in which you are writing code.
'''
numblist=[]
factnumblist=[]
sumnumb=0
def fact(n):
  if (n==1 or n==0):
    return 1
  else:  
    return (n * fact(n - 1))

for i in range(5):
  numb=int(input(f"Enter the number {i+1} :"))
  if numb>=0:
    sumnumb+=numb
    numblist.append(numb)
    factnumb=fact(numb)
    factnumblist.append(factnumb)
  else:
    break
    
print(f"The number are :{numblist}")
print(f"The Sum of all numbers are :{sumnumb}")
print(f"The factorial of all number are :{factnumblist}")

'''
Sample Output
Enter the number 1 :2
Enter the number 2 :3
Enter the number 3 :4
Enter the number 4 :2
Enter the number 5 :9
The number are :[2, 3, 4, 2, 9]
The Sum of all numbers are :20
The factorial of all number are :[2, 6, 24, 2, 362880]
'''


