'''
13. Paragraph to list
● Take input from the user in string form(a sentence or para)
● All the words in the string having more than 4 letters should be stored in a
list
● file name must be lnbstring_list.py in which you are writing code.
● commit this code on your github link under pythonbasic branch
Sample Input : A paragraph is defined as “a group of sentences or a single sentence
that forms a unit”. Length and appearance do not determine whether a section in a
paper is a paragraph.
Sample Output : [ ‘paragraph’ , ‘defined’, ‘group’ , ‘sentences’ , ‘forms’ , ‘Length’ ,
‘appearance’ , ‘determine’ , ‘whether’ , ‘section’ , ‘paper’ , ‘paragraph’ ]
'''
paralist=[]
para=input("Enter the string :")
p=para.split(" ")
for i in range(len(p)):
  p[i] =  ''.join(filter(str.isalnum, p[i])) 
  if len(p[i])>4:
    paralist.append(p[i])
print(paralist)

'''
Enter the string :A paragraph is defined as “a group of sentences or a single sentence that forms a unit”. Length and appearance do not determine whether a section in a paper is a paragraph.
['paragraph', 'defined', 'group', 'sentences', 'single', 'sentence', 'forms', 'Length', 'appearance', 'determine', 'whether', 'section', 'paper', 'paragraph']
'''

