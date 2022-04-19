
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

def guiMain (windows):

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    global image_image_1

    canvas = Canvas(
        windows,
        bg="#E4E4EE",
        height=692 - 28,
        width=1191,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=28)
    canvas.create_rectangle(
        619.0,
        9.0,
        1191.0,
        692.0,
        fill="#164FD5",
        outline="")

    canvas.create_text(
        47.0,
        47.0,
        anchor="nw",
        text="CriptoCodificadorInador",
        fill="#000000",
        font=("Inter", 48 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))

    image_1 = canvas.create_image(
        306.0,
        358.0,
        image=image_image_1
    )

