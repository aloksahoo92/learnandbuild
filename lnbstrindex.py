'''
3. Take User input in string form and perform operation
● Take input from user in string form only and calculate the length of string
● IF length is greater than 7 then display only those character which are
present in even index number
● if length is less than or equals to 7 then display only those character which
are present in odd index number
● file name must be lnbstrindex.py in which you are writing code
● commit this code on your github link under pythonbasic branch'''
str1=[]
evenstrlist=[]
oddstrlist=[]
str1=input("Enter the string :")
strlen=len(str1)
for i in range(strlen):
  if i%2==0:
    evenstr=str1[i]
    evenstrlist.append(evenstr)
  else:
    oddstr=str1[i]
    oddstrlist.append(oddstr)

if strlen>7:
  print(f"The output string is :{evenstrlist}")
else:
  print(f"The output string is :{oddstrlist}")

'''
Enter the string :Python is a cross-platform programming language
The output string is :['P', 't', 'o', ' ', 's', 'a', 'c', 'o', 's', 'p', 'a', 'f', 'r', ' ', 'r', 'g', 'a', 'm', 'n', ' ', 'a', 'g', 'a', 'e']

Enter the string :Python
The output string is :['y', 'h', 'n']
'''
