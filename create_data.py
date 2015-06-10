
import sys
from root_pandas import *
import numpy as np
import pandas as pd

OUTPATH = sys.argv[1]

x = np.random.normal(0, 1, 100000)
y = np.random.normal(0, 1, 100000)

df = pd.DataFrame({'x': x, 'y': y})
df.to_root(OUTPATH)

