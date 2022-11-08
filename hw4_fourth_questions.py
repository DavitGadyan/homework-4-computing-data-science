###############
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.
#
# import packages including custom functions for DRY
import pandas as pd
from hw4_third_questions import *

# import data
df = pd.read_csv('covid.csv')

# calculate stats
print('List of countries: ', df.Country.tolist())

print('Total average of death confirmed: ', (df.Deaths / df.Confirmed).mean())

df_coutries_500_plus = df[df.Active > 500]
print('Total average of death confirmed for countries with more than 500 active cases: ', (df_coutries_500_plus.Deaths / df_coutries_500_plus.Confirmed).mean())

df_coutries_1000_plus = df[df.Active > 1000]
print('Total average of death confirmed for countries with more than 1000 active cases: ', (df_coutries_1000_plus.Deaths/df_coutries_1000_plus.Confirmed).mean())

df_coutries_5000_plus = df[df.Active > 5000]
print('Total average of death confirmed for countries with more than 5000 active cases: ', (df_coutries_5000_plus.Deaths/df_coutries_5000_plus.Confirmed).mean())