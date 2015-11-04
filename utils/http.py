from a801py import requests

class http():
    def post(self, urlto, urlfrom, cookies, data):
        headers = {
            "Referer": urlfrom
        }
        r = requests.post(urlto, headers=headers, data=data, cookies=cookies)
        self.result = r.text
