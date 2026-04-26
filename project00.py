import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#set style
sns.set(style="whitegrid")

#Load titanic dataset from online url
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(type(df))

#show basic info
print("Dataset Head:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values: ")
print(df.isnull().sum())
