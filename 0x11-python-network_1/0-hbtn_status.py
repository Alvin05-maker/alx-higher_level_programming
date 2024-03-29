#!/usr/bin/python3
"""script that fetches resources from the internet using python"""
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content.decode('utf-8'))
    print ("\t- utf8 content:", utf8_content)
