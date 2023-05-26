import requests
import re

req = requests.get("http://ipconfig.kr")
out_addr = re.search(r ' IP Address : )', req.test)[1]
print(out_addr)