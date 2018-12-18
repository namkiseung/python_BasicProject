import requests

res = requests.get("chrome://history/")
print res.content
