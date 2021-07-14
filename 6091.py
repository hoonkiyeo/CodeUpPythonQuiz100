#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1

a,b,c = map(int, input().split())

d = 1

while d % a != 0 or d % b != 0 or d % c != 0:
    d += 1
    
print(d)


# In[11]:


#sol_2

def lcm_calculator():
    a,b,c = map(int,input().split())
    i = 1
    
    while True:
        if (i % a == i % b == i % c == 0):
            break
        else:
            i += 1
    return i

print(lcm_calculator())

