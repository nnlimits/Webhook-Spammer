#pen file in python
import requests
import threading

url = input("webhook url:")
payload = """

message

"""

def function():
    requests.post(url,json={'content': payload})

while True:
    t = threading.Thread(target=function)
    t.start()
