#coding: utf-8

import requests
import json
import time


requests.packages.urllib3.disable_warnings()

login_url = "https://discord.com/api/v8/auth/login"
online_url = "https://discord.com/api/v8/users/@me/settings"

header = {
    'Host': 'discord.com',
    'Connection': 'keep-alive',
    'Content-Length': '132',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg3LjAuNDI4MC44OCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiODcuMC40MjgwLjg4Iiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjczODA2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
    'X-Fingerprint': '791366782001872936.URbkW0ur36qYSCP29pNDfD7hVjo',
    'Accept-Language': 'ko',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Content-Type': 'application/json',
    'Authorization': 'undefined',
    'Accept': '*/*',
    'Origin': 'https://discord.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://discord.com/login?redirect_to=/channels/@me',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': 'locale=ko',
}

s = requests.Session()

def login():
    now = time.localtime()
    formatted_now = f"{now.tm_year}/{now.tm_mon}/{now.tm_mday} {now.tm_hour}:{now.tm_min}:{now.tm_sec}"

    login_data = {
        # your ID
        'login': '*****',
        # your PW
        'password': '*****',
        'undelete': False,
        'captcha_key': None,
        'login_source': None,
        'gift_code_sku_id': None,
    }
    login_data = json.dumps(login_data)

    r = s.post(login_url, headers=header, data=login_data, verify=False)
    print(r.text)
    try:
        Authorization = json.loads(r.text)["token"]
    except Exception as e:
        print(f"[-] Login Error! - {formatted_now}")
        print(e)
        exit(0)

    # Authorization
    header['Authorization'] = Authorization

    print(f"[*] Login Success! - {formatted_now}")

def keep_online():
    online_data = {
        'status': 'online',
    }
    online_data = json.dumps(online_data)

    r = s.patch(online_url, headers=header, data=online_data, verify=False)
    
    if r.status_code != 200:
        return False

    return True

def main():
    go = False
    while True:
        now = time.localtime()
        formatted_now = f"{now.tm_year}/{now.tm_mon}/{now.tm_mday} {now.tm_hour}:{now.tm_min}:{now.tm_sec}"
        hour = now.tm_hour

        if hour >= 10 and hour < 18:
            go = True
        else:
            go = False
            print(f"[-] It's not time to work. - {formatted_now}")
            time.sleep(300)
            # go = True
        
        if go:
            login()
            time.sleep(3)
            while True:
                time.sleep(300)
                # time.sleep(10)
                if keep_online() == False:
                    break

                now = time.localtime()

                print(f"[+] Keep Online! - {formatted_now}")


if __name__ == "__main__":
    main()