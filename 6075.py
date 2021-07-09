#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1

n = int(input())
count = 0
while count <= n:
    print(count)
    count += 1


# In[5]:


#sol_2

n = int(input())
count = 0

while True:
    print(count)
    count += 1
    if count > n:
        break

