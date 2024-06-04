from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_authenticated_proxy import SeleniumAuthenticatedProxy
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
from proxy_credenciales import proxy,proxy_url,proxy_host, proxy_password, proxy_username


import requests, time
from datetime import datetime

def extraer_fecha(cadena):
    temp=""
    for i in range(len(cadena)-1,-1,-1):
        if(cadena[i]=="_"): return temp
        temp=cadena[i]+temp

def get_item(cadena):
    retornar=""
    temp=0
    bloqueo='collectionitem="'
    for i in range(len(cadena)):
        if(temp==len(bloqueo)):
            if(cadena[i]=='"'):
                if(len(retornar)==0): 
                    temp=0
                    continue
                else: return retornar
            retornar+=cadena[i]  
        else:
            if(cadena[i]==bloqueo[temp]): temp+=1
            else: temp=0

def req_betway():

    chrome_options = Options()
    
    chrome_options.set_capability(
            "goog:loggingPrefs", {"performance": "ALL"}
        )

    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")  # This is important for some versions of Chrome
    chrome_options.add_argument("--remote-debugging-port=9222")  # This is recommended
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-size=1920,1080")


    proxy_helper = SeleniumAuthenticatedProxy(proxy_url=proxy_url)
    proxy_helper.enrich_chrome_options(chrome_options)

    chrome_options.binary_location = "/opt/chrome/chrome-linux64/chrome"

    # Set path to ChromeDriver
    chrome_service = ChromeService(executable_path="/opt/chromedriver/chromedriver-linux64/chromedriver")

    # Set up driver
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    driver.get("https://betway.com/es/sports/sct/soccer/copa-america-2024")
    #driver.get("http://example.com")
    
    #print("Estoy aqui")

    time.sleep(12)
    
    #print(driver.page_source)

    actions = ActionChains(driver)

    css_selector="""div[data-tap-recogniser="true"].cookiePolicyAcceptButton"""

    element = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
    )

    element.click()

    time.sleep(15)

    sopa = BeautifulSoup(driver.page_source, "html.parser")
    div_elementos=sopa.find_all('div',{'data-widget':"""EventTableListWidget[soccer_copa-america-2024_matches, soccer_copa-america-2024_matches]""",'class':"eventTableItemCollection"})
    div_elementos=div_elementos[0].find_all('div', recursive=False)

    print("LISTO",len(div_elementos))

    for i in range(3,len(div_elementos)):
        
        item=get_item(str(div_elementos[i]))
        
        element = driver.find_element(By.CSS_SELECTOR,f"""div[collectionitem="{item}"].collapsablePanel""")
        actions.move_to_element(element).click().perform()
        print(i)

        time.sleep(2)

    sopa = BeautifulSoup(driver.page_source, "html.parser")
    arr=[]

    for i in div_elementos:
        
        fecha=extraer_fecha(get_item(str(i)))
        
        partidos=sopa.find_all('div',{'data-tap-recogniser':"true",'class':"eventItemCollection","data-widget":f"EventListWidget[soccer_copa-america-2024_matches, {fecha}]"})
        partidos_ids=partidos[0].find_all('div', recursive=False)

        for j in partidos_ids:
            
            extraer_id=get_item(str(j))
            nombres=j.find('div',{'class':"oneLineScoreboard soccer upcoming","data-widget":f"EventSummaryWidget[soccer_copa-america-2024_matches, {extraer_id}]"})
            
            home=nombres.find('span',{'class':"teamNameFirstPart teamNameHomeTextFirstPart"}).text
            away=nombres.find('span',{'class':"teamNameFirstPart teamNameAwayTextFirstPart"}).text

            cuotas=j.find_all('div',{'class':"odds"})

            print()
            print(home,cuotas[0].text)
            print("X",cuotas[1].text)
            print(away,cuotas[2].text)
            print()

            arr.append([str(datetime.now()),home,away,cuotas[0].text,cuotas[1].text,cuotas[2].text])
    
    return arr

#req_betway()