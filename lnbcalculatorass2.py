'''
1. Create your own calculator
● Take input from the user max (3)
● Create a simple menu-driven calculator that can add, subtract, multiply
and divide numbers
● If the user enter input other than the above four menu then terminate the
program and display “Invalid Input...Try again”
● File name must be in lnbcalculatorass2.py in which you are writing code.
'''
result=0
num1=int(input("Enter the 1st number :"))
num2=int(input("Enter the 2nd number :"))
operation=int(input("Select operation for \nAdd ->1\nSub ->2\nMultiply ->3\nDivide-> 4:\n"))
if operation==1:
  print(f"Add :{num1+num2}")
elif operation==2:
  print(f"Sub :{num1-num2}")
elif operation==3:
  print(f"Multiply :{num1*num2}")
elif operation==4:
  if num2!=0:
    print(f"Divide :{num1/num2}")
  else:
    print("2nd number can't be 0")
else:
  print("Invalid Input...Try again")
  

'''
Sample Output
Enter the 1st number :35
Enter the 2nd number :3
Select operation for 
Add ->1
Sub ->2
Multiply ->3
Divide-> 4:
4
Divide :11.666666666666666
'''
