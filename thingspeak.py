import http.client
import urllib
import time
import random

key = ""

while True:
    a = random.randint(0, 100)
    params = urllib.parse.urlencode({"field1": a, "key": key})
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params)
        response = conn.getresponse()
        print(a)
        print(response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print("connection failed")
        break
