#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1

a=int(input())

while a!=0:
    a=a-1
    print(a)


# In[8]:


#sol_2

n = int(input())
count_list = []

for i in range(n):
    count_list.append(i)
count_list.reverse()

for i in count_list:
    print(i)


# In[9]:


#sol_3

n = int(input())

while True:
    n = n-1
    print(n)
    if n == 0:
        break

