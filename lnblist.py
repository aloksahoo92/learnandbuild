'''4. List operations and decoding
● two lists are given below L1, L2.
● create a new list called L3 containing items in below given pattern
● From L1 it must take only odd index items
● From L2 it must take only even index items
● file name must be lnblist.py in which you are going to write the code
● commit this code on your github link under pythonbasic branch
Inputs : L1 = [11, 21, 24, 12, 18]
L2 = [14, 44, 25, 37, 13]
Expected output : L3=[11,24,18,44,37]'''
L1 = [11, 21, 24, 12, 18]
L2 = [14, 44, 25, 37, 13]
L3=[]
for i in range(len(L1)):
  if i%2==0:
    L3.append(L1[i])
for i in range(len(L2)):
  if i%2!=0:
    L3.append(L2[i])

print(f"L3={L3}")
