#!/usr/bin/env python
# coding: utf-8

# 快速创建数组

# In[2]:


import numpy as np


# In[3]:


np.random.randn(8)


# In[8]:


np.random.randint(100,size=(3,3))


# In[10]:


np.random.randint(10,size=6).reshape(2,3)


# 数组运算

# In[11]:


a=np.random.randint(10,size=6).reshape(2,3)


# In[12]:


b=np.random.randint(10,size=6).reshape(2,3)


# In[20]:


a


# In[19]:


b


# In[17]:


a+b


# In[21]:


a-b


# In[22]:


a*b


# In[23]:


a/b


# 创建矩阵

# In[24]:


np.mat([[1,2,3],[7,8,9]])


# In[25]:


np.mat(a)


# 矩阵的运算

# In[26]:


A=np.mat(a)


# In[27]:


B=np.mat(b)


# In[28]:


A


# In[29]:


B


# In[30]:


A+B


# In[31]:


A-B


# In[33]:


a=np.mat(np.random.randint(10,size=6).reshape(2,3))
b=np.mat(np.random.randint(10,size=6).reshape(3,2))


# In[34]:


a


# In[35]:


b


# #矩阵相乘必须是双方行列数互换后对应，如a是2*3，b就要3*2

# In[36]:


a*b


# array常用函数

# In[37]:


c=np.random.randint(10,size=42).reshape(7,6)


# In[38]:


np.unique(c)


# In[39]:


c


# 列求和

# In[41]:


sum(c)


# 第二行求和

# In[44]:


sum(c[1])


# 第二列求和

# In[55]:


sum(c[:,1])


# 求最大/小值

# In[56]:


c.max()


# In[57]:


c.min()


# In[61]:


max(c[3])     #第四行最大值


# In[67]:


max(c[:,3])   #第4列最大值

