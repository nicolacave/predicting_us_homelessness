# PIT_2012['year'] = 2012
# PIT_2012.replace(',','', regex=True, inplace=True)
# # c = PIT_2012.select_dtypes(object).columns
# # PIT_2012[c] = PIT_2012[c].apply(pd.to_numeric,errors='coerce')

# # pd.to_numeric([PIT_2012['Unsheltered Homeless, 2012', 'Overall Homeless, 2012']], errors='coerce')
# PIT_2012['Unsheltered Homeless, 2012'] = PIT_2012['Unsheltered Homeless, 2012'].astype(float)
# PIT_2012['Overall Homeless, 2012'] = PIT_2012['Overall Homeless, 2012'].astype(float)
# # PIT_2012['Overall Homeless, 2012'] = PIT_2012['Overall Homeless, 2012'].astype(float)

# PIT_2012['unsheltered rate'] = (PIT_2012['Unsheltered Homeless, 2012'] / PIT_2012['Overall Homeless, 2012'])
# PIT_2012 = PIT_2012.loc[:, ['year','CoC Number', 'CoC Name', 'unsheltered rate']]
# PIT_2012.info()

# PIT_2013['year'] = '2013'
# PIT_2013['unsheltered rate'] = (PIT_2013['Unsheltered Homeless, 2013'] / PIT_2013['Overall Homeless, 2013'])
# PIT_2013 = PIT_2013.loc[:, ['year','CoC Number', 'CoC Name', 'unsheltered rate']]

