import requests

def login_mstock(api_key, username, password):
    url = "https://api.mstock.com/login"
    payload = {
        "apiKey": api_key,
        "userId": username,
        "password": password
    }

    r = requests.post(url, json=payload, timeout=10)

    if r.status_code != 200:
        raise Exception("mStock login failed")

    return r.json()
