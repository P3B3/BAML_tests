#%%
import pandas as pd
import PCA

df = pd.read_csv('drug_overdose_death.csv', parse_dates=True, low_memory=False)
df_number_of_death = (df.loc[lambda df:df.Indicator == 'Number of Deaths'])
df_number_of_death = (df_number_of_death[df_number_of_death.State != 'US'])
df_number_of_death.rename(columns={'Data Value':'X'}, inplace=True) 

df_number_of_death_cocaine = (df.loc[lambda df:df.Indicator == 'Cocaine (T40.5)'])
df_number_of_death_heroin = (df.loc[lambda df:df.Indicator == 'Heroin (T40.1)'])
df_number_of_death_opioids = (df.loc[lambda df:df.Indicator == 'Opioids (T40.0-T40.4,T40.6)'])

df_number_of_death.rename(columns={'X':'X1'}, inplace=True)
df_number_of_death_cocaine.rename(columns={'Indicator':'Y','Data Value':'X2'}, inplace=True)
df_merge_cocaine = pd.merge(df_number_of_death_cocaine, df_number_of_death, on=['State','Year', 'Month'])
df_merge_cocaine['Cocaine (T40.5)'] = df_merge_cocaine['X2']/df_merge_cocaine['X1']

df_number_of_death_heroin.rename(columns={'Indicator':'Y','Data Value':'X2'}, inplace=True)
df_merge_heroin = pd.merge(df_number_of_death_heroin, df_number_of_death, on=['State','Year', 'Month'])
df_merge_heroin['Heroin (T40.1)'] = df_merge_heroin['X2']/df_merge_heroin['X1']

df_number_of_death_opioids.rename(columns={'Indicator':'Y','Data Value':'X2'}, inplace=True)
df_merge_opioids = pd.merge(df_number_of_death_opioids, df_number_of_death, on=['State','Year', 'Month'])
df_merge_opioids['Opioids (T40.0-T40.4,T40.6)'] = df_merge_opioids['X2']/df_merge_opioids['X1']

df_merge = pd.merge(df_merge_cocaine,df_merge_heroin, left_index=True, right_index=True)[['Cocaine (T40.5)','Heroin (T40.1)']]
df_merge = pd.merge(df_merge,df_merge_opioids,left_index=True, right_index=True)[['Cocaine (T40.5)','Heroin (T40.1)','Opioids (T40.0-T40.4,T40.6)']]

df_merge.rename(columns={'Cocaine (T40.5)':'X1','Heroin (T40.1)':'X2','Opioids (T40.0-T40.4,T40.6)':'X3'}, inplace=True)  

print (PCA.getPCA(df_merge))