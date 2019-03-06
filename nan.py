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
print(ds)
meat_to_animal = {
  'bacon': 'pig',
  'pulled pork': 'pig',
  'pastrami': 'cow',
  'corned beef': 'cow',
  'honey ham': 'pig',
  'nova lox': 'salmon'
}
d = ds['food'].map(lambda x: meat_to_animal[str.lower(x)])
ds['animal'] = d
print(ds)
