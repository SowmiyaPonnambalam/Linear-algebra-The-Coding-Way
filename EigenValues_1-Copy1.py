#!/usr/bin/env python
# coding: utf-8

# In[1]:


#to plot the obtained eigenvectors for the give matrix


# In[5]:


import numpy as np
import matplotlib.pyplot as plt

def find_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

def plot_eigenvectors(matrix, eigenvectors):
    plt.figure()
    plt.plot([0, eigenvectors[0, 0]], [0, eigenvectors[1, 0]], label='Computed Eigenvector 1', color='b')
    plt.plot([0, eigenvectors[0, 1]], [0, eigenvectors[1, 1]], label='Computed Eigenvector 2', color='g')
    plt.plot([0, given_eigenvectors[0, 0]], [0, given_eigenvectors[1, 0]], linestyle='--', label='Given Eigenvector 1', color='r')
    plt.plot([0, given_eigenvectors[0, 1]], [0, given_eigenvectors[1, 1]], linestyle='--', label='Given Eigenvector 2', color='m')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Eigenvectors')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# Example usage
matrix = np.array([[1, 6], [5, 2]])  # Example matrix
given_eigenvectors = np.array([[6, -5], [3, -2]])  # Example given eigenvectors

computed_eigenvalues, computed_eigenvectors = find_eigenvectors(matrix)
print("Computed Eigenvectors:")
print(computed_eigenvectors)

# Plot eigenvectors
plot_eigenvectors(matrix, computed_eigenvectors)



# In[ ]:






# In[ ]:





# In[ ]:




