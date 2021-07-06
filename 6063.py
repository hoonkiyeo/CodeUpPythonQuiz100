#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1
a, b = input().split()
a = int(a)
b = int(b)
c = a if a>=b else b
print(c)


# In[2]:


#sol_2
a,b = map(int, input().split())
if a >= b:
    print(a)
else:
    print(b)


# In[ ]:




