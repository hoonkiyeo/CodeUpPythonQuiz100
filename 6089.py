#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1

def geom_sequence():
    a, r, n=map(int, input().split())
    sum = a
    for i in range(1,n):
        sum = sum * r
        
    return sum

print(geom_sequence())


# In[9]:


#sol_2

def geom_sequence2():
    a,r,n = map(int,input().split())
    count = 1
    while count < n:
        count += 1
        a = a * r
    return a

print(geom_sequence2())

