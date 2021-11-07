'''
7. Divisibility
● Take input in the form of binary numbers
● Print all the binary numbers between smallest 4-digit and largest 4-digit
● If the numbers are not divisible by 5 stop the iteration and pass all the
remaining numbers in form of (n+1)
● If the numbers are divisible by 5 then continue the iteration and print all
the binary numbers separated by commas.
● File name must be in lnbpasscontinue.py in which you are writing code
'''
listnumb=[]
no=int(input("Enter the number of input :"))
for i in range(no):
  binumb=input(f"Enter the binary number :") #0b01001
  numb=int(binumb,2)
  print(binumb,numb)
  listnumb.append(numb)
smallest=listnumb[0]
largest=listnumb[0]
for i in range(len(listnumb)):
  if smallest>listnumb[i]:
    smallest=listnumb[i]
  if largest<listnumb[i]:
    largest=listnumb[i]
  if listnumb[i]%5!=0:
    print(listnumb[i])
    break
  else:
    print(listnumb[i])

print(smallest,largest)

'''
Sample Output
Enter the number of input :4
Enter the binary number :0b1010
0b1010 10
Enter the binary number :0b1111
0b1111 15
Enter the binary number :0b0010
0b0010 2
Enter the binary number :0b0101
0b0101 5
10
15
2
2 15
'''
