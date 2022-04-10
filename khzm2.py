import time
import requests
from flask import Flask

app = Flask('')


@app.route('/')
def home():
    import socket
    time.sleep(5)
    print(2)
    s = requests.Session()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
    try:
        r = s.get('https://khzm1.herokuapp.com/',headers=headers)
    except:
        pass
    try:
        r = s.get('https://khzm3.herokuapp.com/',headers=headers)
    except:
        pass

    return "I'm alive"


def run():
    app.run(host='0.0.0.0', port=8080)


if __name__ == "__main__":
    app.run()
