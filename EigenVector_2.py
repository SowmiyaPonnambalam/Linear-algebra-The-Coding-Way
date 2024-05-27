#!/usr/bin/env python
# coding: utf-8

# In[1]:


#to find eigenvalues and eigen vectors and to find their dependencies to distinct eigen values

import numpy as np
import sympy

A = np.array([[2, 1,0],
              [1, 3,-1],
             [0,-1,4]])
eigenvalues, eigenvectors = np.linalg.eig(A)
eigenvectors_matrix = np.column_stack(eigenvectors)
eigenvectors_sympy = sympy.Matrix(eigenvectors_matrix)
rref, _ = eigenvectors_sympy.T.rref()
rank = rref.rows
if rank == len(eigenvalues):
    print("Eigenvectors corresponding to distinct eigenvalues are independent.")
else:
    print("Eigenvectors corresponding to distinct eigenvalues are dependent.")


# In[ ]:





# In[ ]:




