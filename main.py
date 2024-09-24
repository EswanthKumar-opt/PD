import pandas as pd
import csv

df = pd.read_csv(r'C:\\Users\\eswanth.kumar\\Desktop\\PD\\sample_data.csv')
# print(df.head(10))
new_table = {'id':[1,2,3],'name': ['Eswanth','sathish','john']}

df2 = pd.DataFrame(new_table)
# print(df2)
## in SQL

# Select * from table

################# filtering #################


filtered_df = df[df['Salary'] == 50000]
# print(filtered_df)

## select * from table where salary = 50000

filtered_df = df[(df['Salary'] == 50000) & (df['Department'] == 'Department_6')]
# print(filtered_df)

# select * from table where salary = 50000 and Department == Department_6

######################selecting rows #####################

selecting_df = df[['Name','Age']].head(10)
# print(selecting_df)

## select Name,Age from table

selected_df = df.drop('Location',axis=1)
# print(selected_df)

## select coulmn1,column2 from table excluding location

############### Aggregations ##################

# sum
total_sum = df['Salary'].sum()
# AVG
# print(total_sum)
total_sum = df['Salary'].mean()
#count
total_sum = df['Salary'].count()
#max
total_sum = df['Salary'].max()
#min
total_sum = df['Salary'].min()

##################### Group by

group_df = df.groupby('Location').sum()
# print(group_df)

## select Location,sum(salary) from table_name group by Location

group_df = df.groupby(['Location','Salary']).sum()
# print(group_df)

################ Handing miss  Data

df1 = df.fillna(0)
# print(df1)

## Select Coalesce(coulmn_name , 0) from table_name

df2 = df.dropna()
# print(df2)

## select * from table where column_name is Not null

######################## Sorting #################

sort = df.sort_values(by='Age').head(10)
# print(sort)


sort2 = df.sort_values(by='Age',ascending= False).head(10)
# print(sort2)

################  removing Duplicate ###############

remove_df = df.drop_duplicates()
# print(remove_df)


################ REname ##################

rename = df.rename(columns= {"Salary" : "new_salary"})
# print(rename)

################# adding ##############

# df['salary_age'] = df['Salary'] + df['Age']
# print(df)


######################  concat ################

# concat = pd.concat(['table1','table2'])
# print(concat)


################  joining ######################

# merged_df = pd.merge(df,df2,on= 'id',how='inner')
# print(merged_df)

# merged_df = pd.merge(df,df2,on= 'id',how='left')
# print(merged_df)

# merged_df = pd.merge(df,df2,on= 'id',how='right')
# print(merged_df)

# merged_df = pd.merge(df,df2,on= 'id',how='outer')
# print(merged_df)

############### contional logical ###########

df['value or non_value'] = df['Salary'].apply(lambda x: 'value' if x > 50000 else 'non_value')
# print(df.head(10))

################# pivot #######################

# pivote = df.query('index >= 0')  # This will return all rows
# print(pivote)

pivote = df.pivot_table(index='Salary', columns='Age', values='Name', aggfunc='sum')  # Modify as needed
print(pivote)
## salary ah sum pana







