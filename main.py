import tkinter as tk
import pyautogui
from PIL import Image, ImageTk
import time
from tkinter import messagebox

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb   

root = tk.Tk()
root.geometry('600x600')
root.title('Autotyper')
root.maxsize(600,600)
root.minsize(600,600)
root.configure(bg=_from_rgb((26, 38, 49)))

icon = Image.open("images/typing.png")
icon=icon.resize((128,128))
render = ImageTk.PhotoImage(icon)
img = tk.Label(root, image=render, bg=_from_rgb((26, 38, 49)))
img.place(x=245,y=25)

what_to_type=tk.Entry(root, fg=_from_rgb((0, 0, 0)))
what_to_type.place(x=230,y=200)

text = tk.Label(root, text="Enter the text here", fg="white", bg=_from_rgb((26, 38, 49)))
text.place(x=90,y=202)

how_many_times=tk.Entry(root, fg='black')
how_many_times.place(x=230,y=240)

text2 = tk.Label(root, text="How many times", fg='white', bg=_from_rgb((26, 38, 49)))
text2.place(x=90,y=242)

def submit():
	time.sleep(5)
	global what_to_type, how_many_times
	try:
		for i in range(int(how_many_times.get())):
			pyautogui.write(what_to_type.get())
			pyautogui.press('enter')

	except:
		messagebox.showinfo("Error", "How many times should be a number")

submit_btn = tk.Button(root, text="Type Now", command=submit)
submit_btn.place(x=260, y=280)

root.mainloop()