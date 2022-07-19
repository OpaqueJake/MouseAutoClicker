#Autoclicker

import time, pyautogui, keyboard, threading
from tkinter import *

window = Tk()

#Functions
def clickedStart():
    time.sleep(3)
    run = True

    intervalInt = None

    try:
        intervalInt = int(txt.get())
    except:
        pass

    start = time.time()

    while run == True:

        if keyboard.is_pressed('0'):
            run = False
            break

        if intervalInt != None:
            print((time.time() + intervalInt))
            print(start)
            if time.time() >= (start + intervalInt):
                pyautogui.click()
                start = time.time()
        else:
            pyautogui.click()

# Title
window.title("AutoClicker")

# Label
lbl = Label(window, text = "Delay in Seconds", font=("Arial", 18), bd=2,relief="flat")
lbl.pack(pady=20)
lbl.grid(column=1, row=0, padx=(75, 20))

# Text
txt = Entry(window,width=15)
txt.grid(column=1, row=1, padx=(75, 10))

# Buttons
btn = Button(window, text= "Start Box", command=clickedStart, bg="blue", fg="lightblue", font=("Helvetica", 12))
btn.grid(column=1, row=2, padx=(75,10), pady=(15, 10))

# Window Size
window.geometry("430x160")

# To change the icon
icon = PhotoImage(file = "autoclickericon.png")
window.iconphoto(False, icon)

# Run the app
txt.focus()
window.mainloop()