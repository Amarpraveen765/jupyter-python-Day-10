#!/usr/bin/env python
# coding: utf-8

# ### Standard Libraries 
# - File I/O
# - Regular Expression
# - Datetime
# - Math (numerical and mathematical)

# ### File Handling in python
#   
#   - File :- Document containing information resides on the permanenet storage
#   - Different types of Files :- txt,doc,pdf,csv,and etc...
#   - input -- keyboard
#   - Output -- File
# 
# ### Modes of the File I/O
# * 'w' -- used to file writing -- if the file is not present firts it creats the file and writes some data to it
#         
# 

# In[1]:


# Function to creat and write to the file
def createfile(filename):
    f = open(filename,'w')
    for i in range(10):
        f.write(" this is %d line\n " %i)
    print("file is created and data has be written")
    return
createfile("file1.txt")


# In[2]:


ls


# In[3]:


import os
cat file1.txt


# In[6]:


def createfile(filename):
    f = open(filename,'w')
    f.write("testing...\n")
    print("file is created and data has be written")
    return
createfile("file1.txt")


# In[7]:


ls


# In[8]:


def appenddata(filename):
    f = open(filename,'w')
    for i in range(10):
        f.write("this is %d line\n" % i)
    print("file is created and dta is writen")
    return
appenddata('file2.txt')


# In[9]:


def appenddata(filename):
    f = open(filename,'a')
    f.write("New line 1 \n")
    f.write("New line 2 \n")
    print("file is created and dta is writen")
    return
appenddata('file2.txt')


# In[10]:


# function to read of the file 
def readfiledata(filename):
    f = open(filename,'r')
    if f.mode == 'r':
        x = f.read()
        print(x)
    f.close()
    return
readfiledata('file2.txt')
    


# In[11]:


# fuction to read the file
def fileoperations(filename,mode):
    with open(filename,mode) as f:
        if f.mode == 'r':
            data = f.read()
            print(data)
        elif f.mode == "a":
            f.wirte("data to the file")
            print('the data successfully written')
    f.close() 
    return
filename = input('enter the file name')
mode = input('enter the mode of the file')
fileoperations(filename,mode)


# In[12]:


# Data Analysis
# word count program
def wordcount(filename,word):
    with open(filename,'r') as f:
        if  f.mode == 'r':
            x = f.read()
            li = x.split() # it's splits the string with 
    cnt = li.count(word)
    return cnt
filename = input('enter the file name:- ')
word = input('enter the word ')
wordcount(filename,word)
    
    


# In[5]:


# character count from the given file
def charcount(filename):
    with open(filename,'r') as f:
        if  f.mode == 'r':
            x = f.read()
            li = list(x) # convert the string- char
    return len(li)
filename = input('enter the file name:- ')
charcount(filename)


# In[4]:


s1 = 'python programming'
print(s1.split('a'))


# In[15]:


# function to find the no of lines in the inout file 
# input : filename(file2.txt)
# output : no of lines (12)

# Data Analysis
# word count program
def countoflines(filename):
    with open(filename,'r') as f:
        if  f.mode == 'r':
            x = f.read()
            li = x.split('\n') # it's splits the string with 
    return len(li)
filename = input('enter the file name:- ')
countoflines(filename)
    


# In[19]:


# function to print the upper and lower characters
def casecount(filename):
    cntupper = 0
    cntlower = 0
    with open(filename,'r') as f:
        if f.mode == 'r':
            x = f.read()
            li = list(x)
    for i in li:
        if i.isupper():
            cntupper += 1
        elif i.islower():
            cntlower += 1
    output = 'Upper case = {0} , lower case = {1}'.format(cntupper,cntlower)
    return output
filename = input('enter the file name:- ')
casecount(filename)


# In[20]:


ls


# In[21]:


cd desktop/pythonprog/Git


# In[22]:


cd/Desktop/Problemsolvingprogramming/Git


# In[23]:


cd/Desktop/ProblemSolvingProgramming/Git


# In[24]:


cd/desktop/ProblemSolvingProgramming/Git


# In[25]:


cd/desktop/python/git


# In[26]:


cd\desktop\ProblemSolvingProgramming\Git


# In[30]:


cd Desktop\ProblemSolvingProgramming


# In[31]:


ls


# In[38]:


import os
os.listdir('Git/')


# In[39]:


li = os.listdir('Git/')
for i in li:
    print(i)


# - older version python -- os.listdir()
# - new version python -- os.scandir() and pathlib.path()

# In[40]:


li = os.scandir('Git/')
for i in li:
    print(i)


# In[41]:


from pathlib import Path
li = Path('Git/')
for i in li.iterdir():
    print(i.name)


# ## Listing all Files in a directory

# In[50]:


import os
dirPath = "Git/"
for i in os.listdir(dirPath):
    if os.path.isfile(os.path.join(dirPath,i)):
        print(i)


# In[51]:


pwd


# In[52]:


dirPath = 'Git/'
with os.scandir(dirPath) as f:
    for i in f:
        if i.is_file():
            print(i.name)


# ### Listing Subdirectories

# In[53]:


dirPath = 'Git/'
for i in os.listdir(dirPath):
    if os.path.isdir(os.path.join(dirPath,i)):
        print(i)


# In[55]:


from pathlib import Path
dirPath = Path('Git/')
for i in dirPath.iterdir():
    if  i.is_dir():
        print(i.name)
    


# In[56]:


dirPath = 'Git/'
with os.scandir(dirPath) as f:   
    for i in f:
        if i.is_dir():
            print(i.name)


# ### Creating a single Directory

# In[66]:


import os
os.mkdir('SingleDirectory')


# In[67]:


import pathlib
p = pathlib.Path('TestFolder')
p.mkdir()


# In[68]:


ls


# ### Creating multiple directories

# In[70]:


import os
os.makedirs('2019/july/11')


# In[71]:


ls


# ### Filename Pattern Matching

# In[84]:


cd ..


# In[85]:


import os 
dirPath = 'Git/'
for f_name in os.listdir(dirPath):
    if f_name.endswith('.ipynb'):
        print(f_name)


# In[89]:


import os 
dirPath = 'Git/'
for f_name in os.listdir(dirPath):
    if f_name.startswith('da'):
        print(f_name)


# ### Deleteing files and Directories

# In[93]:


cd ProblemSolvingProgramming


# In[94]:


cd Git


# In[114]:


cd ..


# In[112]:


import os 
data_file = 'file1.txt'  # give the entire path c:\\Users\\dell\\filename
os.remove(data_file)


# In[103]:


data_dir = 'TestFolder'
os.rmdir(data_dir)


# In[107]:


ls


# In[108]:


data_dir = '2019'
os.rmdir(data_dir)


# In[110]:


import shutil
data_dir = '2019'
shutil.rmtree(data_dir)


# ### Regular Expressions
#   - used to specific pattern 

# In[ ]:




