from tkinter import *
import hashlib
import sys

file_name = sys.argv[1]

hash_md5 = hashlib.md5()
with open(file_name, "rb") as f:
    for buf in iter(lambda: f.read(4096), b""):
        hash_md5.update(buf)

md5hash = hash_md5.hexdigest()

root = Tk()
root.title("WinCork")
root.config(height=100, width=500)

text = Label(root, text=md5hash)
text.place(relx=0.5, rely=.25, anchor=CENTER)

okButton = Button(text="OK", command=quit)
okButton.place(relx=0.5, rely=0.75, anchor=CENTER)

mainloop()