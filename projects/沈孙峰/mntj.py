import requests
dates={'name':'Alphonse','pwd':'123456'}
r=requests.post("http://holen1210.xyz/login.php",data=dates)
print(r.text)
print(r.headers)
