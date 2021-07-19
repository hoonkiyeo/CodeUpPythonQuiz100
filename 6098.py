#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Last quiz

#sol_1
array = []
for i in range(10):
    array.append([])
    rows = input().split()
    for j in range(10):
        array[i].append(int(rows[j]))
        
i = 1
j = 1

while True:
    array[i][j] = 9
    if array[i][j+1] == 1:
        i += 1
    else:
        j += 1
    if array[i][j+1] == 1 and array[i+1][j] == 1:
        array[i][j] = 9
        break
    elif array[i][j] == 2:
        array[i][j] = 9
        break

for i in array:
    for j in i:
        print(j, end = ' ')
    print()        
#input
'''
1 1 1 1 1 1 1 1 1 1
1 0 0 1 0 0 0 0 0 1
1 0 0 1 1 1 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 1 0 1 0 1
1 0 0 0 0 1 2 1 0 1
1 0 0 0 0 1 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
'''
#output
'''
1 1 1 1 1 1 1 1 1 1
1 9 9 1 0 0 0 0 0 1
1 0 9 1 1 1 0 0 0 1
1 0 9 9 9 9 9 1 0 1
1 0 0 0 0 0 9 1 0 1
1 0 0 0 0 1 9 1 0 1
1 0 0 0 0 1 9 1 0 1
1 0 0 0 0 1 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
'''


# In[22]:


#sol_2

def ant_route(size):
    array = []
    for i in range(size):
        array.append([])
        rows = input().split()
        for j in range(size):
            array[i].append(int(rows[j]))
            
    
    i = 1
    j = 1
    
    while True:
        array[i][j] = 9 # 0 -> 9
        if array[i][j+1] == 1:
            i += 1
        else:
            j += 1
        if array[i][j+1] == 1 and array[i+1][j] == 1:
            array[i][j] = 9
            break
        elif array[i][j] == 2:
            array[i][j] = 9
            break
    for i in array:
        for j in i:
            print(j, end = ' ')
        print()
        
ant_route(10)

#input
'''
1 1 1 1 1 1 1 1 1 1
1 0 1 0 1 0 1 0 1 0
1 0 1 0 1 0 1 0 1 0
1 0 1 0 1 0 1 0 1 0
1 0 0 0 0 0 0 2 1 0
1 0 1 0 1 0 1 0 1 0
1 0 1 0 1 0 1 0 1 0
1 0 1 0 1 0 1 0 1 0
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
'''
#output
'''
1 1 1 1 1 1 1 1 1 1 
1 9 1 0 1 0 1 0 1 0 
1 9 1 0 1 0 1 0 1 0 
1 9 1 0 1 0 1 0 1 0 
1 9 9 9 9 9 9 9 1 0 
1 0 1 0 1 0 1 0 1 0 
1 0 1 0 1 0 1 0 1 0 
1 0 1 0 1 0 1 0 1 0 
1 1 1 1 1 1 1 1 1 1 
1 1 1 1 1 1 1 1 1 1
'''


# In[ ]:




