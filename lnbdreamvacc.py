'''
8. Dream vacation
● Take input from the in the form of list and dictionary
● Create a prompt for a dream vacation of people in the following manner
● Ask people to join the poll in yes/no form
● If a person says yes, then ask his name and if no then start the poll again
● Take input from the user to create a list of places he wants to go.
● Ask for a 'done' input once the person has finished creating the list of
places.
● Then again start the loop for polling
● When the user gives input, quit then stop the prompt.
● Print the poll result.
● File name must be in lnbdreamvacc.py in which you are writing code
'''
dictvacat={}
listvacat=[]
flistvacat=[]
fsetvacat={}
flist=[]
while True:
  poll=input("\nDo you want to join the poll ? (yes/no) :").upper()
  if poll=="YES":
    name=input("Enter the person name :")
    
    vacat=input("Enter the vacation place :")
    listvacat.append(vacat)
    while True:
      morevacat=input("Do you want vacation to be add ? (yes/no) :").upper()
      if morevacat=="YES":
        vacat=input("Enter the vacation place :")
        listvacat.append(vacat)

      elif morevacat=="NO":
        print(listvacat)
        dictvacat[name]=listvacat
        print(dictvacat)
        listvacat=[]
        break
  elif poll=="NO":
    break
  else:
    print("Invaid input !!!")
    break

for i in dictvacat:
  for j in range(len(dictvacat[i])):
    flistvacat.append(dictvacat[i][j])
    
fsetvacat=set(flistvacat)
print(f"The Deam Vacations place for all persons are :")
flist=list(fsetvacat)
for i in range(len(flist)):
  print(flist[i])

'''
Sample Output
Do you want to join the poll ? (yes/no) :yes
Enter the person name :Alok
Enter the vacation place :LA
Do you want vacation to be add ? (yes/no) :yes
Enter the vacation place :Leh
Do you want vacation to be add ? (yes/no) :no
['LA', 'Leh']
{'Alok': ['LA', 'Leh']}

Do you want to join the poll ? (yes/no) :yes
Enter the person name :Raj
Enter the vacation place :Leh
Do you want vacation to be add ? (yes/no) :yes
Enter the vacation place :Mumbai
Do you want vacation to be add ? (yes/no) :no
['Leh', 'Mumbai']
{'Alok': ['LA', 'Leh'], 'Raj': ['Leh', 'Mumbai']}

Do you want to join the poll ? (yes/no) :no
The Deam Vacations place for all persons are :
LA
Leh
Mumbai
'''


  

