import pandas as pd

#3
#Reading data (separator for tsv file is tab)
df_data = pd.read_csv(
          'train.tsv',
          sep='\t',
          names=[
           'price', 'nr_rooms', 'meters', 'floors', 'location', 'description'])
pd.options.display.float_format = '{:.2f}'.format

df_description = pd.read_csv('description.csv')
#Name columns
df_description.columns = ['floors', 'name_floor']

#Merge tables - floors is the key
df_flat_name_floor = pd.merge(df_data, df_description, on=['floors'])

#Saving to file
df_flat_name_floor.to_csv('out2.csv', header=False, index=None)
