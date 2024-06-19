import pandas as pd


class myanalysis():

    def __init__(self, filepath,filename):

        self.filepath = filepath
        self.filename = filename


    def read_file(self):

        csvfile=self.filepath+self.filename

        df = pd.read_csv(csvfile)

        return df
    
    

