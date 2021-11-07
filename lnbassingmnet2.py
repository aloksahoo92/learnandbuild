'''
5. Trekking with friends
● Three friends Suman, Amit and Ravi have gone for trekking and there they
decided to plan a racing among themselves
● Amit beats Suman by A(10) meters, Ravi by B(20) meters and 
Suman beats Ravi by C(12) meters
● Find the total length of trek they all have travelled
● File name must be in lnbassingmnet2.py in which you are writing code
Sample Input: A= 10 m, B= 20 m, C= 12m
Sample Output: Total length of the Track= 60 m
'''
def lcm(x, y):
  if x > y:
    greater = x
  else:
    greater = y
  while(True):
    if((greater % x == 0) and (greater % y == 0)):
      lcm = greater
      break
    greater += 1
  return lcm
  
numblist=[]
for i in range(3): 
  numb=int(input(f"Enter the length of trek have travelled by friend {i+1} :"))
  numblist.append(numb)
print(f"The total length of trek they all have travelled :{lcm(lcm(numblist[0],numblist[1]),numblist[2])}")

'''
Sample Output
Enter the length of trek have travelled by friend 1 :10
Enter the length of trek have travelled by friend 2 :20
Enter the length of trek have travelled by friend 3 :12
The total length of trek they all have travelled :60
'''
