import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#import numpy as np


plt.style.use('bmh')
df = pd.read_csv('C:\\Users\\US\\Desktop\\insurance.csv')

#df.info()

df = df[df.smoker != 'yes']     #   removing smokers Data
df = df[df.region != 'southeast']   #   removing patients from southeast data to have data from only one location
df=df.drop(columns=['sex','children','region','smoker'])

df.info()         #     1

print(df['age'].describe())     #       2
print('age Median =',df['age'].median())
print('age Mode',df['age'].mode())

#print(df['bmi'].describe())
#print('bmi Median =',df['bmi'].median())
#print('bmi Mode',df['bmi'].mode())


#print(df['charges'].describe())
#print('charges Median =',df['charges'].median())
#print('charges Mode',df['charges'].mode())
df.to_csv('C:\\Users\\US\\Desktop\\pokoo.csv', index=False)
print(df.head())



#df.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8);
#plt.figure(figsize=(9, 8))
sns.distplot(df['age'], color='g', bins=100, hist_kws={'alpha': 0.4});     #       3
#sns.distplot(df['bmi'], color='g', bins=100, hist_kws={'alpha': 0.4});
#sns.distplot(df['charges'], color='g', bins=100, hist_kws={'alpha': 0.4});


""""
for i in range(0, len(df.columns), 791):
    sns.pairplot(data=df,
                x_vars=df.columns[i:i+791],                 #       4
                y_vars=['bmi'])

"""




plt.show()


