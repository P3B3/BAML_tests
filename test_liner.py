#%%
import pandas as pd
import numpy as np
import linear_reg
from IPython.display import display

df = pd.read_csv('drug_overdose_death.csv', parse_dates=True, low_memory=False)
df_number_of_death = (df.loc[lambda df:df.Indicator == 'Number of Deaths'])
df_number_of_death = (df_number_of_death[df_number_of_death.State != 'US'])
df_number_of_death_overdose = (df.loc[lambda df:df.Indicator == 'Number of Drug Overdose Deaths'])
df_number_of_death_overdose = (df_number_of_death_overdose[df_number_of_death_overdose.State != 'US'])
df_number_of_death.rename(columns={'Data Value':'X'}, inplace=True)  
df_number_of_death_overdose.rename(columns={'Data Value':'Y'}, inplace=True) 
df_merge = (pd.merge(df_number_of_death, df_number_of_death_overdose, on=['State', 'Year', 'Month']))[['X', 'Y']]

linear_reg.displayAll(df_merge)

test = [[4036],[1438],[10234],[892]]
pred = (pd.merge(pd.DataFrame(test), pd.DataFrame(linear_reg.getLineRegPred(df_merge,test)),left_index=True, right_index=True))

display(pred)
#отношение независимых смертей от нарк к зависимым всего смертям + предикативная модель