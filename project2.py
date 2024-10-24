from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import pandas as pd



cService = webdriver.ChromeService(executable_path=r'C:\Users\GLB90110533\Selenium\chromedriver.exe')
browser = webdriver.Chrome(service = cService)

browser.get("https://www.google.com/search?sca_esv=b3942a88c7b3824f&sxsrf=ADLYWIIeGI5vJQe7rSWZJDa2eLOFGX6oBA:1729768245946&q=t%C3%BCrkiye+tarihi+parklar&udm=1&fbs=AEQNm0CgMcZ11KbHg1uunEmuo39Lar3d3J3AG9BqLST8B8Q0277R0vH1pQytave8a5cbxsNScjjxKmCA6REpNDHV3iaXPGdPCWNw8ZVHF8lJTa76YRYSpo9e91LE8_Cnw7qbrwa-l6sM6Fag3DzJJMElIxjeInKmmcoNL9ii351omLAabMfPO_1jJ3iXAMy6L4_ExEJv96ZNuf9jJtHI8ZFuUl8MHR0P228dVgAlA992dr77DlxPvj4&sa=X&ved=2ahUKEwiYot_u8KaJAxX2QvEDHQxVEZAQs6gLegQIEhAB&biw=1280&bih=639&dpr=1.5#vhid=/g/11b60sz996&vssid=rllrl")
time.sleep(0.25)

kaynak = browser.page_source
soup = BeautifulSoup(kaynak, "html.parser")

metinler = soup.find_all("div",attrs={"class":"dbg0pd nbVM1d"})

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

    metinler = soup.find_all("div", attrs={"class": "dbg0pd nbVM1d"})
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
excel.to_excel("makaleler2.xlsx")       # install openpyxl
