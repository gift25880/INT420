import pandas as pd
from sklearn.impute import KNNImputer

def missing_value_summary(df):
  summary_df = df.isna().sum()
  total_na = summary_df[summary_df>0].sort_values(ascending=False)
  percent_na = round(total_na/len(df)*100,2)
  summary_na = pd.concat([total_na, percent_na], axis=1)
  summary_na.columns = ['Total Missing Values', '% of Missing Values']
  print('Your data contain', df.shape[1], 'columns.')
  print('There are missing values in', summary_na.shape[0], 'columns.')
  return summary_na

def fillna_global_mean(df,col_im):
  m = df[col_im].mean()
  df[col_im] = df[col_im].fillna(m)
  return df

def fillna_group_mean(df,col_im,col_gr):
  for g in df[col_gr].unique():
      m = df[col_im][df[col_gr]==g].mean()
      df[col_im][df[col_gr]==g] = df[col_im][df[col_gr]==g].fillna(m)
  return df

def fillna_global_mode(df,col_im):
  m = df[col_im].mode()[0]
  df[col_im] = df[col_im].fillna(m)
  return df

def fillna_group_mode(df,col_im,col_gr):
  for g in df[col_gr].unique():
      m = df[col_im][df[col_gr]==g].mode()
      df[col_im][df[col_gr]==g] = df[col_im][df[col_gr]==g].fillna(m)
  return df

def fillna_knn(df,k):
  #Homework Do something ...
  imputer = KNNImputer(n_neighbors=k)
  imputer.fit(df)
  df = imputer.transform(df)
  return df