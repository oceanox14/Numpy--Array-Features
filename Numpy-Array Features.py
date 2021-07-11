#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.array([1,2,3,4])


# In[3]:


type(a)


# In[11]:


np.array([1.2, 3, 5.0])


# In[12]:


np.array([1.2, 3, 4], dtype="int")


# **#sifirdan array oluşturmak**

# In[13]:


import numpy as np


# In[14]:


np.zeros(10)


# In[15]:


np.zeros(10, dtype = int)


# In[17]:


np.ones((5,3), dtype = int)


# In[18]:


np.full((5,3),5, dtype = float)


# In[19]:


np.arange(0,31, 3)


# In[20]:


np.linspace(5,6,10)


# In[21]:


np.random.normal(10, 3, (3,4))


# np.random.randint(0,10,(3,3))

# # **_Özellikler_**

# * ndim: boyut sayısı
# * shape: boyut bilgisi
# * size: top eleman sayısı
# * dtype: aray veri tipi

# In[27]:


import numpy as np


# In[28]:


np.random.randint(10, size = 10)


# In[29]:


a = np.random.randint(10, size = 10)


# In[30]:


a.ndim


# In[31]:


a.shape


# In[32]:


a.size


# In[33]:


a.dtype


# In[35]:


b = np.random.randint(10, size = (3,5))


# In[36]:


b


# In[38]:


b.ndim


# In[39]:


b.shape


# In[40]:


b.dtype


# In[41]:


b.size


# # Reshapping

# In[45]:


np.arange(1,10)


# In[46]:


np.arange(1,10).reshape((3,3))


# In[47]:


a = np.arange(1,10)


# In[48]:


a


# In[49]:


a.ndim


# In[54]:


b = a.reshape((1,9))


# In[55]:


b


# In[56]:


b.ndim


# In[58]:


b.shape

