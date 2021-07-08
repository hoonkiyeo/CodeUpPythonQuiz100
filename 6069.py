#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1

a = input()

if a=='A':
    print("best!!!")
elif a=='B':
    print("good!!")
elif a=='C':
    print("run!")
elif a=='D':
    print("slowly~")
else:
    print("what?")


# In[9]:


#sol_2

a = input()

print({"A":"best!!!", "B":"good!!", "C":"run!", "D":"slowly~"}.get(a,"what?"))


# In[8]:


#sol_3
a = input()

evaluation_dic = {"A":"best!!!", "B":"good!!", "C":"run!", "D":"slowly~"}

print(evaluation_dic.get(a, "what?"))

