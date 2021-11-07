'''
3. Display the new lists
● Take user input in numeric format to create a list
● Display and calculate the list of all the numbers divisible by 11 but not by 2
and 3, between 100-500
● Now split the entire list to create tuples of length 2,4 and 6 respectively
● Display the new list
● File name must be in lnbdisplayass2.py in which you are writing code
'''
numblist=[]
list1=[]
list2=[]
list3=[]
for i in range(100,501):
  if i%11==0 and not(i%2==0 or i%3==0):
    numblist.append(i)
print(numblist)
for i in range(len(numblist)):
  if i<2:
    list1.append(numblist[i])
  elif i>=2 and i<=5:
    list2.append(numblist[i])
  elif i>=6:
    list3.append(numblist[i])
print(f"Output :{list1},{list2},{list3}")

'''
Sample Output
[121, 143, 187, 209, 253, 275, 319, 341, 385, 407, 451, 473]
Output :[121, 143],[187, 209, 253, 275],[319, 341, 385, 407, 451, 473]
'''
