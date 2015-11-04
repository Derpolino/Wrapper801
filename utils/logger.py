import datetime, time

class Logger():
    # Fonction privee.
    def __log(self, log_type, message):
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M.%d")
        print ("[%s] [%s] %s" % (now, log_type.upper(), message))

    @staticmethod
    def info(self, message):
        self.__log("info", message)

    @staticmethod
    def debug(self, message):
        self.__log("debug", message)

    @staticmethod
    def warning(self, message):
        self.__log("warn", message)

    @staticmethod
    def error(self, message):
        self.__log("error", message)

    @staticmethod
    def critical(self, message):
        self.__log("critical", message)
