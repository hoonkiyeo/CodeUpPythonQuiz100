#!/usr/bin/env python
# coding: utf-8

# In[2]:


a, b = input().split()
print(bool(int(a)) or bool(int(b)))


# In[5]:


a,b = map(int, input().split())

if bool(a) == True | bool(b) == True:
    print(True)
else:
    print(False)


# In[ ]:




