#!/usr/bin/env python
# coding: utf-8

# In[45]:


#sol_1
n = int(input())

if n > 30:
    print("n must be less than 30")
    print("try again")
else:
    for i in range(1, n+1):
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
            print("X", end = " ")
        else:
            print(i, end = " ")


# In[47]:


#sol_2

n = int(input())


if n > 30:
    print("n must be less than 30")
    print("try again")
else:
    
    for i in range(1, n+1):
        if '3' in str(i) or '6' in str(i) or '9' in str(i):
            print("X", end = ' ')
        else:
            print(i, end = ' ')  

