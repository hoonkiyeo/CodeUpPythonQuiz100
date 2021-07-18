#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Last quiz

array = []
for i in range(10):
    array.append([])
    rows = input().split()
    for j in range(10):
        array[i].append(int(rows[j]))
        
i = 1
j = 1

while True:
    if array[i][j] == 2:
        array[i][j] = 9
        break
    elif i == 8 and j == 8:
        array[i][j] = 9
        break
    elif array[i+1][j] == 1 and array[i][j+1] == 1:
        array[i][j] = 9
        break
    array[i][j]=9
    
    if array[i][j+1] == 1:
        i += 1
    else:
        j += 1
        
array

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

