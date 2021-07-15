class homeless():

    def __init__(self, df, year):
        self.df = df
        self.year = year
    
    def rename_columns(self):
        self.df.columns = self.df.columns.str.replace(str(self.year), '')
        self.df.columns = self.df.columns.str.replace(',', '')
        self.df.columns = self.df.columns.str.rstrip()
        return self.df

    def format_df(self):
        self.df['year'] = self.year
        self.df.replace(',','', regex=True, inplace=True)
        self.df.iloc[:,7] = self.df.iloc[:,7].astype(float)
        self.df.iloc[:,2] = self.df.iloc[:,2].astype(float)
        self.df['unsheltered rate'] = (self.df.iloc[:,7] / self.df.iloc[:,2])
        #df = self.df.loc[:, ['year', 'CoC Number', 'CoC Name', 'unsheltered rate']]
        return self.df 

    def strip_columns(self, col_names):
        self.df = self.df[col_names]
        return self.df