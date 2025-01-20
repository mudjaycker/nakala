import webview
from tkinter import Tk
from data.db import API

root = Tk()

sx = root.winfo_screenwidth()
sy = root.winfo_screenheight()


# url = "http://localhost:5173/"
url = "dist/index.html"
api = API()
webview.create_window(
    "nakala",
    url,
    background_color="#4f384a",
    width=sx // 6,
    height=sy // 2,
    on_top=True,
    x=sx,
    y=sy,
    js_api=api,
)
webview.start(gui="qt", debug=True)
