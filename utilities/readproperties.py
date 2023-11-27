import configparser

config = configparser.RawConfigParser()
config.read(".\\configrations\\config.ini")


class Readconfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getuseremail():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getinvalid_password():
        invalid_password = config.get('common info', 'invalid_password')
        return invalid_password
