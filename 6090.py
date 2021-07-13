#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1

a,m,d,n = map(int, input().split())

start = a

for i in range(1,n):
    
    start = start*m
    start = start+d
    
print(start)


# In[4]:


#sol_2

a,m,d,n = map(int, input().split())
count = 1

while count < n:
    count += 1
    a = a*m+d
    
print(a)

