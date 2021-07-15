import requests


class ApiRequest:
    def send_requests(self, method, url, data=None, params=None, headers=None, json=None):
        self.res = requests.request(method=method, url=url, data=data, params=params, headers=headers, json=json)
        return self.res
