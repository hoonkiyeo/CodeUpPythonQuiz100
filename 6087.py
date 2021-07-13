#!/usr/bin/env python
# coding: utf-8

# In[2]:


#sol_1

def without_three_times(start):
    n = int(input())
    
    for i in range(start, n+1):
        if i % 3 == 0:
            continue
        else:
            print(i, end=" ")
            
without_three_times(1)


# In[6]:


#sol_2

n = int(input())
start = 0

while start < n:
    start += 1
    if start % 3 == 0:
        continue
    print(start, end = ' ')

