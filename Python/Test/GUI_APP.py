import tkinter as tk
from tkinter import filedialog, Text
import os
root1=tk.Tk()
apps=[]
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps=f.read()
        tempApps=tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
def addApp():
    filename=filedialog.askopenfilename(initialdir="/",title="Select File",
                                        filetypes=(("executables","*.exe"),("all files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label=tk.Label(frame,text=app,bg="gray")
        label.pack()
def runApps():
    for app in apps:
        os.startfile(app)
canvas=tk.Canvas(root1,height=300,width=700,bg="#263D42")
canvas.pack()
frame=tk.Frame(root1,bg="white")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
openFile=tk.Button(root1,text="Open File",padx=10,pady=5,fg="white",bg="blue",command=addApp)
openFile.pack()
runApps=tk.Button(root1,text="Run Apps",padx=10,pady=5,fg="white",bg="blue",command=runApps)
runApps.pack()
for app in apps:
    label=tk.Label(frame,text=app)
    label.pack()
root1.mainloop()
with open('save.txt','w') as f:
    for app in apps:
        f.write(app +',')