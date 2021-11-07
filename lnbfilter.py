'''
10. Filter
● Create a function even_filter with one parameter. This function will return a
list which will contain only odd values.
● Create a function odd_filter with one parameter. This function will return a
list which will contain only even values.
● Call the function even_filter and pass a list of numbers as an argument.
● Call the function odd_filter and pass a dictionary as an argument.
● NOTE: The list and dictionary must be user defined.
● File name must be lnbfilter.py in which you are writing code.
'''
evenlist=[]
oddlist=[]
fdict={}
evenfilter=[]
oddfilter=[]
def even_filter(num):
  if num%2!=0:
    oddlist.append(num)
    return oddlist
def odd_filter(num):
  if num%2==0:
    evenlist.append(num)
    return evenlist
while True:

  q=input("\n Do you want to check the number (yes/no) :").upper()
  if q=="YES":
    num=int(input("Enter the number :"))
    even_filter(num)
    odd_filter(num)
    print(f"Even filter Output :{oddlist}")
    print(f"Odd filter Output :{evenlist}")

  else:
    break 
print(f"Even filter Output :{oddlist}")
print(f"Odd filter Output :{evenlist}")

'''
Sample Output
Do you want to check the number (yes/no) :yes
Enter the number :22
Even filter Output :[]
Odd filter Output :[22]

 Do you want to check the number (yes/no) :yes
Enter the number :23
Even filter Output :[23]
Odd filter Output :[22]

 Do you want to check the number (yes/no) :yes
Enter the number :25
Even filter Output :[23, 25]
Odd filter Output :[22]

 Do you want to check the number (yes/no) :yes
Enter the number :0
Even filter Output :[23, 25]
Odd filter Output :[22, 0]

 Do you want to check the number (yes/no) :no
Even filter Output :[23, 25]
Odd filter Output :[22, 0]
'''
