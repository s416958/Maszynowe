import pandas as pd

#1
#Data loading (train.tsv) as DataFrame (df_data)
df_data = pd.read_csv(
        'train.tsv',
        sep='\t',
        names=['price', 'nr_rooms', 'meters', 'floors', 'location', 'description'])

#Counting mean of apartments price and round to 1 zl
mean_price = round(df_data['price'].mean(), 3)

#Saving mean_price in out0.csv file
with open('out0.csv', 'w') as file:
    file.write(str(mean_price))

#2
#Counting price for square meter and round to 1 zl
df_data['price_meters'] = (df_data['price']/df_data['meters']).round(3)

#Choosing data with number of rooms (=>3), price and
#price for square meter (lower than mean price for square meter)
df_select_data = df_data.loc[
                df_data['nr_rooms'] >= 3 &
                (df_data['price_meters'] <
                 round(float(df_data['price_meters'].mean()), 2))][
                 ['nr_rooms', 'price', 'price_meters']]

#Saving results in out1.csv file
df_select_data.to_csv('out1.csv', header=False, index=None)
