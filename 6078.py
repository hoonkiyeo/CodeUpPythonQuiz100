#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1

while True:
    letter = input()
    if letter != 'q':
        print(letter)
        continue
    if letter == 'q':
        print(letter)
        break


# In[2]:


#sol_2

while True:
    letter = input()
    print(letter)
    if letter == 'q':
        break

