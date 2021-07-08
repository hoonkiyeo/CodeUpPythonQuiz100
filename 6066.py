#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1
a,b,c = map(int,input().split())

if a % 2 == 0:
    print("even")
else:
    print("odd")
    
if b % 2 == 0:
    print("even")
else:
    print("odd")
    
if c % 2 == 0:
    print("even")
else:
    print("odd")


# In[2]:


#sol_2
a,b,c = map(int,input().split())

print("even" if a % 2 == 0 else "odd")
print("even" if b % 2 == 0 else "odd")
print("even" if c % 2 == 0 else "odd")


# In[ ]:




