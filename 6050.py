#!/usr/bin/env python
# coding: utf-8

# In[1]:


a, b = input().split()
a = int(a)
b = int(b)
print(a<=b)


# In[ ]:


a,b = map(int,input().split())
if a <= b:
    print(True)
else:
    print(False)

