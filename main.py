import webview
from tkinter import Tk

root = Tk()

sx= root.winfo_screenwidth()
sy = root.winfo_screenheight()


# percent = lambda x, p: (p*x)/100 

webview.create_window(
    "nakala",
    "dist/index.html",
    background_color="#4f384a",
    width=300,
    height=500,
    on_top=True,
    x=sx-310,
    y=sy-550
)
webview.start()