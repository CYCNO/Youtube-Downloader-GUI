from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from pytube import *

root = Tk()

root.title('YT Downloader')
root.iconbitmap('download-from-cloud.ico')
root.minsize(width=640, height=250)
root.maxsize(width=640, height=250)

#functions
def Download():
    if var.get() == '':
        messagebox.showerror("An Error Occured", "Please Enter The Link")
    else:
        global folder_path
        filename = filedialog.askdirectory()
        folder_path.set(filename)    
        video = YouTube(var.get())
        if var2.get() == 0:
            vid2 = video.streams.get_by_resolution('360p')
            vid2.download(filename)
            messagebox.showinfo("Download Successfully", "Your Video Is Downloaded Successfully")
        elif var2.get() == 1:
            vid = video.streams.get_by_resolution('240p')
            vid.download(filename)
            messagebox.showinfo("Download Successfully", "Your Video Is Downloaded Successfully")
        elif var2.get() == 2:
            vid3 = video.streams.get_by_resolution('720p')
            vid3.download(filename)
            messagebox.showinfo("Download Successfully", "Your Video Is Downloaded Successfully")
        elif var2.get() == 3:
            vid4 = video.streams.get_by_resolution('1080p')
            vid4.download(filename)
            messagebox.showinfo("Download Successfully", "Your Video Is Downloaded Successfully")
        else:
            messagebox.showerror('An Error Occured', 'Something Went Wrong')         
    


#label
lbl = Label(root, text='YouTube Downloader', fg='black', font='Helvetica 18 bold')
lbl.place(x=200,y=30)

#link label
link = Label(root, text='Link ',font='Helvetica 11 bold',fg='black')
link.place(x=155, y=77)

#entry box
var = StringVar()
ent = Entry(root, textvariable=var,width=47)
ent.place(x=200, y=80)

#quality label
quality = Label(root, text='Quality',font='Helvetica 10 bold')
quality.place(x=140, y=110)

#quality
var2 = IntVar()
qlt = Radiobutton(root, text='Low', value=1, variable=var2).place(x=200, y=110)
qlt1 = Radiobutton(root, text='Medium', value=0, variable=var2).place(x=260, y=110)
qlt2 = Radiobutton(root, text='High', value=2, variable=var2).place(x=340, y=110)
qlt3 = Radiobutton(root, text='Very High', value=3, variable=var2).place(x=400, y=110)

#button browse
folder_path = StringVar()
btn2 = Button(root, text='Download', command=Download, width=17)
btn2.place(x=250,y=150)

root.mainloop()
