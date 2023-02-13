import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as BS

df = pd.read_csv('Stock_analysis/MyPractics/list_co.csv')
df['종목코드'] = df['종목코드'].map(lambda x: str(x).zfill(6))
print(df)
