import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from tkinter import messagebox
import pyttsx3

# Tạo các đối tượng mặc định
root = Tk()
root.title("Chuyển Đổi Giọng Nói")
root.geometry("900x450")
root.resizable(0,0)
root.configure(bg="#305065")

# Xử lý các sự kiện
engine = pyttsx3.init()
def speak():
    text = text_area.get("1.0",'end-1c')
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices') # Set giọng nói nam or nữ

    def setVoice():
        if (gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()
    
    if (text):
        if (speed=="1.75"):
            engine.setProperty('rate',250)
            setVoice()
        elif (speed=="Normal"):
            engine.setProperty('rate',150)
            setVoice()
        else:
            engine.setProperty('rate',90)
            setVoice()
    else:
        messagebox.showerror("Error","You haven't write the text!!!")

def saveFile():
    text = text_area.get("1.0","end-1c")
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setVoice():
        if (gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            path = filedialog.asksaveasfilename(filetypes=(("Mp3 Files", "*.mp3"), ("WAV", "*.wav")),defaultextension=".mp3") #Hỏi Thư mục muốn chứa
            if (path):                                
                engine.save_to_file(text,path)
                engine.runAndWait()
            else:
                messagebox.showerror("Error","You didn\'t choose the folder yet!!! ")
        else:
            engine.setProperty('voice',voices[1].id)
            path = filedialog.asksaveasfilename(filetypes=(("Mp3 Files", "*.mp3"), ("WAV", "*.wav")),defaultextension=".mp3")
            if (path):
                engine.save_to_file(text,path)
                engine.runAndWait()
            else:
                messagebox.showerror("Error","You didn\'t choose the folder yet!!! ")
    
    if (text):
        if (speed=="1.75"):
            engine.setProperty('rate',250)
            setVoice()
        elif (speed=="Normal"):
            engine.setProperty('rate',150)
            setVoice()
        else:
            engine.setProperty('rate',90)
            setVoice()
    else:
        messagebox.showerror("Error","You haven't write the text!!!")

# Update method import file and save a import file
def openFile():
    text_file = filedialog.askopenfilename(title="Choose your text file",filetype=(("text file","*.txt"),))
    if (text_file):
        text_file = open(text_file,'r')
        stuff = text_file.read()
        text_area.delete("1.0",END)
        text_area.insert("1.0",stuff)
        text_file.close()
    else:
        messagebox.showerror("Error","You haven't choose the file yet!!!")

def ExportFile():
    text_file = filedialog.askopenfilename(title="Choose your text file to save",filetype=(("text file","*.txt"),))
    if (text_file):
        text_file = open(text_file,"w")
        text_file.write(text_area.get("1.0",END))

# set icon for app
img_icon = PhotoImage(file="./DoAnPython/img/speaklogo.png")
root.iconphoto(False,img_icon)

# Xử lý GUI phần header
top_header = Frame(root,bg="#778899",width=900,height=100)
top_header.place(x=0,y=0)

Logo_mic = PhotoImage(file="./DoAnPython/img/speakermic.png")
Label(top_header,bg="#778899",image=Logo_mic).place(x=0,y=0)

Label(top_header,bg="#778899",text="TEXT TO SPEECH",font="arial 20 bold",fg="black").place(x=100,y=30)

# Update Thanh cuon (Scrollpane)
# Xử lý GUI phần textArea
text_area = Text(root,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)
scroll = Scrollbar(text_area)
scroll.pack(side=RIGHT,fill=Y)
text_area.yscrollcommand = scroll.set #Text se cuon xuong khi truot thanh cuon
scroll.config(command=text_area.yview) #Thanh cuon se cuon xuong khi cuon Text
scroll.config(cursor="hand2")

# Xử lý GUI phần comboBox
Label(root,text="VOICE",bg="#305065",font="arial 16 bold",fg="white").place(x=580,y=160)
Label(root,text="SPEED",bg="#305065",font="arial 16 bold",fg="white").place(x=760,y=160)

gender_combobox = Combobox(root,values=["Male", "Female"],font="arial 14",state="r",width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set("Male")
gender_combobox.config(cursor="hand2")

speed_combobox = Combobox(root,values=["0.75", "Normal","1.75"],font="arial 14",state="r",width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set("Normal")
speed_combobox.config(cursor="hand2")

speakBtn = Button(root,text="SPEAK",compound=LEFT,image=img_icon,bg="#FF9999",width=120,font="arial 14 bold",padx=4,command=speak)
speakBtn.place(x=550,y=280)
speakBtn.config(cursor = "hand2")

img_save = PhotoImage(file="./DoAnPython/img/download.png")
saveBtn = Button(root,text="SAVE",compound=LEFT,image=img_save,bg="#39c790",width=120,font="arial 14 bold",padx=4,command=saveFile)
saveBtn.place(x=730,y=280)
saveBtn.config(cursor = "hand2")

importBtn = Button(root,text="Import",bg="#39c790",width=15,padx=4,font="arial 14 bold",command=openFile)
importBtn.place(x=600,y=370)
importBtn.config(cursor = "hand2")

root.mainloop()