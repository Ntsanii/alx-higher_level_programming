#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as a parameter
"""

if __name__ == '__main__':
    from sys import argv
    from requests import post

    url = argv[1]
    email = argv[2]
    res = post(url, {'email': email})
    print(res.text)
