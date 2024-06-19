
from stocks_ta.logger import mylogger
from pathlib import Path
import datetime as dt
import yfinance as yf
import pandas as pd
import json
import csv
import os
import time



now = dt.datetime.now()

class stock_data_ingest():

    def __init__(self, stock_tickerfile, sourcepath, destinatonpath, logpath):

        self.stock_tickerfile=stock_tickerfile
        self.sourcepath=sourcepath
        self.destinatonpath=destinatonpath
        self.logpath=logpath
        print("inside init method")


    def get_tickers(self):

        tickerpathandsymbol=[]

        tickerfilepath=self.sourcepath+self.stock_tickerfile

        dataframe = pd.read_csv(tickerfilepath)

        for i,row in dataframe.iterrows():

            try:

                print(i)

                symbol=(row['Symbol'].replace(' ', ''))

                print(symbol)

                tickerpathandsymbol.append(symbol)

            except Exception as e:
                print(e)
                mylogger.logging_error(e)
        
        return tickerpathandsymbol
    

    
    def download_data(self, startdate, end_date): 

        for ticker in self.get_tickers():

            try: 

                ticker_file_exist_check = Path(self.destinatonpath+str(ticker)+".csv")

                print(ticker_file_exist_check)

                if ticker_file_exist_check.is_file():

                    if os.stat(ticker_file_exist_check).st_size == 0:

                        dataframe_yf = yf.download(ticker, period="max",interval = "1d")

                        dataframe_yf.to_csv(self.destinatonpath+'{}.csv'.format(ticker), header=True)

                        print("New Ingestion "+str(ticker))

                        mylogger.logging_info("New Ingestion,"+str(ticker))

                    else:

                        dataframe_yf = yf.download(ticker, start=startdate, end=end_date,interval = "1d")
                
                        dataframe_yf.to_csv(self.destinatonpath+'{}.csv'.format(ticker),mode='a', header=False)
                        
                        print("Appending Data "+str(ticker))

                        mylogger.logging_info("Appending Data,"+str(ticker))


                else:

                    dataframe_yf = yf.download(ticker, period="max",interval = "1d")

                    dataframe_yf.to_csv(self.destinatonpath+'{}.csv'.format(ticker), header=True)

                    print("New Ingestion "+str(ticker))

                    mylogger.logging_info("New Ingestion,"+str(ticker))

                    # break

            except Exception as e:
                print(e)
                mylogger.logging_error(e)
                

