
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import pandas as pd



cService = webdriver.ChromeService(executable_path=r'C:\Users\GLB90110533\Selenium\chromedriver.exe')
browser = webdriver.Chrome(service = cService)

browser.get("https://www.google.com/search?sca_esv=f3c510255100d4e3&sxsrf=ADLYWILSQwFeGYFuJlYO2G43fdlkdHiGFg:1729635154574&q=kad%C4%B1k%C3%B6y+pub+mekanlar%C4%B1&udm=1&fbs=AEQNm0AgNL97A_985v2UtF2-8qNLAQdEvmmuSnz_oboHmd7dsMokucL2dhGVgCyKMts2D6ffq6g7hEKmnf8h3J21I9svZdInJ9Uq-ujSz2B1FztyQNNtsU6R3cgz_-OZJ03-75lCYAwwSdPCtGvafZkgwxun0IfMT1W4vn3OLoR8faKTk5muYBaoKngdxMpwu_j95HxYKVsp28o-DL7SdgATIx6-VTmsm5Kwx9sDKHi53ygVi8o--pE&sa=X&ved=2ahUKEwiHyOqHgaOJAxXzVfEDHcFMMcgQs6gLegQIEBAB&biw=1280&bih=639&dpr=1.5#vhid=/g/1hc23ng0f&vssid=rllrl")
time.sleep(0.25)

kaynak = browser.page_source
soup = BeautifulSoup(kaynak, "html.parser")

metinler = soup.find_all("div",attrs={"class":"uMdZh tIxNaf alUjuf"})

liste = []

for metin in metinler:
    #baslik = metin.find("span", attrs={"class": "hlFld-Title"}).text
    baslik = metin.find("span", attrs={"class": "OSrXXb e62wic"}).text
    liste.append([baslik])




sonraki_sayfa_butonu = soup.find("table", class_="AaVjTc")

for a in sonraki_sayfa_butonu.find_all('a', href=True):
    sonraki_sayfa_linki = a['href']
    print(sonraki_sayfa_linki)

browser.get("https://www.google.com/" + sonraki_sayfa_linki)

p = 0

while p < 10:
    browser.get("https://www.google.com/" + sonraki_sayfa_linki)
    kaynak = browser.page_source
    soup = BeautifulSoup(kaynak, "html.parser")

    metinler = soup.find_all("div", attrs={"class": "uMdZh tIxNaf alUjuf"})
    for metin in metinler:
        # baslik = metin.find("span", attrs={"class": "hlFld-Title"}).text
        baslik = metin.find("span", attrs={"class": "OSrXXb e62wic"}).text
        liste.append([baslik])

    sonraki_sayfa_butonu = soup.find("table", class_="AaVjTc")
    for a in sonraki_sayfa_butonu.find_all('a', href=True):
        sonraki_sayfa_linki = a['href']
        print(sonraki_sayfa_linki)

    p = p + 1


excel = pd.DataFrame(liste)           # install pandas
excel.columns=["Wuhuuuuuuuu"]
excel.to_excel("makaleler.xlsx")       # install openpyxl






