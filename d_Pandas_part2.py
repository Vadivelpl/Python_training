# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 07:45:54 2018

@author: PL Vadivel (pv48452)
"""
import pandas as pd
Train = pd.read_csv('C:/Vadivel/Analytics/Python-learning/Citi/titanic_train.csv')

#Conditional Row selection
Train['Survived']>0 # Returns a boolean dataframe of true or false
Train[Train['Survived']>0] # This will retain only rows where inside condition returned true. inside condition will return boolean series. for whichever row the series value is false, that row will be dropped
Train[(Train['Survived']>0) & (Train['Pclass']==1)] #'and' will work only for individual value, will not work for list. so use '&'. Similarly use '|' instead of 'or' for series comparison
Train[(Train['Survived']>0) & (Train['Pclass']==1)][['PassengerId','Name']] #conditional row selection and selecting specific columns
Train1 = Train[Train['Embarked'].isin(['C','S'])]
Train[Train['Survived']>0]['Sex'].value_counts()
len(Train[Train['Survived']>0]) #number of people who survived
Train[Train['Survived']==1]['Age'].mean() #Average age of people who survived
Train[-Train.Age.isnull() & Train.Survived==0][0:5][['Age','Sex']] #showing first five rows of members whose age is known and not survived - only two columns
Train[Train.Survived==1 & Train.Sex.str.startswith('m')]['Age'].mean() # Average age of male people who survived

#Groupby, Agg
Train.groupby(['Sex'])['Survived'].mean()
Train1 = Train.groupby(['Sex'])[['Survived']].mean()
type(Train.groupby(['Sex'])['Survived'].mean())
type(Train.groupby(['Sex'])[['Survived']].mean())
Train1.reset_index(inplace=True) #old index will become a new column
Train1.reset_index(inplace=True, drop=True) #old index will be deleted
Train.groupby(['Survived'])[['PassengerId']].nunique() #Number of unique passengerids who survived
Train.groupby(['Survived'])[['PassengerId']].count() #count and nunique will return same value if there are no duplicates
Train.groupby(['Sex']).agg({'Age':[min,max,sum],      # find the min,max and sum of the age for each group
                                     'Pclass': 'count', # find the number of passenger class entries
                                     'Name': 'first'})    # get the first name per group

#Handling NAs
Train.info()
Train1 = Train.copy() #without copy function, train1 will only reference train. any change to train1 will reflect in train also
Train1['Age'].fillna(value=Train1['Age'].mean(),inplace=True)
Train1.info()
Train1 = Train.copy()
Train1['Age'].fillna(value=20,inplace=True)
Train.dropna() #removes all rows where any column is NA
Train.Embarked.dropna() #removes rows where 'Embarked' column is NA
Train[['Embarked','Age']].dropna() #drops rows which has na values in any of the two columns
Train.dropna(axis=1,how="any") #removes columns which has NA in any row. default axis is 0 which means row
Train.dropna(axis=1,how="all") #removes columns which has NA in all row

#Handling duplicates
Train.drop_duplicates() #if entire row is duplicate
Train['PassengerId'].drop_duplicates() #remove if more than one row has same passengerId

#Column names
Train1.rename(columns={'Pclass':'passengerclass'},inplace=True) #changing column names
Train1.columns=['Id', 'Survived', 'Class', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'] #assigning all column names

#sort
Train1 = Train1.sort_values(by=['Survived', 'Age'], ascending=[True, False]) ### sort 
Train1.sort_values(by=['Survived', 'Age'], inplace=True) #default is ascending=True

#concat , append
Train1 = Train[0:300] ; Train2 = Train[300:500] ; Train3 = Train[500:]
Train_final = pd.concat([Train1, Train2,Train3],axis=0)
Train_final = Train1.append([Train2,Train3]) # This line and previous line return same results
#for row concatenation, column names should be same
Train1 = Train[Train.columns[:6]] ; Train2 = Train[Train.columns[6:]]
Train_final = pd.concat([Train1, Train2],axis=1)
#for column concatenation, row index should be same in the dataframes to be concatenated

#Merge, join
Sex_surv = Train.groupby('Sex')[['Survived']].mean()
Sex_surv.reset_index(inplace=True)
Sex_surv.columns=['Sex','Sex_surv_rate']
merged_df1 = pd.merge(Train,Sex_surv,how='left', on ='Sex')
Train[['PassengerId','Survived']].join(Train_final[['Pclass','Sex']], how='outer') #join is similar to merge except the key you want to join on is your index instead of a column
