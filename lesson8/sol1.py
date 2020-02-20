import requests


def html(u):
    req = requests.get(u)
    return len(req.text)


url = "https://google.com"
print(html(url))
