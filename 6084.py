#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1

h,b,c,s = map(int, input().split(" "))
result = h*b*c*s/8/1024/1024
byte = "MB"
print(format(result, ".1f"), byte, sep = " ")


# In[2]:


#sol_2

h,b,c,s = map(int,input().split())
print(round(h*b*c*s/8/1024/1024, 1), "MB")

