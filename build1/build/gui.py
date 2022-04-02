
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1191x692")
window.configure(bg = "#E4E4EE")


canvas = Canvas(
    window,
    bg = "#E4E4EE",
    height = 692,
    width = 1191,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    630.0,
    0.0,
    1442.0,
    1024.0,
    fill="#164FD5",
    outline="")

canvas.create_text(
    42.0,
    24.0,
    anchor="nw",
    text="Rabin",
    fill="#000000",
    font=("Inter", 64 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=751.0,
    y=285.0,
    width=277.0,
    height=65.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="groove"
)
button_2.place(
    x=169.0,
    y=620.0,
    width=260.0,
    height=42.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    299.5,
    176.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_1.place(
    x=55.0,
    y=147.0,
    width=489.0,
    height=30.0
)

canvas.create_text(
    56.0,
    147.0,
    anchor="nw",
    text="Primo p",
    fill="#164FD5",
    font=("Inter", 24 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    299.5,
    274.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_2.place(
    x=55.0,
    y=245.0,
    width=489.0,
    height=30.0
)

canvas.create_text(
    57.0,
    245.0,
    anchor="nw",
    text="Primo q",
    fill="#164FD5",
    font=("Inter", 24 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    299.5,
    374.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_3.place(
    x=55.0,
    y=345.0,
    width=489.0,
    height=30.0
)

canvas.create_text(
    56.0,
    345.0,
    anchor="nw",
    text="Número n",
    fill="#164FD5",
    font=("Inter", 24 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    299.5,
    512.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_4.place(
    x=55.0,
    y=451.0,
    width=489.0,
    height=30.0
)

canvas.create_text(
    56.0,
    459.0,
    anchor="nw",
    text="Texto claro",
    fill="#164FD5",
    font=("Inter", 24 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    917.5,
    512.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
entry_5.place(
    x=736.0,
    y=451.0,
    width=363.0,
    height=30.0
)

canvas.create_text(
    740.0,
    459.0,
    anchor="nw",
    text="Texto cifrado",
    fill="#164FD5",
    font=("Inter", 24 * -1)
)
window.resizable(False, False)
window.mainloop()
