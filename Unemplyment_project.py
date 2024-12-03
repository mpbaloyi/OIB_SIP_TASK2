
#MIKATEKO PETRONELLA BALOYI
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r'C:\Users\mihlotib\Desktop\Mika\Internship_Oasis Infobyte\Unemployment in India.csv')
#print(df.head()) #testing if the file opened

#displaying the rows of the csv file(by default it will return the first 5 rows unless you specify the number)
#And inspecting the structure of the dataFrame
rows=df.head()
print(rows)

#Displaying the columns
cols=df.columns
print(cols)

#Displaying  the number of rows and columns
shyp=df.shape
print(shyp)

# removing any leading or trailing whitespace characters.
df.columns = df.columns.str.strip()
df['Estimated Unemployment Rate (%)']

# Renaming columns with simpler names
df.rename(columns={

    'Estimated Unemployment Rate (%)': 'Unemployment Rate',
    'Estimated Employed': 'Employed',
    'Estimated Labour Participation Rate (%)': 'Labour Participation Rate'
}, inplace=True)
print(df.columns) #checking if it changed

#visualizing the frequency distribution of regions in the Unemployment in India dataFrame
plt.figure(figsize=(10,6))
sns.countplot(y='Region',data=df)
plt.title(' Frequency distribution of regions')
plt.show()

# Add a 12-month moving average for the unemployment rate
df['Unemployment_MA'] = df['Unemployment Rate'].rolling(window=12).mean()

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

#  plotting the unemployment rate
#comparing the trend of the unemployment rate with its 12-month moving average
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Date', y='Unemployment Rate', marker='*', label='Unemployment Rate')
sns.lineplot(data=df, x='Date', y='Unemployment_MA', label='12-Month Moving Average')
plt.title('Unemployment Rate and 12-Month Moving Average Over Time')
plt.legend()
plt.show()

#States with high and low unemployment rates
avg_unemployment_rate=df.groupby('Region')['Unemployment Rate'].mean()
highest_unemployment_state=avg_unemployment_rate.idxmax()
lowest_unemployment_state=avg_unemployment_rate.idxmin()
high_unemployment_rate=avg_unemployment_rate.max()
low_unemployment_rate=avg_unemployment_rate.min()
print(f'State  with the highest employment is : {highest_unemployment_state}')
print(f'With high employment rate of : {high_unemployment_rate}')
print(f'State  with the lowest employment is : {lowest_unemployment_state}')
print(f'With the low employment rate of : {low_unemployment_rate}')
#_______________________________________________________________________________
avg_unemployment_rate

regions = avg_unemployment_rate.index
avarage_rates = avg_unemployment_rate.values

plt.figure(figsize=(10, 6))
plt.bar(regions, avarage_rates, color='green')
plt.xlabel('Region')
plt.ylabel('Average Unemployment Rate')
plt.title('Average Unemployment Rate by Region')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 6))
sns.boxplot(x='Region', y='Unemployment Rate', data=df,palette="Set2")
plt.title("Unemployment Rate Distribution by Region")
plt.xlabel('State')
plt.ylabel('Unemployment Rate')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(x='Region', y='Labour Participation Rate', data=df,palette='hsv')
plt.title("Estimated Labour Participation Rate")
plt.xlabel('Region')
plt.ylabel('Labour Participation Rate')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(x='Region', y='Employed', data=df,palette='brg')
plt.title("Estimated employed")
plt.xlabel('Region')
plt.ylabel('Employed')
plt.xticks(rotation=90)
plt.show()

#creating a histogram with a density plot
sns.histplot(data=df, x='Unemployment Rate', kde=True,color='brown')
plt.show()


sns.histplot(data=df, x='Employed', kde=True,color='darkorange')
plt.tight_layout()
plt.show()

sns.histplot(data=df, x='Labour Participation Rate', kde=True,color='navy')
plt.show()

plt.figure(figsize=(10,7))
sns.scatterplot(data=df, x='Unemployment Rate', y='Labour Participation Rate', hue='Region')
plt.show()

pplot=df[['Unemployment Rate','Employed','Labour Participation Rate']]
sns.pairplot(pplot,markers='*',palette='coolwarm')
plt.show()

#Animated bar chat to visualize the unemployment rate across different region
import plotly.express as px

fig = px.bar(df, x='Region', y='Unemployment Rate', title='unemployment rate 2020',
             animation_frame='Date',template='plotly',color='Region')
fig.show()
#Area graph
df['Area'].value_counts()

sns.countplot(x='Area',data=df)
plt.title(' Visualization (Count Plot) Area')
plt.show()
print(df['Area'].value_counts())