import tkinter as tk
import requests
from bs4 import BeautifulSoup


def StockTracker(entry):
    url = 'https://finance.yahoo.com/quote/' + str(entry)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    price = soup.find_all("div", {"class":"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text
    label['text'] = str(price)
    

    


