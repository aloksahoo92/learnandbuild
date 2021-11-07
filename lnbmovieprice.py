'''
6. Movie tickets:
● A movie theater charges different ticket prices depending on person's age
● Take input from the user in the form of age and number of people
respectively
● If a person is under the age of 3, the ticket is free
● If a person is between 3 and 12, the tickets are 100 rupees.
● If a person is above 12 then the tickets are 150 rupees.
● Take input of the age and print the cost of their tickets.
'''
price=0
totalprice=0
while True:
  age=int(input(f"Enter the age of person  :"))
  person=int(input(f"Enter the person number :"))
  if age<3:
    price=0
  elif age>=3 and age<12:
    price=100
  else:
    price=150
  totalprice+=person*price
  print(f"Total Price :Rs {totalprice}")
  more=input(f"more data ? (yes/no) :")
  if more=="no":
    break
  else:
    continue

'''
Sample Output
Enter the age of person  :10
Enter the person number :20
Total Price :2000
more data ? (yes/no) :y
Enter the age of person  :30
Enter the person number :20
Total Price :5000
more data ? (yes/no) :no
'''