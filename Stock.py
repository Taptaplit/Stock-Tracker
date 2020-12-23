import tkinter as tk
import requests
from bs4 import BeautifulSoup

def StockTracker(entry):
    url = 'https://finance.yahoo.com/quote/' + str(entry)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    price = soup.find_all("div", {"class":"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text
    label['text'] = str(price)

root = tk.Tk()


canvas = tk.Canvas(root, width="10000", height="50000", bg="#af0fff")
canvas.pack()

frame = tk.Frame(root, bg="red", bd=5)
frame.place(relwidth=0.85, relheight=0.1, relx="0.5", rely="0.1", anchor="n")

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relwidth=0.30, relx=0.7, relheight=1)

entry = tk.Entry(frame, bg="purple", font=50)
entry.place(relwidth=0.65, relheight=1)

#lower fram

lower_frame = tk.Frame(root, bg="blue", bd=10)
lower_frame.place(relx = 0.5, rely=0.25, relwidth=0.65, relheight=0.25, anchor='n')

label = tk.Label(lower_frame, bg="red" ,font=50 )
label.place(relwidth=1, relheight=1)



root.mainloop()
