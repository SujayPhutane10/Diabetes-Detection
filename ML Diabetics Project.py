#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# In[2]:


get_ipython().run_line_magic('cd', '')


# In[3]:


get_ipython().run_line_magic('cd', 'Downloads')


# In[4]:


df=pd.read_csv("diabetes.csv")


# In[5]:


df


# In[6]:


non_zero_mean= df.loc[df["SkinThickness"] !=0, "SkinThickness"].mean()


# In[7]:


df["SkinThickness"]=df["SkinThickness"].replace(0,non_zero_mean)


# In[8]:


df


# In[9]:


X=df[["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"]]


# In[10]:


y=df["Outcome"]


# In[11]:


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)


# In[12]:


tree_classifier=DecisionTreeClassifier()


# In[13]:


tree_classifier.fit(X_train,y_train)


# In[15]:


y_pred=tree_classifier.predict(X_test)
y_pred


# In[16]:


accuracy=accuracy_score(y_test,y_pred)
accuracy*100


# In[21]:


Pregnancies=int(input("Enter the Number of Pregnancies You Had:-"))   #Pregnancy number that had occur
Glucose	=int(input("Enter Your Blood Glucose Concentration:-"))       #Glucose is the main sugar in your blood
BloodPressure=int(input("Enter Your Blood Pressure:-"))      #A person with diabetes should have a blood pressure (BP) target of less than 140/90 mm Hg. 
SkinThickness=int(input("Enter Your SkinFold Thickness:-"))
Insulin=float(input("Enter Your Body Insulin Level:-"))  #Insulin is a hormone that helps the body use glucose (sugar) for energy.
BMI=float(input("Enter Your Body Mass Index :-"))      #Body mass index (BMI) is a measure of a person's weight relative to their height.
DPF=float(input("Enter Your DiabetesPedigreeFunction:-"))  #a function that scores diabetes based on family history
Age=int(input("Enter Your Age:-"))

y_pred = tree_classifier.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DPF,Age]])
print(y_pred)


# In[ ]:




