'''
8. Splitting the list
● Create a list ranging from 1-20
● Create a new list that contains first and the last five elements of the
existing list
● Now create and display another list that contains square of the elements
of the new list
● Now split the new list into three parts where the length of splitted parts
should be two, three and five respectively
● File name must be in lnblist.py in which you are writing code
● Commit this code on your github link under the python string branch
'''
lis=[]
lis2=[]
lis2sq=[]
lis3=[]
lis4=[]
lis5=[]
for i in range(20):
  datalis=int(input(f"Enter the integer {i+1} :"))
  lis.append(datalis)
  if i==0 or i==15 or i==16 or i==17 or i==18 or i==19 :
    lis2.append(lis[i])
for j in range(len(lis2)):
  datasq=lis2[j]**2
  lis2sq.append(datasq)
print(f"list 1 :{lis}")
print(f"list 2 :{lis2}")
print(f"list 3 :{lis2sq}")
for k in range(len(lis2sq)):
  if k<=2:
    lis3.append(lis2sq[k])
  elif k==3:
    lis4.append(lis2sq[k])
  elif k==5 or k==4:
    lis5.append(lis2sq[k])
print(f"list 4 :{lis3}")
print(f"list 5 :{lis4}")
print(f"list 6 :{lis5}")

'''
Sample Output
Enter the integer 1 :12
Enter the integer 2 :32
Enter the integer 3 :32
Enter the integer 4 :12
Enter the integer 5 :43
Enter the integer 6 :54
Enter the integer 7 :32
Enter the integer 8 :13
Enter the integer 9 :53
Enter the integer 10 :42
Enter the integer 11 :42
Enter the integer 12 :87
Enter the integer 13 :43
Enter the integer 14 :21
Enter the integer 15 :4
Enter the integer 16 :1
Enter the integer 17 :23
Enter the integer 18 :43
Enter the integer 19 :22
Enter the integer 20 :2
list 1 :[12, 32, 32, 12, 43, 54, 32, 13, 53, 42, 42, 87, 43, 21, 4, 1, 23, 43, 22, 2]
list 2 :[12, 1, 23, 43, 22, 2]
list 3 :[144, 1, 529, 1849, 484, 4]
list 4 :[144, 1, 529]
list 5 :[1849]
list 6 :[484, 4]
'''
