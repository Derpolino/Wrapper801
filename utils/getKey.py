from a801py import requests
import re

class getKey():
    def __init__(self, connected, JSESSIONID, url):
        if (connected == 1):
            cookies = {
                "JSESSIONID": JSESSIONID
            }
        else:
            cookies = {}

        r = requests.get(url, cookies=cookies)
        matches = re.search('<input type="hidden" name="(.*?)" value="(.*?)">', r.text)

        if (connected == 0):
            self.key1 = matches.group(1)
            self.key2 = matches.group(2)
            self.JSESSIONID = r.cookies['JSESSIONID']
        else:
            self.key1 = matches.group(1)
            self.key2 = matches.group(2)
            self.JSESSIONID = JSESSIONID
