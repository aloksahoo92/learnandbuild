'''
10. Convert tuple to list using given string
● Take input from the user in the form of tuple
● Take another input from the user in the form of string
● Convert the tuple to list
● Add string to the list after each element
● Convert list to tuple again
● File name must be lnbconvtuple.py in which you are writing the code
● Commit this code on your github link under pythonbasic branch
Sample Input: (21,37,18), K= “Age”
Sample output: (21,”Age”,37,”Age”,18,”Age”)
'''
datalis=[]
d1tuple=()
dataoutuple=()
datatup=()
dataoutlis=[]
dataouttup=()
lenum=int(input("Enter the number of input :"))
for i in range(lenum):
  num=int(input(f"Enter the data {i+1} :"))
  datalis.append(num)
d1tuple=tuple(datalis)
print(f"The tuple is : {d1tuple}")
strdata=input("Enter the string :")
for j in range(len(datalis)):
  if j/1==j:
    dataoutlis.append(datalis[j])
    dataoutlis.append(strdata)
dataoutuple=tuple(dataoutlis)
print(dataoutuple)

'''
Enter the number of input :4
Enter the data 1 :23
Enter the data 2 :43
Enter the data 3 :23
Enter the data 4 :54
The tuple is : (23, 43, 23, 54)
Enter the string :age
(23, 'age', 43, 'age', 23, 'age', 54, 'age')
'''
