import pandas as pd

def missing_value_summary(df):
  summary_df = df.isna().sum()
  total_na = summary_df[summary_df>0].sort_values(ascending=False)
  percent_na = round(total_na/len(df)*100,2)
  summary_na = pd.concat([total_na, percent_na], axis=1)
  summary_na.columns = ['Total Missing Values', '% of Missing Values']
  print('Your data contain', df.shape[1], 'columns.')
  print('There are missing values in', summary_na.shape[0], 'columns.')
  return summary_na