#!/usr/bin/env python
# coding: utf-8

# In[1]:


a, b = input().split()
print(bool(int(a)) and bool(int(b)))


# In[2]:


a, b = map(int, input().split())

if bool(a) == True and bool(b) == True:
    print(True)
else:
    print(False)


# In[ ]:




