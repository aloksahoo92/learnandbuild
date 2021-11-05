'''
9. Raining like cats and dogs
● Take user input in the form of a string.
● Return True if the string "cat" and "dog" appear the same number of times
in the given string
● file name must be lnbcatndog.py in which you are writing code
● commit this code on your github link under pythonstring branch
Sample Input    Sample Output
‘Catdog’        True
‘Catcat’        False
‘Hello’         False
'1cat1cadodog'  True

'''
catcount=0
dogcount=0
inputstr=input("Enter the string :")
catcount=inputstr.count('cat')
dogcount=inputstr.count('dog')
if catcount==dogcount:
  print("The result is : True")
else:
  print("The result is : False")

'''
Sample Output
Enter the string :catdogcatdoghhhhcatdog
The result is : True
Enter the string :catcatdog
The result is : False
'''
