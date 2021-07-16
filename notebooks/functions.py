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
        self.df['state'] = self.df['CoC Number'].str.extract('([A-Z]\w{0,})', expand=True)
        self.df.replace(',','', regex=True, inplace=True)
        self.df['Unsheltered Homeless'] = self.df['Unsheltered Homeless'].astype(float)
        self.df['Overall Homeless'] = self.df['Overall Homeless'].astype(float)
        self.df['unsheltered rate'] = (self.df['Unsheltered Homeless'] / self.df['Overall Homeless'])
        return self.df 

    def strip_columns(self, col_names):
        for column in self.df.columns:
            if column not in col_names:
                self.df.drop(column, axis=1, inplace=True)
            else:
                continue
        return self.df