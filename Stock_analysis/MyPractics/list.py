import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as BS

list = pd.read_csv('Stock_analysis/MyPractics/list_co.csv')
list.종목코드 = list.종목코드.map('{06d}'.format)
print(list)
