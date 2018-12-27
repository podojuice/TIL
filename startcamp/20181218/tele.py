import requests


MY_CHAT_ID ='675764478'
msg = 'happyhacking'
BOT_TOKEN = '787984297:AAGQMAwoHF9W1GJSfcuJaJSeHA1fSNgc-4U'
url = 'api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(BOT_TOKEN, MY_CHAT_ID, msg)

response = requests.get(url)
print(response.json())