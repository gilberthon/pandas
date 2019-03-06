import pandas as pd
import numpy as np
from numpy import nan as NA


string_data = pd.Series(['aardvark', 'artichoke', NA, 'avocado'])
# string_data[0] = None
# print(string_data.isnull())
# print(string_data.dropna())

data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA],
                     [NA, NA, NA], [NA, 6.5, 3.]])
# print(data)
# print(data.dropna(axis=1, how='all'))

df0 = pd.DataFrame(np.random.randn(7, 3))
df0.iloc[:4, 1] = NA
df0.iloc[:2, 2] = NA
df0.iloc[:6, 0] = NA
# df0.fillna({0: 0, 1: 0.5, 2: 1}, inplace=True)
# print(df0)
# print(df0.dropna())

# print(df0.fillna(method='bfill', limit=2))
# print(df0.fillna(df0.mean()))
a = df0.mean(1).fillna(0)
# print(a)
# print(df0.fillna(a))

ds = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
                            'Pastrami', 'corned beef', 'Bacon',
                            'pastrami', 'honey ham', 'nova lox'],
                   'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
# print(ds)
meat_to_animal = {
  'bacon': 'pig',
  'pulled pork': 'pig',
  'pastrami': 'cow',
  'corned beef': 'cow',
  'honey ham': 'pig',
  'nova lox': 'salmon'
}
d = ds['food'].map(lambda x: meat_to_animal[x.lower()])
ds['animal'] = d
# print(ds)

ser = pd.Series([1., -999., 2., -999., -1000., 3.])
# print(ser)
ser.replace([-999, -1000], [NA, 0], inplace=True)
# print(ser)

df = pd.DataFrame(np.arange(12).reshape(3, 4),
                  index=['Ohio', 'Colorado', 'New York'],
                  columns=['one', 'two', 'three', 'four'])
# print(df)
df.rename(index=str.title, columns=str.upper, inplace=True)
# print(df)

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
cats = pd.cut(ages, bins, labels=group_names)
# print(cats)
# print(cats.categories)

df = np.random.rand(1000)
cats = pd.qcut(df, 4, precision=2)
# print(cats.value_counts())

data = pd.DataFrame(np.random.randn(1000, 4))
col = data
# print(data[(np.abs(col) > 3).any(1)])
# print(np.abs(data) > 3)

df = pd.DataFrame(np.arange(5 * 4).reshape(5, 4))
sampler = np.random.permutation(5)
# print(sampler)
# print(df.take(sampler))
# print(df.sample(1))
df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                   'data1': range(6)})
dummies = pd.get_dummies(df['key'], prefix='key')
print((df[['data1', 'key']].join(dummies)))
