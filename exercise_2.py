import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import linear_model
from scipy import stats
import numpy as np
from sklearn.metrics import mean_squared_error
import seaborn as sns

# Reading data
df_data_public = pd.read_csv(
                 'survey_results_public.csv',
                 header=0,
                 index_col=['Respondent'])

# Selecting columns
df_data_public_col = pd.read_csv(
                     'survey_results_public.csv',
                     header=0,
                     usecols=[
                         'YearsCode',
                         'Age1stCode',
                         'Age',
                         'WorkWeekHrs',
                         'CodeRevHrs',
                         'Hobbyist',
                         'Country']).dropna()

# Selecting numeric data: (if numeric = true) and saving all data as numeric
df_data_public_col = df_data_public_col[
                     df_data_public_col[
                        'Age1stCode'].str.isnumeric() == True]
df_data_public_col['Age1stCode'] = pd.to_numeric(
                                   df_data_public_col['Age1stCode'])
df_data_public_col = df_data_public_col[
                        df_data_public_col['YearsCode'].str.isnumeric() ==
                        True]
df_data_public_col['YearsCode'] = pd.to_numeric(
                                  df_data_public_col['YearsCode'])
# Looking for correlaction - high
df_data_public_col.corr()
df_data_public_col.describe()

# Finding quantiles
Q1 = df_data_public_col.quantile(0.25)
Q3 = df_data_public_col.quantile(0.75)
IQR = Q3 - Q1

# Deleting deviated values
col_df_data_public_q = df_data_public_col[
                        ~((df_data_public_col < (Q1 - 1.5 * IQR)) |
                          (df_data_public_col > (Q3 + 1.5 * IQR))).any(axis=1)]
col_df_data_public_q.corr()

# Plots before deleting deviated values and after deleting
df_data_public_col.plot()
plt.show()
col_df_data_public_q.plot()
plt.show()

# Changing data into 0 or 1
col_df_data_public_q['Hobbyist'] = col_df_data_public_q[
                                    'Hobbyist'].map({'Yes': 1, 'No': 0})

col_df_data_public_q['Hobbyist'] = col_df_data_public_q[
                                    'Hobbyist'].dropna()

col_df_data_public_q['Country'] = col_df_data_public_q['Country'].dropna()
label_encoder = preprocessing.LabelEncoder()

label_encoder.fit(col_df_data_public_q['Country'])
label_encoder.transform(col_df_data_public_q['Country'])

# Assignment id for every country
col_df_data_public_q['Country_id'] = col_df_data_public_q[
                                        'Country'].factorize()[0]
# Creating a dictionary
id_to_category = dict(col_df_data_public_q[['Country_id',
                                            'Country']].values)

# Predicting age (based on Country)
reg = linear_model.LinearRegression()
reg.fit(col_df_data_public_q[['YearsCode']], col_df_data_public_q[['Age']])

# MSE (mean squared error) - difference between
# the estimator and the estimated value
mean_squared_error(col_df_data_public_q[['Age']],
                   reg.predict(col_df_data_public_q[['YearsCode']]))


reg = linear_model.LinearRegression()
reg.fit(col_df_data_public_q[['Age1stCode', 'YearsCode']],
        col_df_data_public_q[['Age']])

mean_squared_error(col_df_data_public_q[['Age']],
                   reg.predict(col_df_data_public_q[['Age1stCode',
                                                     'YearsCode']]))

reg = linear_model.LinearRegression()
reg.fit(col_df_data_public_q[['Age1stCode',
                              'YearsCode',
                              'Hobbyist',
                              'Country_id']],
                              col_df_data_public_q[['Age']])

# MSE should be between 0 and 1
mean_squared_error(col_df_data_public_q[['Age']],
                   reg.predict(col_df_data_public_q[['Age1stCode',
                                                     'YearsCode',
                                                     'Hobbyist',
                                                     'Country_id']]))
# MSE is very high, there is no relationship between
# age and country data

# Box plots
sns.boxplot(y='Age', data=df_data_public)
plt.show()
sns.boxplot(y='Age', data=col_df_data_public_q)
plt.show()

sns.regplot(y=col_df_data_public_q['YearsCode'],
            x=col_df_data_public_q['Age'])
plt.show()

# Dots are not focused in place of regression
sns.regplot(y=col_df_data_public_q['YearsCode'],
            x=col_df_data_public_q['Age'])
plt.show()
