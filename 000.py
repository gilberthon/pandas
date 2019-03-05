import pandas as pd
import numpy as np

df = pd.DataFrame({'Qu1': [1, 3, 4, 3, 4],
                   'Qu2': [2, 3, 1, 2, 3],
                   'Qu3': [1, 5, 2, 4, 4]})
print(df.apply(pd.value_counts))
