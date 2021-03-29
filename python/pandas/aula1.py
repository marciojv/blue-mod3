# Importação da  biblioteca pandas. 
import pandas as pd

train_df = pd.read_csv('sample_data/titanic.csv')
#print(train_df)
example_series =  pd.Series([1,5,10,30,50,30,15,40,45])

# media
print(train_df['age'].mean())
print(example_series.mean())

#mediana
print(train_df['age'].median())
print(example_series.median())

# Mediana e Quantil
print(train_df['age'].quantile())
print(example_series.quantile())
print(train_df['age'].quantile(q=0.25))
print(example_series.quantile(q=0.25))

# amplitude
print(train_df['age'].max() - train_df['age'].min())
print(example_series.max() - example_series.min())

#varianca
print(train_df['age'].var())
print(example_series.var())

#Desvio padrão
print(train_df['age'].std())
print(example_series.std())

