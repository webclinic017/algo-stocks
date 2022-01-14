

def sendTelegramMessage(msg):
    import requests
    telegram_api_url = f"https://api.telegram.org/bot5030570649:AAFbGmcT4T72M_uhiBjy7pEgPi_Lk0j694Y/sendMessage?chat_id=@magnus_vn_algo&text={msg}"
    requests.get(telegram_api_url)