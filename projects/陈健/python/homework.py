import requests

params={'name':'Sliver','pwd':'123456'}
r = requests.post("http://holen1210.xyz/login.php",params)
print(r.text)
