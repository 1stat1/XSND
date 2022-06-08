#!/usr/bin/env python
# coding: utf-8

# numpy中自带的input和output

# In[ ]:


import pickle


# In[1]:


import numpy as np


# In[2]:


x=np.arange(20)


# In[3]:


x


# In[24]:


#f=open('x.pkl','wb')


# In[ ]:


#pickle.dump(x,f)


# In[29]:


get_ipython().system('ls')


# 写入硬盘

# In[33]:


np.save('one_array',x)


# In[37]:


get_ipython().system('ls')


# 加载刚才保存的array

# In[39]:


np.load('one_array.npy')


# In[40]:


y=np.arange(6)


# In[41]:


y


# 压缩保存2个array

# In[42]:


np.savez('two_array.npz',a=x,b=y)


# In[43]:


ls


# 加载压缩的2个array

# In[44]:


c=np.load('two_array.npz')


# In[47]:


c['a']


# In[48]:


c['b']

