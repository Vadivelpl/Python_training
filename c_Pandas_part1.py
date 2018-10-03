# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 15:27:32 2018

@author: PL Vadivel (pv48452)
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

############################# PANDAS SERIES ###################################
#series
labels=['a','b','c']
my_data=[10,20,30]
arr=np.array(my_data)

dd=pd.Series(data=my_data,index=labels) #series is very similar to numpy arrays except it has an index and index can be labelled in the way we want and not just integers
dd=pd.Series(my_data,labels) #if parameters are in the same order, then you can just pass the parameters name
dd=pd.Series(arr,labels) #series can also be created on top of numpy array. if index is not given, default index will be 0,1,2,....
print(dd[0],dd['a'])

d={'b':20,'a':5,'c':30} # Dictionary
ee=pd.Series(d) #series can also be formed from dictionary where it automatically understands key of dict to be the index 
dd+ee #this will match the index and add the value. if one index is not present in other series, it will return null. array will add only elements in the same order.


############################# PANDAS DATAFRAME ###################################
#Read from files
Train = pd.read_csv('C:/Vadivel/Analytics/Python-learning/Citi/titanic_train.csv') #back slash in path - within single quotes
Inp = pd.read_excel("Filename.xlsx",sheetname='Sheet1') #sheetname
data = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html') #returns list of tables in that page. Requires html5lib

#write to files
Train.to_csv('Filename.csv',index=False) ### write to csv 
Train.to_excel("Filename.xlsx",sheet_name='Sheet1') #sheet_name

#creating dataframes
df=pd.DataFrame() #creating an empty dataframe 
X = np.arange(1,11)
df = pd.DataFrame(X,columns=['Unique_Id']) #X is an numpy array. creating dataframe from array with column name
new_df = pd.DataFrame(columns=Train.columns) #creating an dataframe with column names from another df
df=pd.DataFrame(np.random.randn(5,4),['A','B','C','D','E'],['W','X','Y','Z']) #data followed by rowlabels followed by columlabels

# Initial exploratory analysis
Train.index #gives the index details of that dataframe
Train.shape   #displays the dimension of the dataframe
Train.columns #displays all the column names in the dataframe
Train.dtypes  #displays types of all columns
Train.head()  #displays top 5 rows
Train.head(n=10) #specify number of rows required
Train.info()  #columns, types, how many non null values
Train.describe() #gives standards statistics on numerical clumns, top,freq for categorical columns
Train[["PassengerId","Fare"]].describe() #describe only selected columns
Train['Embarked'].value_counts() #value counts will work only on pandas series. so you will have to select only one column
Train['Embarked'].value_counts(normalize=True)
len(Train) #No of rows

Train['Survived'].sum()
Train.Age.mean() #mean
Train.Age.std() #Standard deviation
Train.Age.max() # Age of oldest person in titanic
Train.Embarked.unique()
Train.Embarked.nunique()
Train['Age'].quantile(0.90) #90th percentile
for col in Train.columns:
    print(col,Train[col].nunique())
pd.crosstab(Train.Sex,Train.Survived)
plt.hist(Train.Age, bins=16, range =(0,80)) #histogram
help(Train['Embarked'].value_counts())
help(pd.Series().value_counts())

#creating new columns
Train['relatives']=Train['Parch']+Train['SibSp'] #creating new columns on the go. no need to predefine new column names
Train['name_sex'] = Train['Name']+"_"+Train['Sex'] #concatenating two string columns
Train['id_survived'] = Train['PassengerId'].map(str)+"_"+Train['Survived'].map(str) #concatenating two number columns. could be used for say year_month
Train['Pclass'] = Train['Pclass'].astype('category') #changing datatype of a column

#dropping columns
Train.drop('id_survived',axis=1) #Drops the column and displays in console, but dataframe is not updated
Train.drop('id_survived',axis=1,inplace=True) # Drops the column and updates the dataframe
Train = Train.drop('name_sex',axis=1) #Another way to drop and update columns. default axis is 0 which is index(row index). To get column use axis=1. shape method will return (row,column) hence row is 0th axis and column is 1st axis
Train1 = Train.drop(['relatives','Embarked'],axis=1) #Dropping a list of columns
Train1 = Train.select_dtypes(exclude=['object']) #removing all columns which are of object datatype.

# Slicing and dicing
Passengerid = Train['PassengerId'] #fetching a single column. df.W can also be used but this is not prefered as it will confuse with methods in dictionary
Passengerid_df = Train[['PassengerId']] #Creates a single column data frame if put inside double brackets
id_fare_df = Train['PassengerId','Fare'] #this will return error. For more than one column , you have to send column names only as list
id_fare_df = Train[['PassengerId','Fare']] #this is right representation - double brackets for more than one columns
Train.PassengerId[0:10] #first ten rows of one column in dataframe. Not recommended since it will be confusion if Survived is variable or method/function
Train[0:10][['PassengerId','Fare']] # Display two columns, continuous rows
Train[-5:] #accessing last five rows
Train[Train.columns[-3:]] # Accessing last 3 columns
Train.loc[[0,2]] #fetching entire 0th and 2nd row using loc. In loc you have to use the index name
Train.loc[[0,2],['PassengerId','Fare']] #fetching two specific columns from 0th and 2nd row using loc
Train.loc[2:5,['PassengerId','Fare']] #selecting continous rows using loc. index 2 till 5. No stop-1
Train.loc[:,['PassengerId','Fare']] #fetching specific columns for all rows. This is similar to Train[['PassengerId','Fare']]
Train.loc[0,'Fare'] #fetching a value in a specific row and a specific column. Single brackets - since it returns a value and not a list
Train.iloc[0:2,0:2] #iloc also requires square brackets. Accessing by row index number and column index number together
Train.iloc[:,2] #all rows, 3rd column or column with index 2
Train.iloc[0,3] #0th row and 3rd column
