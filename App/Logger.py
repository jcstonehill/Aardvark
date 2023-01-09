import os
import datetime

class Log:
    filePath: str
    debugMode: bool

    @classmethod
    def Create(cls, debugMode: bool = False):
        cls.debugMode = debugMode
        date = datetime.date.today()

        year = str(date.year)
        month = str(date.month)
        day = str(date.day)

        currentTime = datetime.datetime.now()
        currentTime = currentTime.strftime("%H%M%S")

        cls.filePath = os.getcwd() + '\\Logs\\' + year + '_' + month + '_' + day + '_' + currentTime + '.log'

        with open(cls.filePath, 'a') as f:
            f.write('')
        
    @classmethod
    def Info(cls, message: str):
        messageType: str = 'INFO'

        cls.__WriteMessageToFile(message, messageType)

    @classmethod
    def Debug(cls, message: str):
        if(cls.debugMode):
            messageType: str = 'DEBUG'

            cls.__WriteMessageToFile(message, messageType)

    @classmethod
    def Warning(cls, message: str):
        messageType: str = 'WARNING'

        cls.__WriteMessageToFile(message, messageType)
    
    @classmethod
    def Error(cls, message: str):
        messageType: str = 'WARNING'

        cls.__WriteMessageToFile(message, messageType)

    @classmethod
    def __WriteMessageToFile(cls, message: str, messageType: str):
        currentTime = datetime.datetime.now()
        currentTime = currentTime.strftime("%H.%M.%S")

        line = 'App' + ' : ' + currentTime + ' : ' + messageType + ' : ' + message + '\n'

        with open(cls.filePath, 'a') as f:
            f.write(line)