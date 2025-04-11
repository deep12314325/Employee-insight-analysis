import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
file_path=r"C:\Users\RoG\OneDrive\Desktop\pp.xlsx"
df=pd.read_excel(file_path)
##print("Some EDA Outcomes :")
##print(df.head())
##print(df.tail())
##print(df.info())
##print(df.describe())
##print(df.shape)
df['Age'] = pd.to_datetime('today').year - pd.to_datetime(df['BirthDate']).dt.year
subset = df[['Age', 'Salary']].dropna()
corr = subset.corr()
print(corr)
##print(df['Salary'].corr())
##1
##df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
##salary_data = df['Salary'].dropna()
#### Histogram
##plt.figure(figsize=(8,5))
##sns.histplot(salary_data, kde=True, bins=30)
##plt.title("Salary Distribution")
##plt.xlabel("Salary")
##plt.ylabel("Frequency")
##plt.show()
##
#### Boxplot
##plt.figure(figsize=(6,2))
##sns.boxplot(x=salary_data)
##plt.title("Salary Spread")
##plt.show()
##
####2
####print("Compare mean salary across departments")
####salary_by_post = df.groupby('Post Name')['Salary'].mean().sort_values(ascending=False)
####
######Bar plot
####salary_by_post.plot(kind='bar', figsize=(10,5), color='skyblue')
####plt.title("Average Salary by Post Name")
####plt.ylabel("Average Salary")
####plt.xticks(rotation=45)
####plt.tight_layout()
####plt.show()
####
######3
######print("Analyze if older employees earn more")
######from datetime import datetime
######
######df['BirthDate'] = pd.to_datetime(df['BirthDate'], errors='coerce')
######df['Age'] = datetime.now().year - df['BirthDate'].dt.year
######
######## Scatter plot
######plt.figure(figsize=(8,5))
######sns.scatterplot(x='Age', y='Salary', data=df)
######plt.title("Age vs Salary")
######plt.xlabel("Age")
######plt.ylabel("Salary")
######plt.grid(True)
######plt.show()
####
######4
####print("Analyze tenure (in years) across employees")
####import pandas as pd
####import matplotlib.pyplot as plt
####
##### Calculate age from BirthDate
####df['BirthDate'] = pd.to_datetime(df['BirthDate'], errors='coerce')
####df['Age'] = pd.Timestamp.now().year - df['BirthDate'].dt.year
####
##### Group by Post Name and calculate average age
####avg_age_by_post = df.groupby('Post Name')['Age'].mean().sort_values()
####
##### Bar chart
####plt.figure(figsize=(10,6))
####avg_age_by_post.plot(kind='barh', color='skyblue')
####plt.title("Average Employee Age by Post Name (Tenure Proxy)", fontsize=14)
####plt.xlabel("Average Age")
####plt.ylabel("Post Name")
####plt.tight_layout()
####plt.show()
####
####
######5
##print("Show how hiring has changed over time")
##bins = [20, 30, 40, 50, 60, 70]
##labels = ['20–29', '30–39', '40–49', '50–59', '60+']
##df['Age'] = pd.to_datetime('today').year - pd.to_datetime(df['BirthDate']).dt.year
##df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
##age_group_counts = df['Age Group'].value_counts().sort_index()
##
### Pie chart
##plt.figure(figsize=(8,6))
##age_group_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
##plt.title("Employee Distribution by Age Group (Hiring Trend Proxy)")
##plt.ylabel("")  
##plt.tight_layout()
##plt.show()
####
######6
##print("Median Tenure (Estimated via Age)")
##df['BirthDate'] = pd.to_datetime(df['BirthDate'], errors='coerce')
##df['Age'] = pd.Timestamp.now().year - df['BirthDate'].dt.year
##median_tenure = df['Age'].median()
##print(f"Median Estimated Tenure: {median_tenure:.1f} years")
##plt.figure(figsize=(10,6))
##plt.hist(df['Age'].dropna(), bins=10, color='skyblue', edgecolor='black')
##plt.axvline(median_tenure, color='red', linestyle='--', label=f'Median Age: {median_tenure:.1f}')
##plt.title("Age Distribution (Tenure Proxy)")
##plt.xlabel("Age (Years)")
##plt.ylabel("Number of Employees")
##plt.legend()
##plt.tight_layout()
##plt.show()
##
##
####7
##print("New Hires This Year (Approx via BirthDate)")
##recent_births = df[df['BirthDate'].dt.year >= 2000]
##new_hires = recent_births.shape[0]
##print(f"New Hires (born ≥ 2000): {new_hires}")
##df['BirthDate'] = pd.to_datetime(df['BirthDate'], errors='coerce')
##df['Age'] = pd.Timestamp.now().year - df['BirthDate'].dt.year
##df['AgeGroup'] = pd.cut(df['Age'], bins=[20,30,40,50,60,70], labels=['21-30','31-40','41-50','51-60','61-70'])
##gender_age = df.groupby(['AgeGroup', 'Gender']).size().unstack(fill_value=0)
### Plot
##gender_age.plot(kind='bar', stacked=True, figsize=(10,6), color=['lightblue','lightcoral'])
##plt.title('Hiring Trend by Gender and Age Group')
##plt.xlabel('Age Group')
##plt.ylabel('Number of Employees')
##plt.legend(title='Gender')
##plt.xticks(rotation=0)
##plt.tight_layout()
##plt.show()

####8
print("Heatmap presentation of salary and age correlation") 
plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap='YlGnBu', center=0)
plt.title("Correlation Heatmap: Age vs Salary")
plt.show()
