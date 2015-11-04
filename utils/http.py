import requests
import logger

class http():
    @staticmethod
    def post(self, url, referer, cookies, data):
        headers = { "Referer": referer }
        Logger.debug("Sending POST request to %s" % url)
        Logger.debug("--- Referer: %s" % referer)
        req = requests.post(url, headers=headers, data=data, cookies=cookies)
        return req.text

    @staticmethod
    def get(self, url, cookies):
        Logger.debug("Sending GET request to %s" % url)
        req = requests.get(url, headers=headers, cookies=cookies)
        return req.text
