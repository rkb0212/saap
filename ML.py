#!/usr/bin/env python
# coding: utf-8

# # 11sept,23

# In[3]:


import sklearn


# In[4]:


from sklearn import tree   #1:orange , 0:apple
features = [[140,1],[130,1],[150,0],[170,0]]
labels = [0,0,1,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
print(clf.predict([[150,0]]))


# In[ ]:




