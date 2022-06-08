#!/usr/bin/env python
# coding: utf-8

# array的创建及访问

# In[1]:


import numpy as np


# In[2]:


list_1=[1,2,6,9]


# In[3]:


list_1


# In[4]:


array_1=np.array(list_1)


# In[5]:


array_1


# In[6]:


list_2=[10,13,54,66]


# In[15]:


array_2=np.array([list_1,list_2])


# In[16]:


array_2


# In[17]:


array_2.shape


# In[19]:


array_2.size


# In[20]:


array_2.dtype


# In[25]:


array_3=np.array([[1.2,2,3.6,10],[2,33.2,6,1.2]])


# In[26]:


array_3.dtype


# In[29]:


array_4=np.arange(1,12,3)


# In[30]:


array_4


# In[32]:


np.zeros([2,3])


# In[33]:


np.eye(3)


# In[35]:


np.eye(3).dtype


# In[38]:


a=np.array([[1,3,5],[2,4,6],[7,8,9]])


# In[39]:


a


# In[40]:


a[2][1]


# In[43]:


a[2,1]


# In[47]:


a[:2,1:]


# In[ ]:




