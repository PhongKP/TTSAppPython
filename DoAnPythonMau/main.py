from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather Forcast")
root.geometry("900x500+300+200")
root.resizable(False,False)

def get_weather ():
    try:
        city = textfiled.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        res = obj.timezone_at(lng=location.longitude,lat=location.latitude)

        home = pytz.timezone(res)
        local_time = datetime.now(home)
        current = local_time.strftime("%I:%M %p")
        clock.config(text=current)
        name.config(text="CURRENT WEATHER")

        api = "https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid=b0331e7ea775bbc793cb2ac9328ee48e"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        descrip = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humiditty']
        wind = json_data['wind']['speed']

        t.config(text=(temp,"Độ"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"Độ"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=descrip)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather App","Invalid Input!!!")

#search box
search_img = PhotoImage(file="./DoAnPythonMau/img/search.png")
myimg = Label(image=search_img)
myimg.place(x=20,y=20)

textfiled = tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),border=0,bg="#404040",fg="white")
textfiled.place(x=50,y=40)
textfiled.focus()

search_icon = PhotoImage(file="./DoAnPythonMau/img/search_icon.png")
myimg_icon = Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040")
myimg_icon.place(x=400,y=34)

#Logo
logo_img = PhotoImage(file="./DoAnPythonMau/img/logo.png")
logo = Label(image=logo_img)
logo.place(x=150,y=100)

#Infor Box
frame_img = PhotoImage(file="./DoAnPythonMau/img/box.png")
frame_myimg = Label(image=frame_img)
frame_myimg.pack(padx=5,pady=5,side=BOTTOM)

#Time
name = Label(root,font="arial,15,bold")
name.place(x=30,y=100)
clock = Label(root,font="Helvetica,20")
clock.place(x=30,y=130)

#Label infor
label1 = Label(root,text="WIND",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2 = Label(root,text="HUMIDTY",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)

label3 = Label(root,text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4 = Label(root,text="PRESSURE",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

t = Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c = Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w = Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h = Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)
d = Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=490,y=430)
p = Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=700,y=430)

root.mainloop()