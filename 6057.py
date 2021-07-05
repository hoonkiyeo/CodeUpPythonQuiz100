#!/usr/bin/env python
# coding: utf-8

# In[1]:


a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print((a and b) or (not a and not b))


# In[2]:


a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print(a==b)


# In[4]:


a,b = map(int,input().split())
c = bool(a)
d = bool(b)
if c == d:
    print(True)
else:
    print(False)


# In[ ]:




