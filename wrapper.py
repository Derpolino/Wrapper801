from utils import *

class wrapper:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.connected = False
        self.JSESSIONID = "X"
    def connect(self):
        if(self.connected == True):
            Logger.error("You are already connected. Please start another instance.")
            return

        key = getKey(self.connected, self.JSESSIONID, "http://atelier801.com")
        self.JSESSIONID = key.JSESSIONID
        data = {
            "rester_connecter": "on",
            "id": self.username,
            "pass": self.password,
            key.key1: key.key2
        }
        cookies = {"JSESSIONID" : self.JSESSIONID}
        res = http.post("http://atelier801.com/identification","http://atelier801.com/", cookies, data)
        if (res == '{"redirection":"http://atelier801.com/"}'):
            Logger.info("Bot connected.")
            self.connected = True
        else:
            Logger.error("Connection error: " + res)

    def disconnect(self):
        if(self.connected == True):
            key = getKey(self.connected, self.JSESSIONID, "http://atelier801.com")
            self.JSESSIONID = key.JSESSIONID
            data = {key.key1: key.key2}
            cookies = {"JSESSIONID" : self.JSESSIONID}

            res = http.post("http://atelier801.com/deconnexion","http://atelier801.com/", cookies, data)
            if (res == '{"redirection":"http://atelier801.com/"}'):
                Logger.info("Bot disconnected.")
            else:
                Logger.error("Connection error: " + res)
        else:
            Logger.error("You must be connected in order to disconnect.")
    def post(self,message):
        #Todo: finish this
        #not tested !!
        if(message.type==0):
            if(self.connected == True):
                key = getKey(self.connected, self.JSESSIONID, "http://atelier801.com/new-dialog")
                self.JSESSIONID = key.JSESSIONID
                data = {
                    "destinataire": message.to,
                    "objet": message.object,
                    "message": message.message,
                    key.key1: key.key2
                }
                cookies = {"JSESSIONID" : self.JSESSIONID}
                res = http.post("http://atelier801.com/new-dialog","http://atelier801.com/create-dialog", cookies, data)
                if (res.text[:14] == '{"redirection"'):
                    Logger.info("Message sent")
                else:
                    Logger.error("Error while sending the message. Error : " + res.text)
            else:
                Logger.error("You must be connected to send an mp.")
