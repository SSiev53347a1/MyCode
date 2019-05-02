#!/usr/bin/env python3
import requests

def main():
    r = requests.get('https://frederick.craigslist.org/d/free-stuff/search/zip')
    print(r.text)
    print(dir(r)) 
main()

