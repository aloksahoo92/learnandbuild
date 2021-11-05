'''2. Take User input and decode logic
● Take 2 integer input from user and print their products(their multiplication)
● IF product is greater than 500 then return their sum
● If the product is smaller than 500 then return "Hello LNB code is running
fine !!"
● file name must be lnbcal.py in which you are writing code
● commit this code on your github link under pythonbasic branch'''
num1=int(input("Enter the integer  1st :"))
num2=int(input("Enter the integer  2nd :"))
if num1*num2>500:
  print(f"The output is :{num1+num2}")
else:
  print("Hello LNB code is running fine !!")
'''
Sample Output
Enter the integer  1st :20
Enter the integer  2nd :3
Hello LNB code is running fine !!

Enter the integer  1st :20
Enter the integer  2nd :30
The output is :50
'''

