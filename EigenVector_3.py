#!/usr/bin/env python
# coding: utf-8

# In[1]:


#to find the inverse of the matrix

import numpy as np
M=np.array([[0,1,2],[1,0,3],[4,-3,8]])
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
m_inv=np.linalg.inv(M)
print(m_inv)
for i in range(len(M)):
   for j in range(len(m_inv[0])):
       # iterate through rows of Y
       for k in range(len(m_inv)):
           result[i][j] += M[i][k] * m_inv[k][j]

for r in result:
   print(r)


# In[ ]:




