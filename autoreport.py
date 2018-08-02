import pyautogui
#import webbrowser
from selenium import webdriver



websitelogin = "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1531173297&rver=6.7.6640.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d1a072b0a-f278-99fe-c620-f41edc9eae69&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015"

#to read email list and proxies list
F = open("report.txt","r")
proxies = open("proxy.txt","r")
list = F.readlines()
PROXY = proxies.readlines()
count = 0
countproxy = 0
NumProxy = 0
for word in list:
    if "\n" in word:
        list[count] = word[:len(word)-1]
    count+=1

for prox in PROXY:
    if "\n" in prox:
        PROXY[countproxy] = prox[:len(prox)-1]
    countproxy+=1
    print(prox)
    




def disconnect():
    while(pyautogui.locateOnScreen('disconnect.png')==None):
        print("waitdisconnect")
    valuedisc = pyautogui.locateOnScreen('disconnect.png')
    pyautogui.moveTo(valuedisc[0]+68, valuedisc[1], 0.25)
    pyautogui.click()
    pyautogui.moveTo(valuedisc[0]-234, valuedisc[1]+350, 0.25)
    pyautogui.click()


def RevSpam(x, y):
    pyautogui.PAUSE = 0.25
    pyautogui.moveTo(x, y)
    pyautogui.click()
    pyautogui.moveTo(x, y-179, 0.15)
    pyautogui.click()
    pyautogui.moveTo(x, y-134)
    pyautogui.click()


def openemail(index):
    while(pyautogui.locateOnScreen('sign infast.png')==None):
        print("wait signin")
    valuesignIN = pyautogui.locateOnScreen('sign infast.png')
    pyautogui.moveTo(valuesignIN[0]+185, valuesignIN[1]+54, 1)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('del')
    pyautogui.typewrite(list[index], interval=0.1)
    pyautogui.press('enter')
    while(pyautogui.locateOnScreen('psw.png')==None):
        print("wait psw")
    pyautogui.typewrite(list[index+1], interval=0.1)
    pyautogui.press('enter')
    while(pyautogui.locateOnScreen('spm.png')==None):
        print("wait spam")
    valuecorrierinde = pyautogui.locateOnScreen('spm.png')
    pyautogui.moveTo(valuecorrierinde[0], valuecorrierinde[1])
    pyautogui.click()
    return valuecorrierinde
    
def ReOpen():
    while(pyautogui.locateOnScreen('msn.png')==None):
        print("wait close")
    pyautogui.hotkey('alt', 'f4')



########################################
# IP:PORT or HOST:PORT

#i is the index of the email in the list and i+1 is its password
for i in range(0,len(list),2):
    #chrome proxy changer
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--proxy-server=http://%s' % PROXY[NumProxy])
    chrome_options.add_argument("--start-maximized")
    NumProxy += 1
    chrome = webdriver.Chrome(chrome_options=chrome_options)
    chrome.get(websitelogin)
    #using fonctions we define
    coord = openemail(i)
    while(pyautogui.locateOnScreen('videfast.png')==None):
        RevSpam(coord[0]+457, coord[1]-267)
    disconnect()
    ReOpen()











