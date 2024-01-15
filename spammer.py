from pyautogui import typewrite, press
from time import sleep
from customtkinter import CTk, CTkFrame,CTkButton, CTkLabel, CTkEntry,CTkOptionMenu, set_appearance_mode, set_default_color_theme, CTkImage
# from tkinter import Button, Entry, Label, Message,Tk, messagebox
# from tkinter import ttk
from PIL import Image
from tkinter import messagebox
from time import strftime
from webbrowser import open
from pyperclip import copy

linktop = 'https://github.com/abray87/spammer-bot'

global speed_rate 
global start_time
start_time = "start"
speed_rate = 50

def setting():
    # --------------------------------------- GUI SETTING ---------------------------------------
    set_appearance_mode('dark')
    set_default_color_theme('blue')
    sroot = CTk()
    sroot.title("SETTING")
    sroot.geometry("450x330")
    sroot.resizable(False, False)
    sframe = CTkFrame(master=sroot, border_width=2, corner_radius=10, border_color="red")
    sframe.pack(pady=20, padx=20, expand=True, fill="both")
    # ---------------------------------------   func SETTING   ---------------------------------------
    def  set_change():
        if speedoption.get() == 'Super Fast (50ms)':
            speed_rate = 0.05
        elif speedoption.get() == 'Fast (100ms)':
            speed_rate = 0.01
        elif speedoption.get() == 'Medium (250ms)':
            speed_rate = 0.25
        elif speedoption.get() == 'Slow (500ms)':
            speed_rate = 0.5
        if timeentry.get() == "":
            if len(timeentry.get()) == 0:
                start_time = "start"
            elif len(timeentry.get()) == 8:
                if timeentry.get()[3] and timeentry.get()[5] == ":":
                    start_time = timeentry.get()
                else:
                    messagebox.showerror("Incorrect format !")
            else:
                messagebox.showerror("Incorrect format !")



            
    # --------------------------------------- ELEMENTS SETTING ---------------------------------------
    settinglbl = CTkLabel(master=sframe, text="SETTING", font=("montserrat", 27, "bold"))
    speedlbl = CTkLabel(master=sframe, text="Speed :", font=("montserrat", 22, "bold"))
    speedoption = CTkOptionMenu(
                                master=sframe, 
                                values=['Super Fast (50ms)','Fast (100ms)', 'Medium (300ms)', 'Slow (500ms)'],
                                font=("montserrat", 15, "bold"),
                                width=190, height=35
                                )
    starttime = CTkLabel(master=sframe, text="Schedule :", font=("montserrat", 22, "bold"))
    timeentry = CTkEntry(master=sframe, placeholder_text="18:10:35", font=("montserrat", 22, "bold"), width=190)
    setchange = CTkButton(master=sframe, text="SET CHANGE", font=("montserrat", 15, "bold"), width=200)
    sexit = CTkButton(master=sframe, text="EXIT", font=("montserrat", 15, "bold"), width=200, hover_color="red", command=lambda : sroot.destroy())

    settinglbl.place(x=145, y=15)
    speedlbl.place(x=40, y=90)
    speedoption.place(x=190, y=90)
    starttime.place(x=40, y=135)
    timeentry.place(x=190, y=135)
    setchange.place(x=108, y=210)
    sexit.place(x=108, y=245)
    sroot.mainloop()
# setting()
def spam():

    if start_time == "start":
        textv = text.get()
        numv = int(num.get())
        sleep(5)
        for a in range(numv):
            typewrite(textv)
            press("enter")
            sleep(speed_rate)        
    else:
        if strftime("%H:%M:%S") == start_time :
            textv = text.get()
            numv = int(num.get())
            sleep(5)
            for a in range(numv):
                typewrite(textv)
                press("enter")
                sleep(speed_rate)  # delay
        else:
            sleep(1)
def  sharep():
    copy(linktop)
    messagebox.showinfo("Share this Project", "Thanks for Sharing this project, The link has been copied to your clipboard !")
def donate():
    copy("TV59qxTsCocxEK8jeHnf6WmbcuwUB2uUPE")
    messagebox.showinfo("Donate", "If you want to support me, my Tron address has been copied to your clipboard !")
#--------------------------------------- data -----------------------------------

path1 = r"C:\Users\Abolfazl\Desktop\n-p\1.png"
photo1 = CTkImage(Image.open(path1), size=(32,32))

path2 = r"C:\Users\Abolfazl\Desktop\n-p\5.png"
photo2 = CTkImage(Image.open(path2), size=(32,32))

path3 = r"C:\Users\Abolfazl\Desktop\n-p\8.png"
photo3 = CTkImage(Image.open(path3), size=(30,30))

path4 = r"C:\Users\Abolfazl\Desktop\n-p\7.png"
photo4 = CTkImage(Image.open(path4), size=(30,30))

#------------------------------------------- GUI ------------------------------------------- 
set_appearance_mode('dark')
set_default_color_theme('blue')
root = CTk()
root.title("SPAMMER")
root.geometry("350x450")
root.resizable(False, False)
frame = CTkFrame(master=root, border_width=2, corner_radius=10, border_color="red")
frame.pack(pady=20, padx=20, expand=True, fill="both")
# --------------------------------- lbl | btn ---------------------------------
spam_lbl = CTkLabel(frame, text="Spammer", font=("montserrat", 27, "bold"), bg_color='transparent', text_color="white")
txt_lbl = CTkLabel(frame, text="Text :", font=("montserrat", 20, "bold"), bg_color='transparent', text_color="white")
text = CTkEntry(master=frame, placeholder_text="Text", height=35, font=("montserrat", 15))
num_lbl = CTkLabel(frame, text="Number :", font=("montserrat", 20, "bold"), bg_color='transparent', text_color="white")
num = CTkEntry(master=frame, placeholder_text="Number", height=35, font=("montserrat", 15))
start_btn = CTkButton(master=frame, text="START", font=("montserrat", 15, "bold"), width=130, height=33, command=spam)
setting_btn= CTkButton(master=frame, text="SETTING", font=("montserrat", 15, "bold"), width=130, height=33, command=setting)
# last btn
share = CTkButton(master=frame, text="",font=("montserrat", 15, "bold"), width=20, height=20, image=photo1, bg_color="#2b2b2b", fg_color="#2b2b2b", hover_color="#3f4444",
                  command=sharep)
donate = CTkButton(master=frame, text="", font=("montserrat", 15, "bold"), width=20, height=20, image=photo2, bg_color="#2b2b2b", fg_color="#2b2b2b", hover_color="#3f4444", command=donate)
rate = CTkButton(master=frame, text="", font=("montserrat", 15, "bold"), width=20, height=20, image=photo3, bg_color="#2b2b2b", fg_color="#2b2b2b", hover_color="#3f4444", command=lambda: open(linktop))
source = CTkButton(master=frame, text="", font=("montserrat", 15, "bold"), width=20, height=20, image=photo4, bg_color="#2b2b2b", fg_color="#2b2b2b", hover_color="#3f4444", command=lambda: open(linktop))
diving_line = CTkLabel(frame, text="____________________________________________________", font=("montserrat", 10, "bold"), bg_color='transparent', text_color="white")


spam_lbl.place(x=85, y=15)
num_lbl.place(x=25, y=160)
num.place(x=150, y=160)
txt_lbl.place(x=25, y=110)
text.place(x=150, y=110)
start_btn.place(x=92, y=230)
setting_btn.place(x=92, y=270)

diving_line.place(x=29, y=325)
share.place(x=42, y=357)
donate.place(x=102, y=357)
rate.place(x=162, y=357)
source.place(x=222, y=357)

root.mainloop()




# def how_to_work():
#     messagebox.showerror("error", "Access Denied")
    # root = Tk()
    # root.geometry("500x200")
    # root.resizable(0,0)


    # gj = Message(root,text="1)open the chat page app Telegram, Whatsapp, Instagram and ...")
    # gj.grid(row=0,column=0)

    # nn = Message(root,text="2)run 'the spammer bot', Enter the text and number")
    # nn.grid(row=0,column=1)

    # ll = Message(root,text="3)you have 5 seconds to click on your chat bar and start spamming the text")
    # ll.grid(row=0,column=2)




    # root.mainloop()





#________________GUI________________

# app = Tk()
# app.geometry("305x300")
# app.title("Spammer Bot")
# app.resizable(0,0)


# title_text = Label(app, text="Spam The Text",fg="red",font=16,padx=85)
# title_text.grid(row=0,column=0,pady=(5,0))

# get_text = Label(app, text="Enter the Text")
# get_text.grid(row=1,column=0,pady=(10,0))

# getting_text = Entry(app, width=30)
# getting_text.grid(row=2,column=0)

# get_num_text = Label(app, text="How Many?")
# get_num_text.grid(row=3,column=0)

# get_num_entry = Entry(app, width=30)
# get_num_entry.grid(row=4,column=0)

# but = Button(app, text="Start", command=spam,width=11)
# but.grid(row=5,column=0,pady=(10,0))

# htw = Button(app, text="How to work",command=how_to_work,width=11)
# htw.grid(row=6,column=0,pady=(5,0))

# cre = Label(app, text="Created By Abolfazl Rashidian")
# cre.grid(row=7,column=0,pady=(48,0))


# app.mainloop()




 
