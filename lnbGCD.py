'''
11. Greatest Common Divisor
● Take a user input in a list consisting of 2 or more than 2 numeric values.
● Find the GCD of the numbers of the list using a user defined function.
● File name must be lnbGCD.py in which you are writing code.

'''
numlist=[]
gcdno=0
def gcd(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            gcdno = i 
    return gcdno
listno=int(input("Enter the number of integer :"))
for i in range(listno):

  num1 =  int(input("Enter the number :"))
  numlist.append(num1)
for i in range(len(numlist)): 
  if i+1<len(numlist):
    gcdno=gcd(numlist[i], numlist[i+1])


print(f"The GCD of {numlist} is ", gcdno)

'''
Sample Output
Enter the number of integer :2
Enter the number :34
Enter the number :17
The GCD of [34, 17] is  17
'''
