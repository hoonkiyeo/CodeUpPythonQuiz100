#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1

def smallest_num_in_list():
    
    n = int(input())
    a = list(map(int, input().split()))
    smallest_num = 10000000
    
    for num in a:
        if num < smallest_num:
            smallest_num = num
    
    return smallest_num

print(smallest_num_in_list())

