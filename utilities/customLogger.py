import inspect
import logging

class LogGenerator:
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        log_file_path = r"D:\Projects_Fremwork\Alpha_Capital_User\Logs\ALPHA_CAPITAL_AUTOMATION.log"
        logfile = logging.FileHandler(log_file_path)
        log_format = logging.Formatter(" %(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        logfile.setFormatter(log_format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger