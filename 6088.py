#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1

a,d,n = map(int, input().split())

if d == 0 and a == 1:
    print(1)
elif d == 0:
    print(0)
else:
    lst = list(range(a, d*n, d))
    print(lst[n-1])


# In[3]:


#sol_2

a,d,n = map(int,input().split())

for i in range(2, n+1):
    a += d

print(a)


# In[ ]:


#sol_3

a,d,n = map(int,input().split())
count = 1
while count < n:
    count += 1
    a += d
    
print(a)

