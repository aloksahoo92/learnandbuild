'''
14.MAKE A PROGRAM TO MERGE TWO LIST INTO A
SINGLE DICTIONARIES
● Take inputs from the user
● Any one list must contain unique elements
● both the list should be of the same size
● both the list should be a combination of numbers and names
● Name of dictionary you can take it accordingly
● file name should be in lnbmerge.py
● commit the code on github link under pythonbasic branch
'''
namelist=[]
marklist=[]
studict={}
studno=int(input("\nEnter the number of student :"))
for i in range(studno):
  name=input(f"Enter the name of student {i+1} :")
  mark=int(input(f"Enter the mark of studend {i+1} :"))
  namelist.append(name)
  marklist.append(mark)
  studict[name]=mark
print(f"Name of the student :{namelist}")
print(f"Mark of the student :{marklist}")
print(f"Detail of the student :{studict}")

'''
Sample Output

Enter the number of student :4
Enter the name of student 1 :RAJ
Enter the mark of studend 1 :45
Enter the name of student 2 :RAHUL
Enter the mark of studend 2 :55
Enter the name of student 3 :RAVI
Enter the mark of studend 3 :56
Enter the name of student 4 :RAKESH
Enter the mark of studend 4 :66
Name of the student :['RAJ', 'RAHUL', 'RAVI', 'RAKESH']
Mark of the student :[45, 55, 56, 66]
Detail of the student :{'RAJ': 45, 'RAHUL': 55, 'RAVI': 56, 'RAKESH': 66}
'''
