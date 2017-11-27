import requests
datas={'name':'zt','pwd':'66661111'}
html = requests.post("http://holen1210.xyz/login.php",data=datas)
print(html.text)
print(html.headers)