import webview
from tkinter import Tk
from data.db import API

root = Tk()

sx = root.winfo_screenwidth()
sy = root.winfo_screenheight()


# percent = lambda x, p: (p*x)/100
dev_url = "http://localhost:5173/"
production_url = "dist/index.html"
api = API()
webview.create_window(
    "nakala",
    production_url,
    background_color="#4f384a",
    width=325,
    height=510,
    on_top=True,
    x=sx - 310,
    y=sy - 550,
    js_api=api,
)
webview.start(debug=False, gui="qt")
