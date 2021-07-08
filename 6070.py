#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1
a=int(input())
if a//3==1:
    print("spring")
elif a//3==2:
    print("summer")
elif a//3==3:
    print("fall")
else:
    print("winter")


# In[12]:


#sol_2 (function)
a = int(input())

def season(month):
    if month > 12:
        print("wrong index")
        print("month must be 1 to 12")
        print("try again")
    elif month // 3 == 1:
        print("spring")
    elif month // 3 == 2:
        print("summer")
    elif month // 3 == 3:
        print("fall")
    elif month // 3 == 4 or month // 3 == 0:
        print("winter")
        
season(a)
        
    

