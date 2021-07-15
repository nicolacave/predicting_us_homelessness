class homeless():

    def __init__(self, df, year):
        self.df = df
        self.year = year

    def format_df(self):
        self.df['year'] = self.year
        self.df.replace(',','', regex=True, inplace=True)
        self.df.loc[8] = self.df.loc[8].astype(float)
        self.df.loc[4] = self.df.loc[4].astype(float)
        self.df['unsheltered rate'] = (self.df.loc[8] / self.df.loc[4])
        df = self.df.loc[:, ['year', 'CoC Number', 'CoC Name', 'unsheltered rate']]
        return df 
