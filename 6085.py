#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1

w,h,b = map(int, input().split(" "))
result = w*h*b/8/1024/1024
byte = "MB"
print(format(result, ".2f"), byte, sep = " ")

