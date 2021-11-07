'''
12. Prompt Maybe
● Define a function that:
. Uses lambda function to make a list consisting of cube of each
value in the list.
. Ask the user ‘Do you need the sum of all cubic values?’ and
continue if the user says ‘yes’ and return the list if it says ‘no’.
. If the user gives some other input then ‘yes’ and ‘no’, give 3 trials
to the user reminding that,“Input must be ‘yes’ or ‘no’! ”. Else break
the loop and return nothing.
● File name must be lnbprompt.py in which you are writing code
'''
numlist=[]
cubelist=[]
cubeno=0
cubesum=0
count=0
while True:
  q=input(f"\nDo you want to add a number to numlist {numlist} :(yes/no)").upper()
  if q=="YES":
    num=int(input("Enter the number : "))
    numlist.append(num)
    cube=lambda n:n*n*n
    for i in range(len(numlist)):
      cubeno=cube(numlist[i])
    cubelist.append(cubeno)
    print(numlist,cubelist)
    qsum=input(f"Do you need the sum of all cubic values? :(yes/no)").upper()
    if qsum=="YES":
      for i in range(len(cubelist)):
        cubesum+=cubelist[i]
      print(f"The sum of all cubic values is : {cubesum}")
    elif qsum=="NO":
      print(f"The cubic list is : {cubelist}")
    else:
      count+=1
      print(count)
      if count>3:
        break
      else:
        print(f"Reminder {count} :Input must be ‘yes’ or ‘no’! ")

  else:
    break

'''

Do you want to add a number to numlist [] :(yes/no)yes
Enter the number : 6
[6] [216]
Do you need the sum of all cubic values? :(yes/no)yes
The sum of all cubic values is : 216

Do you want to add a number to numlist [6] :(yes/no)no
'''
