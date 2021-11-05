'''
6. Operating the tuples
● Take input from the user in form of integers (minimum10 & maximum 20
integers)
● Convert the integers into binary tuples
● Use the operators AND & OR for the last two binary tuples and then
display the result
● Now convert the resultant tuple into integer and display the value
● File name must be lnbtuple.py in which you are writing the code
● Commit this code on your github link under pythonbasic branch
'''
datalist=[]
databinlist=[]
databintuple=()

no=int(input("Enter the no of input (number should be (minimum10 & maximum 20):"))
if no>=10 and no<=20:
  for i in range(no):
    data=int(input(f"Enter the integer {i+1}:"))
    datalist.append(data)
    databin=int(bin(data).replace("0b", ""))
    databinlist.append(databin)
    finaland=databinlist[0]
    finaland=finaland & databinlist[i]
    finalor=databinlist[0]
    finalor=finalor | databinlist[i]
    databintuple=tuple(databinlist)

print(databintuple)
databinand=bin(finaland)
databinor=bin(finalor)
print(f"And of all input: {finaland}\nin binary format: {databinand},\n\nOr of all input: {finalor}\nin binary format: {databinor}")

'''
Sample output
Enter the no of input (number should be (minimum10 & maximum 20):10
Enter the integer 1:1
Enter the integer 2:2
Enter the integer 3:3
Enter the integer 4:4
Enter the integer 5:5
Enter the integer 6:6
Enter the integer 7:6
Enter the integer 8:6
Enter the integer 9:7
Enter the integer 10:7
(1, 10, 11, 100, 101, 110, 110, 110, 111, 111)
And of all input: 1
in binary format: 0b1,

Or of all input: 111
in binary format: 0b1101111
'''
