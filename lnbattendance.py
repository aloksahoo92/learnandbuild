'''
5. Attendance of the Employees
● A Company’s CEO wants the attendance of all the employees
● There are e no.of employees and w no.of working days
● Find the maximum number of consecutive days on which all the
employees are present
● File name must be lnbattendance.py in which you are writing the code
● Commit this code on your github link under pythonbasic branch
* Constraints:
1<=e<=10
1<=w<=31
Each data[i][j]={‘P’,’A’}
Sample Input: e= 5 , w= 7
Data = [PPPPP, PPAPP, AAAPP, PAPAP, AAAAA, PAAAP, PPPPP]
Sample output: 1,7
'''

count=0
empno=int(input("Enter the number of Employees :"))
workday=int(input("Enter the number of Working days :"))
data=[]
if (empno<=10 and empno>=1)and(workday<=31 and workday>=1):
  for i in range(workday):
    attendata=input(f"Enter the Attendance details (P/A)  for day {i+1}:").upper()
    if len(attendata)==empno:
      data.append(attendata)  
    else:
      print(f"Invaid input!!!.\nEnter the number attendance like:-for all Present {'P'*empno} or for all Absent {'A'*empno}")
      break
  print(f"So the attendance data is :{data}")
  attend=0
  print("The maximum number of consecutive days on which all the employees are present on :")
  for attend in range(len(data)):

    if data[attend] =='P'*empno:
      count+=1
      print(attend+1)
else:
  print("Invaid input!!! 1<=number of employees <=10 and 1<=working days<=31")


'''
Sample Output
Enter the number of Employees :5
Enter the number of Working days :5
Enter the Attendance details (P/A)  for day 1:ppppp
Enter the Attendance details (P/A)  for day 2:papap
Enter the Attendance details (P/A)  for day 3:aaaaa
Enter the Attendance details (P/A)  for day 4:ppppp
Enter the Attendance details (P/A)  for day 5:ppppp
So the attendance data is :['PPPPP', 'PAPAP', 'AAAAA', 'PPPPP', 'PPPPP']
The maximum number of consecutive days on which all the employees are present on :
1
4
5
'''
