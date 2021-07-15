#!/usr/bin/env python
# coding: utf-8

# In[27]:


#sol_1

d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)
        
n = int(input())

for i in range(n):
    x,y = input().split()
    d[int(x)][int(y)] = 1
    
for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end = ' ')
    print()
    
'''
5
1 1
2 2
3 3
4 4
5 5
'''
    
'''
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
'''


# In[12]:


#sol_2

def coordinate_system(num):
    array = [[0] * num for _ in range(num)]
    n = int(input())
    
    for i in range(n):
        a = list(map(int, input().split()))
        array[a[0]][a[1]] = 1
    for x in range(1, len(array)): #rows
        for y in range(1, len(array[0])): #columns
            print(array[x][y], end = " ")
        print()
        
coordinate_system(20)

