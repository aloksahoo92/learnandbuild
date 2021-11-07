'''
2. Calendar
● Take input from the user in form of three integers
● The three integers represent a year, month and day
● Print the season of that month and day
● Now check whether the given year is a leap year or not
● If the year is a leap year then print the number of days in that year else print the
next leap year
● file name must be lnbcalendercoditional.py in which you are writing the code
● Commit this code on your github link under pythonbasic branch.

'''
import calendar
year=int(input("Enter the year :"))
month=int(input("Enter the month :"))
day=int(input("Enter the day :"))
print(calendar.month(year, month))
if year/4==0:
  print(f"The number of days in {year} is 366")
else:
  ly=year%4 #2017 1,2018 2,2019 3,2020 0
  year=year-ly+4
  print(f"The next Leap year is :{year}")

'''
Sample Output
Enter the year :2017
Enter the month :3
Enter the day :1
     March 2017
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31

The next Leap year is :2020
'''
