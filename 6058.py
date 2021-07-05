#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1
a, b = input().split()
c= bool(int(a))
d= bool(int(b))

print( not (c or d) )


# In[2]:


#sol_2
a, b = input().split()
c= bool(int(a))
d= bool(int(b))

print( c==False and d==False )


# In[3]:


#sol_3
a,b = map(int,input().split())
if bool(a) == False & bool(b) == False:
    print(True)
else:
    print(False)


# In[ ]:




