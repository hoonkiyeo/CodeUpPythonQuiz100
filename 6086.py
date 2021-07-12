#!/usr/bin/env python
# coding: utf-8

# In[2]:


#sol_1

def stop_sum():
    n = int(input())
    total_sum = 0
    for i in range(1, n+1):
        sum += i
        if sum == n or sum > n:
            break
        else:
            continue
    return sum

print(stop_sum())
            


# In[3]:


#sol_2

def stop_sum():
    n = int(input())
    total_sum = 0
    start = 0

    while True:
        total_sum += start
        start += 1
        if total_sum >= n:
            break
    
    return total_sum

print(stop_sum())


# In[ ]:




