#!/usr/bin/env python
# coding: utf-8

# In[2]:


#sol_1
a, b, c = input().split()

a=int(a)
b=int(b)
c=int(c)

if a%2==0:
    print(a)
    
if b%2==0:
    print(b)
    
if c%2==0:
    print(c)


# In[13]:


#sol_2

a,b,c = map(int,input().split())


if a % 2 == False:
    print(a)
if b % 2 == False:
    print(b)
if c % 2 == False:
    print(c)
    

