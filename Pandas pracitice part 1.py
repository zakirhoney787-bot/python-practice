import pandas as pd
data={"employees":['Talha' ,'Ehsan','Ahmed','Zakir','Ali'],
      "spends": [200,None,180,50,140],
      "age":[24,21,23,17,23]
      }
dat={"name":['Talha' ,'Ehsan','Ahmed','Zakir','Ali'],
      "couts": [200,None,180,50,140],
      "age":[24,21,23,17,23]
      }

#make above's rows and columns
df=pd.DataFrame(data)
df2=pd.DataFrame(dat)

# df=pd.read_json('data.json',encoding='latin1')
# takes the json file in csv and print in csv without order maintaining
csvfile=df.to_csv('mini practice.csv')
# print(df,'\n')

# print(df.head())

#this tells information about each entry and column
# information=df.info()
# print(information)
# it tells us about the micro details of objects 
# details=df.describe()
# print(details)
# tell the number of rowand column in the dictionaty
# print(df.shape,'\n')
# tell column's name 
# print(df.columns)
# d=df[['employees','spends']]
# filtered file
# filtered=df[(df['spends']>80) & (df['age']>20)]
# print("these are all the under 20 < boys with >80 spends")
# print(filtered)

'''
PART 2 GET READY
'''
# ADD COLUMN
# df['mobile']=['vivo','Iphone','Realme','Oneplus','Sumsung']
df.insert(3,'mobile',['vivo','Iphone','Realme','Oneplus','Sumsung'])
# UBDATE
df.loc[3,'mobile']=='Google'
# df['spends']=df['spends']-10

#REMOVE COLUMN OR PARTICULAR
# df.drop(columns=['spends'],inplace=True)

#SHOW EMPTY PLACES
# df.isnull.sum()
# not worked 

# fill them
# df.dropna(inplace=True)
# print(df)
print()
# df.fillna((55),inplace=True)
# df['spends'] = df['spends'].fillna(df['spends'].mean())

#INTERPOLATE
# df['spends']=df['spends'].interpolate(method='linear')

#SORT
# df.sort_values(by='age',ascending=False,inplace=True)
# df.sort_values(by=['age','spends'],ascending=[True,True],inplace=True)

# df['spends']=df['spends'].mean()
# df['spends']=df['spends'].min()
# df['spends']=df['spends'].max()
# df['spends']=df['spends'].sum()

#GROUPING AND AGGREGATING                 not worked
# df.groupby('age')['spends'].sum()
df.groupby['spensds','age']['spends'].sum()

df.merge(df,df2)

print(df)
