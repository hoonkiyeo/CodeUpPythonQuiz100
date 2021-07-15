#!/usr/bin/env python
# coding: utf-8

# In[2]:


#sol_1

h,w = map(int, input().split())
n = int(input())
array = [[0 for col in range(w)] for row in range(h)]

for i in range(n):
    l,d,x,y = map(int,input().split())
    if d == 0:
        for j in range(l):
            array[x-1][y-1+j] = 1
            
    else:
        for j in range(l):
            array[x-1+j][y-1] = 1
            
array

for i in array:
    for j in i:
        print(j, end = ' ')
    print()

#input
'''
5 5
3
2 0 1 1
3 1 2 3
4 1 2 5
'''
#output
'''
1 1 0 0 0
0 0 1 0 1
0 0 1 0 1
0 0 1 0 1
0 0 0 0 1
'''

