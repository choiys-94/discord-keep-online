# Discord Keep Online

## Change login_data
```python
def login():
    now = time.localtime()
    formatted_now = f"{now.tm_year}/{now.tm_mon}/{now.tm_mday} {now.tm_hour}:{now.tm_min}:{now.tm_sec}"

    login_data = {
        # your ID
        'login': '*****',
        # your PW
        'password': '******',
        'undelete': False,
        'captcha_key': None,
        'login_source': None,
        'gift_code_sku_id': None,
    }
    login_data = json.dumps(login_data)
```
Put your discord ID/PW in login_data

## Run
```bash
$ python discordbot.py
```