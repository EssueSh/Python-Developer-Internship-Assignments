#!/usr/bin/env python
# coding: utf-8

# In[3]:


Year=int(input('Enter year'))
if Year % 400 == 0:
    print('Year:',Year,'is leap year')
elif Year % 100 == 0:
    print('Year:',Year,'is not a leap year')
elif Year % 4 == 0:
    print('Year:',Year,'is leap year')
else:
    print('Year:',Year,'is not a leap year')


# In[ ]:




