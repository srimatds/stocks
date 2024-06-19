import logging
import datetime as dt
import time


class mylogger():

    # def __init__(self,message):
    #     self.message=message

    def logging_info(message):

        # LOG_FILE = "./stocks_ta/log_files" + "/logs"
        # if not os.path.exists(LOG_FILE):
        #     os.makedirs(LOG_FILE)

        # LOG_FILE = LOG_FILE + "/" + dt.datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d %H_%M_%S') + ".log"
        csvfileformat="./stocks_ta/log_files/"+ dt.datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d') + ".csv"
        logFormatter = logging.Formatter("%(levelname)s,%(asctime)s,%(message)s")
        fileHandler = logging.FileHandler("{0}".format(csvfileformat))
        fileHandler.setFormatter(logFormatter)
        rootLogger = logging.getLogger()
        if not rootLogger.handlers:
            rootLogger.addHandler(fileHandler)
        rootLogger.setLevel(logging.INFO)

        return logging.info(message)
    

    def logging_error(message):

        csvfileformat="./stocks_ta/log_files/"+ dt.datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d') + ".csv"
        logFormatter = logging.Formatter("%(levelname)s,%(asctime)s,%(message)s")
        fileHandler = logging.FileHandler("{0}".format(csvfileformat))
        fileHandler.setFormatter(logFormatter)
        rootLogger = logging.getLogger()
        if not rootLogger.handlers:
            rootLogger.addHandler(fileHandler)
        rootLogger.setLevel(logging.error)

        return logging.error(message)
