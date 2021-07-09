#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1
a=int(input())

while a!=0:
    print(a)
    a=a-1


# In[19]:


#sol_2

n = int(input())
count_list = []

for i in range(1, n+1):
    count_list.append(i)

count_list.reverse()
for i in count_list:
    print(i, sep = "\n")

