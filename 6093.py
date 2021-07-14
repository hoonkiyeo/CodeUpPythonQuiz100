#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1

n = int(input())
a = input().split()

a_lst=[]
num_lst = []


for i in range(n):
    a[i] = int(a[i])
    a_lst.append(a[i])
    
for a in a_lst:
    num_lst.append(a)

for i in range(n-1, -1, -1):
    print(num_lst[i], end = " ")


# In[2]:


#sol_2

n = int(input())
a = list(map(int, input().split()))

for i in range(n-1, -1, -1):
    print(a[i], end = ' ')

