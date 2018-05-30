import pandas as pd
import quandl

#quandl.get('WIKI/GOOGL')
quandl.ApiConfig.api_key = '-qAjQbTFBxyeUkunkuZ7'
df = quandl.get('BCMGEX/MWU2016', start_date='2016-09-14', end_date='2016-09-14')

file = open('data.csv', mode='w')
file.write(df.to_csv())