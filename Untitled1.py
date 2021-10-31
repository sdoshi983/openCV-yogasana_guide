#!/usr/bin/env python
# coding: utf-8

# In[7]:


# python program to search element from list

# 1
l=[1,2,3,4,5,6,7,8,9,10]
n=int(input('Enter value that you want to search from a list : '))

flag=0
for i in l:
    if n==i:
        flag=1
        break
        
if flag==1:
    print('Yes',n,'found in list', 'at index : ', i-1)
else:
    print('No',n,'not found in list')
	
#-------------------------------------------------------------------------------------------------
print('\n\n')
# 2
L=[2,58,95,999,65,32,15,1,7,45]
n=int(input("Enter the number to be searched : "))
found=0
for x in L:
    if x==n:
        print("Item found at the Index : ",L.index(n))
        found=1
if found==0:
    print("Item not found in list")


# In[ ]:





# In[ ]:




