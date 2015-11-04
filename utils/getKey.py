import requests
from utils import http
import re

class getKey():
    def __init__(self, connected, session_id, url):
        if (connected == True):
            cookies = { "JSESSIONID": session_id }
        else:
            cookies = {}

        res = http.get(url, cookies=cookies)
        matches = re.search('<input type="hidden" name="(.*?)" value="(.*?)">', res)

        if (connected == False):
            self.key1 = matches.group(1)
            self.key2 = matches.group(2)
            self.JSESSIONID = r.cookies['JSESSIONID']
        else:
            self.key1 = matches.group(1)
            self.key2 = matches.group(2)
            self.JSESSIONID = session_id
