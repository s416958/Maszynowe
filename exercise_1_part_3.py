import matplotlib.pyplot as plt
import pandas as pd

# 4
# Setting to display (max. 100 columns)
pd.set_option('display.max_columns', 100)

# Reading data
df_data_survey_schema = pd.read_csv('survey_results_schema.csv', header=0)
df_data_survey_public = pd.read_csv(
                 'survey_results_public.csv',
                 header=0,
                 usecols=['Respondent', 'WorkWeekHrs', 'Age'],
                 index_col=['Respondent'])

# Deleting NA data
df_data_survey_public.dropna(inplace=True)

# Checking types
df_data_survey_public.dtypes

# Checking more information
df_data_survey_public.info()

# Checking unique values
column_values = df_data_survey_public[['Age']].values.ravel()
unique_values = pd.unique(column_values)
print(unique_values)

# Rounding and checking values
df_data_survey_public['Age'].round(0)
column_values = df_data_survey_public['Age'].values.ravel()

# Checking duplicates
unique_values = pd.unique(column_values)
print(unique_values)

df_data_survey_public['WorkWeekHrs'].round(0)
column_values = 
df_data_survey_public['WorkWeekHrs'].values.ravel().astype('int64')
unique_values = pd.unique(column_values)
print(unique_values)

# Selecting respondents who works 160 h per week
df_data_survey_public = 
df_data_survey_public[df_data_survey_public.WorkWeekHrs < 161]

# Changing type
df_data_survey_public = df_data_survey_public.astype('int64', copy=False)

# 5
# Making a chart
plt.plot(df_data_survey_public['Age'],
         df_data_survey_public['WorkWeekHrs'],
         'ro',
         markersize=0.5)
df_data_public_gender = pd.read_csv(
                        'survey_results_public.csv',
                        header=0,
                        usecols=[
                             'Respondent', 'WorkWeekHrs', 'Age', 'Gender'],
                        index_col=['Respondent'])
plt.xlabel('Wiek respondenta')
plt.ylabel('Przepracowanie godziny w tygodniu')
plt.show()

# Dropping NA data
df_data_public_gender.dropna(inplace=True)

# Checking number of genders and unique names
column_values = df_data_public_gender['Gender'].values.ravel()
unique_values = pd.unique(column_values)
print(unique_values)
df_data_public_gender['Gender'] = df_data_public_gender['Gender'].astype(str)
df_data_public_gender.info()

# Selecting only man and woman
df_data_public_gender = df_data_public_gender.loc[
                        (df_data_public_gender['Gender'] == 'Man') |
                        (df_data_public_gender['Gender'] == 'Woman')]
column_values = df_data_public_gender['Gender'].values.ravel()
unique_values = pd.unique(column_values)
print(unique_values)

column_values = df_data_public_gender[['Age']].values.ravel()
unique_values = pd.unique(column_values)
print(unique_values)

df_data_public_gender['WorkWeekHrs'].round(0)
column_values = df_data_public_gender[
                'WorkWeekHrs'].values.ravel().astype('int64')
unique_values = pd.unique(column_values)
print(unique_values)

df_data_public_gender = df_data_public_gender[
                        df_data_public_gender.WorkWeekHrs < 161]
grouped = df_data_public_gender.groupby('Gender')
fig, axes = plt.subplots(grouped.ngroups, sharex=True, figsize=(8, 6))

for i, (Gender, d) in enumerate(grouped):
    ax = d.plot.scatter(x='Age', y='WorkWeekHrs', ax=axes[i], label=Gender)
    ax.set_xlabel('Wiek respondenta')
    ax.set_ylabel('Przepracowane godziny w tygodniu')
fig.tight_layout()
plt.show()
