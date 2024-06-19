from stocks_ta.stocks_ingest import stock_data_ingest
from stocks_ta.analysis import myanalysis

ticketfilename="Tickers_Jan_2024.csv"
sourcepath="./stocks_ta/ticker_file/"
destionpath="./stocks_ta/stock_data/"
logpath="./stocks_ta/log_files/"
logfilename="2024_06_18.csv"


startd="2024-01-01"
endd="2024-06-15"



if __name__ == "__main__":
    print("inside the main method")

    stock_data = stock_data_ingest(ticketfilename,sourcepath,destionpath,logpath)

    stock_download_data=stock_data.download_data(startd,endd)

    logfile_df=myanalysis(logpath,logfilename)

    print(logfile_df.read_file())



   




