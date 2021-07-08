#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sol_1
score = int(input())

if score >= 90:
    print("A")
elif score >= 70:
    print("B")
elif score >= 40:
    print("C")
else:
    print("D")


# In[4]:


#sol_2
n = int(input())

def grading_scale(grade):
    if grade >= 90:
        score = "A"
    elif grade >= 70:
        score = "B"
    elif grade >= 40:
        score = "C"
    else:
        score = "D"
        
    print(score)

grading_scale(n)

