import logging

class log_generator_class:

    @staticmethod
    def log_gen_method():
        log_file=logging.FileHandler(".\\Logs\\CredKart.log")
        #log format we are using--> Time Level Function Msg
        log_format=logging.Formatter('%(asctime)s -	%(levelname)s -	%(funcName)s - %(lineno)d - %(message)s')
        log_file.setFormatter(log_format)
        logger=logging.getLogger()
        logger.addHandler(log_file)
        logger.setLevel(logging.INFO)
        return logger
