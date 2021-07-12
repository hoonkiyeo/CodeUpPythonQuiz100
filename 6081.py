#!/usr/bin/env python
# coding: utf-8

# In[1]:


#6081

#sol_1
n = input()
base = 16 #base
hexa = int(n, base) #hexadecimal

for i in range(1,16):
    a = hexa * i
    print("{0}*{1:X}={2:X}".format(n, i, a))


# In[2]:


#sol_2

n = int(input(), 16)

for i in range(1, 16) :
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

