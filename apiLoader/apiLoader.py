from itertools import count
from urllib import response
import requests
from concurrent.futures import ThreadPoolExecutor
import time
import random
start = time.time()

def devicenamegen():
    devicesNames =[]
    a = random.choice(devicesNames)
    return [
        #add json data here
    ]

def post_url(args):
    payload  = devicenamegen()
    headers ={
        #add headers here
    }
    return requests.post(args[0], headers = headers,  json = payload)

form_data ={
    "o":"oi"
}

counts = 60  # number of requests to be made to endpoint 

urls = [("https://api.com/endpoint", form_data)]*count

with ThreadPoolExecutor(max_workers=3) as pool:
    response_list = list(pool.map(post_url,urls ))


for response in response_list:
    print(response)
end = time.time()
#print(response.text)

print(end-start)