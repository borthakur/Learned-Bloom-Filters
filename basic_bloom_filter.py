#!/usr/bin/env python
# coding: utf-8

# In[3]:


# In[4]:




# In[12]:


from bitarray import bitarray
import mmh3
import random
import numpy as np


# In[6]:


bit_array = bitarray(10)
bit_array.setall(0)

b1 = mmh3.hash(str(654), 41) % 10 
bit_array[b1] = 1
b2 = mmh3.hash(str(654), 42) % 10 
bit_array[b2] = 1
b1 = mmh3.hash(str(654), 41) % 10
b2 = mmh3.hash(str(654), 42) % 10


# In[7]:


if bit_array[b1] == 1 and bit_array[b2] == 1:
    print("Probably in set")
else:
    print("Definitely not in set")


# In[8]:


class BloomFilter:
    
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
        
    def add(self, num):
        for seed in range(1,self.hash_count+1):
            result = mmh3.hash(str(num), seed) % self.size
            self.bit_array[result] = 1
            
    def lookup(self, num):
        for seed in range(1,self.hash_count+1):
            result = mmh3.hash(str(num), seed) % self.size
            if self.bit_array[result] == 0:
                return False
        return True


# In[9]:


bf = BloomFilter(1000,3)

bf.add(51)
bf.add(432)
bf.add(11)
bf.add(2875)

print(bf.lookup(234))
print(bf.lookup(51))
print(bf.lookup(2875))
print(bf.lookup(2876))


# In[13]:


data=np.empty(100,dtype=int)
for i in range(0,100):
    data[i]=random.randint(0, 100000000)
for j in range(0,50):
    bf.add(data[j]);


# In[14]:


print(bf.lookup(data[60]))
print(bf.lookup(data[25]))


# In[ ]:

'''Function inputs bloom filter, number array and number of entries from number array and outputs -1 if there is false negative, and otherwise false positive rates'''
def fpr(bf,nums,pos):
    for i in range(pos):
        if(bf.lookup(nums[i])==False):
            return -1
    count = 0
    for i in range(pos,len(nums)):
        if(bf.lookup(nums[i])==True):
            count+=1
    return count/len(nums)

print(fpr(bf,data,50))

# %%
