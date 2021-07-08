#!/usr/bin/env python
# coding: utf-8

# In[2]:


#sol_1
n=int(input())

if n < 0:
    if n % 2 == 0:
        print("A")
    else:
        print("B")
else:
    if n % 2 == 0:
        print("C")
    else:
        print("D")
        


# In[1]:


#sol_2
n = int(input())

def classification(x):
    if x < 0:
        if x % 2 == 0:
            print("A")
        else:
            print("B")
    
    elif x == 0:
        print("input cannot be zero")
        print("try again")
    else:
        if x % 2 == 0:
            print("C")
        else:
            print("D")
            
classification(n)


# In[ ]:




