import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as BS

list_csv = pd.read_csv('GITHUB/my-project/Stock_analysis/list_co.csv')
list_df = pd.DataFrame(list_csv)
list_df = list_df.sort_values(by='종목코드')

print(list_df[0:])
