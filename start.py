import os
import subprocess
from importlib.resources import path
import threading
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from cgitb import reset
import secrets
import time
import gspread
import colorama
from colorama import Fore, Back, Style
print(Style.BRIGHT + Fore.RESET + "Welcome To Ramgadiya Program")
print(Style.BRIGHT + Fore.RESET +
      "Contact us on Whatsapp For Software Activation +91 8059199600")
print(Style.BRIGHT + Fore.RESET +
      "Visit Site for More detail https://ramgadiya.com")
colorama.init(autoreset=True)

config = configparser.ConfigParser()
config.read('config.ini')
PROXY = [  "192.99.101.142:7497",
    "198.50.198.93:3128",
    "52.188.106.163:3128",
    "20.84.57.125:3128",
    "172.104.13.32:7497",
    "172.104.14.65:7497",
   "165.225.220.241:10605",
    "165.225.208.84:10605",
    "165.225.39.90:10605",
    "165.225.208.243:10012",
    "172.104.20.199:7497",
    "165.225.220.251:80",
    "34.110.251.255:80",
    "159.89.49.172:7497",
    "165.225.208.178:80",
    "205.251.66.56:7497",
    "139.177.203.215:3128",
    "64.235.204.107:3128",
    "165.225.38.68:10605",
    "165.225.56.49:10605",
    "136.226.75.13:10605",
    "136.226.75.35:10605",
    "165.225.56.50:10605",
    "165.225.56.127:10605",
    "208.52.166.96:5555",
    "104.129.194.159:443",
    "104.129.194.161:443",
    "165.225.8.78:10458",
    "5.161.93.53:1080",
    "165.225.8.100:10605",]


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument(f'user-agent={user_agent}')
options.add_experimental_option("detach", True)
options.add_argument("--window-size=1920,1080")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-infobars")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--use-fake-device-for-media-stream")
options.add_argument("--start-maximized")


count = 0
number = 3
meet_code = config['ZOOM']['Meeting_ID']
passcode = config['ZOOM']['Meeting_Pass']
sec = config['ZOOM']['Member_Hold_Time']

def driver_wait(driver, locator, by, secs=5, condition=EC.element_to_be_clickable):
    wait = WebDriverWait(driver=driver, timeout=secs)
    element = wait.until(condition((by, locator)))
    return element


lis = ['Mohammed UAE',
'Victor Sam',
'SENTHILKUMAR DUBAI',
'Tamilarasan',
'NAWAZ KHALEEL',
'Samimii',
'PEER MOHAMMAD',
'L Krishnakumar',
'Yuvanathan',
'MANJU',
'Muthubabu',
'Christopher Asir Dass',
'KITTY',
'Prabhakar',
'Neranjan',
'Muralidhar',
'S ANANYA',
'Anushka',]



n = 0
def fun(n, count):
    p = PROXY[count]
    if p is not None:
        options.add_argument(f"--proxy-server={p}")
    driver = webdriver.Chrome('chromedriver', options=options)
    return driver
    
    wait_time = sec * 60
    
    driver.get(f'https://zoom.us/wc/join/{meet_code}')

    

    wait.until(EC.presence_of_element_located((By.ID, "inputname")))
    
    inp = driver.find_element(by='id', value='inputname')

    
    inp.send_keys(f"{lis[n]}")
    time.sleep(1)

    
    wait.until(EC.presence_of_element_located((By.ID, "joinBtn")))
    btn2 = driver.find_element(by='id', value='joinBtn')
    

    try:
        elem = driver.find_element(
            by='id', value='onetrust-accept-btn-handler')
        elem.click()
        time.sleep(1)
    except NoSuchElementException:
        pass

    try:
        elem = driver.find_element(by='id', value='wc_agree1')
        elem.click()
    except NoSuchElementException:
        pass

    
    wait.until(EC.presence_of_element_located((By.ID, "inputpasscode")))
    inp2 = driver.find_element(by='id', value='inputpasscode')
    # time.sleep(1)
    inp2.send_keys(passcode)
    wait.until(EC.presence_of_element_located((By.ID, "joinBtn")))
    btn3 = driver.find_element(by='id', value='joinBtn')
   # time.sleep(1)
    btn3.click()
   

    count += 1
    if count == 30:
        count = 0
    # n+=1
    # time.sleep(2)


while n < number:
    a = threading.Thread(target=fun, args=(n, count,))
    a.start()
    n += 1
    time.sleep(20)

input()
