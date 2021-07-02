#!/usr/bin/env python
# coding: utf-8

# In[1]:


a, b, c = input().split()
a=int(a)
b=int(b)
c=int(c)
hap=a+b+c
avg=hap/3
print(hap, format(avg, ".2f"))


# In[4]:


a,b,c = map(int, input().split())
total_sum = a+b+c
avg = total_sum / 3
print(total_sum, format(avg, ".2f"), sep = " ")


# In[ ]:




