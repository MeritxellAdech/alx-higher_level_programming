#!/usr/bin/python3
""" Fetching data from a URL """
from urllib.request import urlopen, Request


if __name__ == "__main__":

    # getting the url
    url = "https://intranet.hbtn.io/status"
    # Requesting the URL
    req = Request(url)
    # Opening the request
    with urlopen(req) as response:
        result = response.read()
        print("Body response:")
        print(f"\t- type: {type(result)}")
        print(f"\t- content: {result}")
        print(f"\t- utf8 content: {result.decode()}")
