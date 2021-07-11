#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1

sum = 0
n = int(input())

for i in range(1, n+1):
    if i % 2 == 0:
        sum += i
    else:
        continue
        
print(sum)


# In[2]:


#sol_2

sum = 0
start = 2
n = int(input())

while start <= n:
    
    if start % 2 == 0:
        sum += start
    start += 1
    
print(sum)

