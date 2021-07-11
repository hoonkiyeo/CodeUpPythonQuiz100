#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1

a,b = map(int, input().split())


for i in range(1, a+1):
    for j in range(1, b+1):
        print(i,j)

