import pandas as pd
import numpy as np
import csv


c = 'examples/ex7.csv'


def csv_pro(c):
    with open(c) as f:
        lines = list(csv.reader(f))
    headers, values = lines[0], lines[1:]
    return {h: v for h, v in zip(headers, zip(*values))}


print(pd.DataFrame(csv_pro(c)))
