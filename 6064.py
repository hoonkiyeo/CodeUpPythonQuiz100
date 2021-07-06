#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

d = a if a<b else b
e = d if d<c else c

print(e)


# In[5]:


#sol_2
a,b,c = map(int,input().split())

if a < b:
    if a < c:
        print(a)
    elif c > a:
        print(c)
elif a > b:
    if b < c:
        print(b)
    else:
        print(c)


# In[ ]:




