#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1

n = int(input())
sum = 1

for i in range(1, n):
    sum += i
    if sum == n:
        i = i
    elif sum < n:
        i = i+1
    elif sum > n:
        break
        
print(i)


# In[4]:


#sol_2

n = int(input())

s = 0
t = 0
while s<n :
    t += 1
    s += t
    
print(t)

