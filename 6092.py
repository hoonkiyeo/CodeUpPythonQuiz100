#!/usr/bin/env python
# coding: utf-8

# In[20]:


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


# In[22]:


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


# In[26]:


#sol_2

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

