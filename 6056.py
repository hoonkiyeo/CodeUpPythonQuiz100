#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1
a, b=input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))


# In[2]:


#sol_2
a,b = map(int,input().split())
c = bool(a)
d = bool(b)
if c != d:
    print(True)
else:
    print(False)

