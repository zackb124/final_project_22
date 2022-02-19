#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd

xl = "C:\\Users\\zachi\\Desktop\\final_project_22\\data_nov_21.xlsx"

def clean_data (xl,month):
    
    df=pd.read_excel(xl)
        #Remove unnecessary column - "removed 1"

    df.drop(columns=['Removed 1'],inplace=True)

    #Make the Category column easier to understand 

    df=df.replace({'Category' : { 'Y' : "Antisemitic", 'W' : "Non-Antisemitic", 'U' : "Anti-Zionist" }})

    
    #Fix the Summary column's text

    df = df.replace(r'\n',' ', regex=True) 

    posts_description = df["A short summary of the content- write briefly in your own words "]

    posts_description=posts_description.str.lower().str.replace('[^\w\s]','')

    #get rid of NaNs in category

    list = ["Anti-Zionist",
    "Antisemitic",
    "Non-Antisemitic"]

    df = df.loc[df['Category'] .isin(list)]

    #Convert "time stamp" to english

    df = df.rename(columns={"חותמת זמן":"Time stamp"})

        #Change the date time to the d/m/y
    from datetime import datetime
    df['Time stamp'] = pd.to_datetime(df['Time stamp']).dt.date #This function convert the date text into dt.date type
    month = 'November'


    new_df = df[pd.to_datetime(df["Time stamp"]).dt.strftime('%B') == month]


    return new_df







# In[22]:


df = df=pd.read_excel("C:\\Users\\zachi\\Desktop\\final_project_22\\data_nov_21.xlsx")
df = df.rename(columns={"חותמת זמן":"Time stamp"})

    #Change the date time to the d/m/y
from datetime import datetime
df['Time stamp'] = pd.to_datetime(df['Time stamp']).dt.date #This function convert the date text into dt.date type
user_input = 'November'


#the_user_target_date = df["Time stamp"]>df["Time stamp"].dt.strftime('%B') == user_input
#new_df = df[the_user_target_date]

new_df = df[pd.to_datetime(df["Time stamp"]).dt.strftime('%B') == user_input]


# In[ ]:




