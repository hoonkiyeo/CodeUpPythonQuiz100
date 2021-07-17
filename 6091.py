#!/usr/bin/env python
# coding: utf-8

# In[15]:


#sol_1

a,b,c = map(int, input().split())

d = 1

while d % a != 0 or d % b != 0 or d % c != 0:
    d += 1
    
print(d)

#input
'''
3 7 9
'''
#output
'''
63
'''


# In[13]:


#sol_2

def lcm_calculator():
    a,b,c = map(int,input().split())
    i = 1
    
    while True:
        if (i % a == i % b == i % c == 0):
            break
        else:
            i += 1
    return i

print(lcm_calculator())
#input
'''
1 1 9
'''
#output
'''
9
'''

