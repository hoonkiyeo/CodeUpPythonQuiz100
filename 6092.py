#!/usr/bin/env python
# coding: utf-8

# In[2]:


#sol_1

n = int(input())
a = input().split()

d = []
for i in range(24):
    d.append(0)
    
for i in range(n):
    a[i] = int(a[i])
    
for i in range(n):
    d[a[i]] += 1
    
for i in range(1,24):
    print(d[i], end = ' ')
    
#input
'''
10
1 3 2 2 5 6 7 4 5 9
'''
#output
'''
1 2 1 1 2 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
'''


# In[6]:


#sol_2

n = int(input())
a = list(map(int,input().split()))
student_list = []
for i in range(24):
    student_list.append(0)

for i in a:
    student_list[i-1] += 1

for student in student_list:
    print(student, end = ' ')
    
#input
'''
10
1 3 2 2 5 6 7 4 5 9
'''
#output
'''
1 2 1 1 2 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
'''


# In[7]:


#sol_3

def attendence_check():
    n = int(input())
    num_list = list(map(int, input().split()))
    student_list = []
    for i in range(24):
        student_list.append(0)
        
    for i in a:
        student_list[i-1] += 1
    for student in student_list:
        print(student, end = ' ')
attendence_check()

#input
'''
10
1 3 2 2 5 6 7 4 5 9
'''
#output
'''
1 2 1 1 2 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
'''

