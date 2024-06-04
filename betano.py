import requests
from datetime import datetime
from proxy_credenciales import proxy

def req_betano():

    #print(proxy)

    arr=[]


    cabeza={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Host":"www.betano.pe"
    }

    cabeza = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Cookie": "cf_clearance=XKDcabSSLUj_TxEMg2rwKFy1UwAj2MBDJKZx0Nw4Qc8-1716881166-1.0.1.1-mANsFiF_q_L6FSJ3t8syJP3lwZ0bpY4LTXYinQste33VsMiQtbERw7G4Z.bKoMUv5b6w8rsAD4xpJcCULNvVCg; OptanonConsent=isGpcEnabled=0&datestamp=Tue+May+28+2024+02%3A32%3A18+GMT-0500+(Colombia+Standard+Time)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=ff8d580b-bd07-4065-8f63-37cce55ef5b1&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A0%2CC0004%3A0%2CC0002%3A0&geolocation=PE%3BLMA&AwaitingReconsent=false; datadome=YeZdyPITEidA0Sz~Y5vlVIP~vMqV8a7OzT~pkN~Gcln16Eo9ARgvFf5VJyNWafK3Wh7u3KzF6KITv8F9Zpk7cTkRZ5bKoZuksEVjmerbU983Vk0JzCuxiF8PbKAdUIb2; _fbp=fb.1.1716881169233.1019164396; MgidSensorNVis=1; MgidSensorHref=https://www.betano.pe/sport/futbol/campeonatos/copa-america/188650/; _ga=GA1.1.1731938543.1716881169; _gcl_au=1.1.606654159.1716881169; _ga_RMMH28YC0F=GS1.1.1716881168.1.1.1716882104.60.0.0; _ga_SJLCV23YJW=GS1.1.1716881168.1.1.1716882104.0.0.1794420839; OptanonAlertBoxClosed=2024-05-28T07:26:11.345Z",
    "Host": "www.betano.pe",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "TE": "trailers",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0"
    }


    q=requests.get("https://www.betano.pe/api/sport/futbol/campeonatos/copa-america/188650/?req=la,s,stnf,c,mb,mbl",headers=cabeza,proxies=proxy)
    
    print(q.status_code)
    
    data=q.json()

    for i in data["data"]["blocks"][0]["events"]:
        print("-"*50)

        for j in i["markets"][0]["selections"]:
            print(j["fullName"],j["price"])
        

        arr.append([str(datetime.now()),i["markets"][0]["selections"][0]["fullName"],i["markets"][0]["selections"][2]["fullName"],i["markets"][0]["selections"][0]["price"],i["markets"][0]["selections"][1]["price"],i["markets"][0]["selections"][2]["price"]])
        #print(i["name"])
        print("-"*50)

    return arr

#req_betano()