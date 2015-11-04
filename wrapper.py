from utils import *

class wrapper:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.connected = 0
        self.JSESSIONID = "X"
    def connect(self):
        key = getKey(self.connected, self.JSESSIONID, "http://atelier801.com")
        self.JSESSIONID = key.JSESSIONID
        data = {
            "rester_connecter": "on",
            "id": self.username,
            "pass": self.password,
            key.key1: key.key2
        }
        cookies = {"JSESSIONID" : self.JSESSIONID}
        connect = http()
        connect.post("http://atelier801.com/identification","http://atelier801.com/", cookies, data)
        if (connect.result == '{"redirection":"http://atelier801.com/"}'):
            print('[BOT] CONNECTED !')
            self.connected = 1
        else:
            print('[BOT] ERROR WITH CONNECTION ! ERROR : ' + connect.result)

    def disconnect(self):
        if(self.connected == 1):
            key = getKey(self.connected, self.JSESSIONID, "http://atelier801.com")
            self.JSESSIONID = key.JSESSIONID
            data = {key.key1: key.key2}
            cookies = {"JSESSIONID" : self.JSESSIONID}
            connect = http()
            connect.post("http://atelier801.com/deconnexion","http://atelier801.com/", cookies, data)
            if (connect.result == '{"redirection":"http://atelier801.com/"}'):
                print('[BOT] DISCONNECTED !')
            else:
                print('[BOT] ERROR WITH DECONNECTION ! ERROR : ' + connect.result)
        else:
            print('[BOT] ERROR : YOU ARE NOT CONNECTED')
