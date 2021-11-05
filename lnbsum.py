'''1. Take User input and process
● Take 5 integer input from the user.
● Remove all numbers less than 9.
● Calculate the sum of remaining numbers
● File name must be lnbsum.py in which you are writing code
● Commit this code on your github link under pythonbasic branch
'''

intlist=[]
sum=0
for i in range(5):
  number=int(input(f"Enter the integer {i+1} :"))
  if number >=9:
    sum+=number
    intlist.append(number)
print(f"The sum of {intlist} is :{sum}")

'''
Sample Output
Enter the integer 1 :23
Enter the integer 2 :32
Enter the integer 3 :12
Enter the integer 4 :43
Enter the integer 5 :21
The sum of [23, 32, 12, 43, 21] is :131
'''

