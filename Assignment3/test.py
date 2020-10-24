import numpy as np
import pandas as pd
ser = pd.Series(np.arange(4.), index=['a','b','c','d'])
print(ser[-1])