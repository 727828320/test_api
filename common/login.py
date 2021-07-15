import pytest
import requests


@pytest.fixture(scope='module')
def company_login_token():
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    data = {
        "corpid":"ww257577244a96bd33",
        "corpsecret":"zHiVxtcvQwte9XtJ5ITpYCqSxoO_PUwc6l2t9DR_6d4"
    }
    r = requests.post(url=url, json=data)
    print(r)
    return str(r.json()['access_token'])

