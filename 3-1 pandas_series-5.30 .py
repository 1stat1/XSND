#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd 


#  通过python的list创建pandas_series

# In[2]:


s1= pd.Series([1,2,3,4])     #此处S大写


# In[3]:


s1


# In[4]:


s1.values


# In[5]:


s1.index


# 通过np.array创建

# In[6]:


s2=pd.Series(np.arange(6))


# In[7]:


s2


# 通过python字典创建

# In[8]:


s3=pd.Series({'1':1,'2':2,'3':3})


# In[9]:


s3


# In[10]:


s3.values


# In[11]:


s3.index


# In[12]:


s4=pd.Series([3,6,9,2,5,8],index=['S','T','A','T','Y','T'])    #再用S4举例说明


# In[13]:


s4


# In[14]:


s4.values


# In[15]:


s4.index


# #对series进行操作

# In[16]:


s4['T']


# In[17]:


s4[s4<6]


# series转换成python字典

# In[18]:


s4=pd.Series([3,6,9,2,5,8],index=['1','2','3','4','5','6'])


# In[19]:


s4


# In[20]:


s4.to_dict()


# In[21]:


s4


# In[22]:


s5=pd.Series(s4.to_dict())


# In[23]:


s5


# In[24]:


s5.values


# In[25]:


s5.index


# 改变index

# In[26]:


s5.shape


# In[27]:


s5 


# In[32]:


type(s5)


# In[28]:


index_1=['a','b','c','d','e','f']


# In[42]:


s6=pd.Series(s5.values,index=index_1)


# In[43]:


s6


# In[ ]:




