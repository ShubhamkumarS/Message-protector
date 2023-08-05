__author__ = "Shubham Kumar"
import os
from tkinter import *
from tkinter import messagebox


main = Tk()
main.geometry("1366x768")
main.title("Steganography & Cryptography")
main.resizable(0, 0)
def Exit():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=main)
    if sure == True:
        main.destroy()
        
main.protocol("WM_DELETE_WINDOW", Exit)

def IMG():
    main.withdraw()
    os.system("python Hide_Secret_Text_Message.py")
    main.deiconify()


def PDF():
    main.withdraw()
    os.system("python PDF_Protector.py")
    main.deiconify()

def TEXT():
    main.withdraw()
    os.system("python Message_Encryption_and_Decryption.py")
    main.deiconify()

label1 = Label(main)
label1.place(relx=0, rely=0, width=1366, height=768)
img =PhotoImage(file="./Image/admin.png")
label1.configure(image=img)

button1 = Button(main)
button1.place(relx=0.268, rely=0.415, width=150, height=130)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#ffffff")
button1.configure(cursor="hand2")
button1.configure(foreground="#ffffff")
button1.configure(background="#ffffff")
button1.configure(borderwidth="0")
img1 = PhotoImage(file="./Image/1.png")
button1.configure(image=img1)
button1.configure(command=IMG)

button2 = Button(main)
button2.place(relx=0.455, rely=0.415, width=150, height=130)
button2.configure(relief="flat")
button2.configure(overrelief="flat")
button2.configure(activebackground="#ffffff")
button2.configure(cursor="hand2")
button2.configure(foreground="#ffffff")
button2.configure(background="#ffffff")
button2.configure(borderwidth="0")
img2 = PhotoImage(file="./Image/2.png")
button2.configure(image=img2)
button2.configure(command=PDF)


button3 = Button(main)
button3.place(relx=0.640, rely=0.415, width=150, height=130)
button3.configure(relief="flat")
button3.configure(overrelief="flat")
button3.configure(activebackground="#ffffff")
button3.configure(cursor="hand2")
button3.configure(foreground="#ffffff")
button3.configure(background="#ffffff")
button3.configure(borderwidth="0")
img3 = PhotoImage(file="./Image/3.png")
button3.configure(image=img3)
button3.configure(command=TEXT)

main.mainloop()
