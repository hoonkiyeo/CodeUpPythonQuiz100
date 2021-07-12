#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1

r,g,b = map(int, input().split(" "))
count = 0

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j,k, sep = " ")
            count += 1
print(count)


# In[2]:


#sol_2

r,g,b = map(int,input().split())

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
print(r*g*b)

