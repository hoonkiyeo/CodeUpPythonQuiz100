#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1

c=input()
i = ord('a')
c = ord(c)

while i<=c:
    print(chr(i), end=' ')
    i+=1


# In[1]:


#sol_2

end = ord(input())
start = ord('a')

while True:
    print(chr(start), end = " ")
    start += 1
    if start > end:
        break

