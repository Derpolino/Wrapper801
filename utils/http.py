from a801py import requests

class http():
    def post(self, url, referer, cookies, data):
        headers = { "Referer": referer }
        req = requests.post(url, headers=headers, data=data, cookies=cookies)
        self.result = req.text
        return req.status # Retourne le status de la requête.
