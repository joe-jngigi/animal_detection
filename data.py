# This is a pyhton script that can be used to download or get requests kust like curl/wget
import requests

url="https://www.kaggle.com/louise2001/quantum-physics-articles-on-arxiv-1994-to-2009/download"

r = requests.get(url)

r.headers
