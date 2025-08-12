#!/usr/bin/env python
# coding: utf-8

# In[111]:


import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# In[112]:


car = pd.read_csv(r"C:\Users\Muthu\Downloads\archive (18)\cardekho.csv")


# In[113]:


car.head()


# In[114]:


import re


# In[115]:


def extract_brand_car(full_name):
    words = full_name.split()
    
    # Handle 2-word brand names
    two_word_brands = ['land rover', 'force motors', 'rolls royce', 'ashok leyland', 'isuzu motors', 'mini cooper', 'mahindra renault']
    full_name_lower = full_name.lower()
    brand = ''
    for bw in two_word_brands:
        if full_name_lower.startswith(bw):
            brand = ' '.join(words[:2])
            rest = words[2:]
            break
    else:
        brand = words[0]
        rest = words[1:]
    
    # Extract car name: take up to 2 words that are capitalized and not purely numeric or specifiers
    car_name_parts = []
    for word in rest:
        if re.fullmatch(r'[A-Za-z0-9]+', word) and not re.fullmatch(r'(VDI|LDI|ZDI|VXI|ZXI|EXI|TXI|LS|LT|LX|SX|S|E|SE|BSIII|BSIV|BSVI|[0-9]+|MT|AT|CVT|AMT|TDI|MPI|CRDI|D|P|X)', word.upper()):
            car_name_parts.append(word)
        else:
            break
    car_name = ' '.join(car_name_parts)
    
    return pd.Series([brand.title(), car_name])

# Apply updated logic
car[['Car_Brand', 'Car_Name']] = car['name'].apply(extract_brand_car)


# In[116]:


car.drop(columns=['name'],inplace=True)


# In[117]:


car.head()


# In[118]:


car.shape


# In[119]:


car.info


# In[120]:


car.isnull().sum()


# In[121]:


car.dropna(inplace=True)
car.shape


# In[122]:


car.duplicated().sum()


# In[123]:


car.drop_duplicates(inplace=True)
car.shape


# In[124]:


car.info()


# In[125]:


for col in car.columns:
    print('UNIQUE VALUES-'+col)
    print(car[col].unique())
    print('--------------------------------\n')


# In[126]:


car['mileage(km/ltr/kg)'] = car['mileage(km/ltr/kg)'].astype('object')


# In[127]:


car['engine'] = car['engine'].astype('object')


# In[128]:


car['seats'] = car['seats'].astype('int')


# In[129]:


def clean_data(value):
    value=value.strip()
    if value=="":
        value = 0
    return float()


# In[130]:


car['max_power']=car['max_power'].apply(clean_data)


# In[132]:


car['fuel']=car['fuel'].replace(['Diesel','Petrol','LPG','CNG'],[1,2,3,4])


# In[133]:


car['seller_type']=car['seller_type'].replace(['Individual','Dealer','Trustmark Dealer'],[1,2,3]).astype(int)


# In[134]:


car['transmission'] = car['transmission'].replace(
    dict(zip(car['transmission'].unique(), range(1, len(car['transmission'].unique()) + 1)))
).astype(int)


# In[135]:


car.head()


# In[136]:


car['owner'] = car['owner'].replace(
    dict(zip(car['owner'].unique(), range(1, len(car['owner'].unique()) + 1)))
).astype(int)


# In[137]:


car['Car_Brand'] = car['Car_Brand'].replace(
    dict(zip(car['Car_Brand'].unique(), range(1, len(car['Car_Brand'].unique()) + 1)))
).astype(int)


# In[138]:


car.info()


# In[139]:


car['Car_Name'] = car['Car_Name'].replace(
    dict(zip(car['Car_Name'].unique(), range(1, len(car['Car_Name'].unique()) + 1)))
).astype(int)


# In[140]:


car


# In[161]:


car.reset_index(inplace=True)


# In[163]:


car.drop(columns=['index'],inplace=True)


# In[165]:


car.drop(columns=['level_0'], inplace=True)
car


# In[166]:


input_data=car.drop(columns=['selling_price'])
output_data=car['selling_price']


# In[167]:


x_train, x_test, y_train, y_test = train_test_split(input_data, output_data, test_size=0.2)


# In[168]:


model = LinearRegression()


# In[169]:


model.fit(x_train, y_train)


# In[170]:


predict = model.predict(x_test)


# In[171]:


predict


# In[172]:


x_train.head(1)


# In[203]:


input_data_model = pd.DataFrame([['2017','400000','1','1','1','1','22.9','1248.0','0.0',	'5','1','5']],
                                columns=['year','km_driven','fuel','seller_type','transmission','owner','mileage(km/ltr/kg)','engine','max_power','seats','Car_Brand','Car_Name'])


# In[204]:


input_data_model


# In[205]:


model.predict(input_data_model)


# In[ ]:




