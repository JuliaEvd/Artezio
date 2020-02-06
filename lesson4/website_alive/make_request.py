import requests


def make(s):
    re = requests.get(s)
    return re
