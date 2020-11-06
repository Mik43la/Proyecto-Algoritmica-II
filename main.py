from tkinter.ttk import Combobox

import Dijkstra
import Edmonds_Karp
import Kruskal

from tkinter import *

from PIL import Image, ImageTk

global picture, boton_kruskal, boton_edmonds, boton_dijkstra, boton_atras, e, window


class Example(Frame):
    global picture

    def __init__(self, master, *pargs):
        global picture

        Frame.__init__(self, master, *pargs)

        self.image = Image.open(picture)
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self, event):
        global picture
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


def borrar_botones():
    global picture, boton_kruskal, boton_edmonds, boton_dijkstra, boton_atras, e, window

    boton_edmonds.place_forget()
    boton_kruskal.place_forget()
    boton_dijkstra.place_forget()


def poner_botones():
    global picture, boton_kruskal, boton_edmonds, boton_dijkstra, boton_atras, e, window

    boton_kruskal = Button(window, text="kruskal", command=kruskal, bg="black", fg="white")
    boton_kruskal.place(x=580, y=100, width=200, height=40)
    boton_edmonds = Button(window, text="edmonds", command=edmonds, bg="black", fg="white")
    boton_edmonds.place(x=580, y=40, width=200, height=40)
    boton_dijkstra = Button(window, text="dijkstra", command=dijkstra, bg="black", fg="white")
    boton_dijkstra.place(x=580, y=150, width=200, height=40)


def kruskal():
    global picture, boton_kruskal, boton_edmonds, boton_dijkstra, boton_atras, e, window

    Kruskal.main()
    e.destroy()
    borrar_botones()
    e.pack_forget
    picture = 'path_Kruskal.png'
    e = Example(window)
    e.pack(fill=BOTH, expand=YES)
    boton_atras = Button(window, text="atras", command=menu, bg="black", fg="white")
    boton_atras.place(x=0, y=0, width=100, height=30)


def edmonds():
    global picture, boton_kruskal, boton_edmonds, boton_dijkstra, boton_atras, e, window

    Edmonds_Karp.main()

    e.destroy()
    borrar_botones()
    picture = 'path_Edmonds.png'
    e = Example(window)
    e.pack(fill=BOTH, expand=YES)
    boton_atras = Button(window, text="atras", command=menu, bg="black", fg="white")
    boton_atras.place(x=0, y=0, width=100, height=30)


def dijkstra():
    global picture, boton_kruskal, boton_edmonds, boton_dijkstra, boton_atras, e, window

    Dijkstra.main()
    e.destroy()
    borrar_botones()
    picture = 'path_Dijkstra.png'
    e = Example(window)
    e.pack(fill=BOTH, expand=YES)
    boton_atras = Button(window, text="atras", command=menu, bg="black", fg="white")
    boton_atras.place(x=0, y=0, width=100, height=30)


def menu():
    global picture, boton_kruskal, boton_edmonds, boton_dijkstra, boton_atras, e, window

    e.destroy()
    picture = 'fondo_caminos.jpg'
    e = Example(window)
    e.pack(fill=BOTH, expand=YES)

    # botones
    poner_botones()


def main():
    global picture, boton_kruskal, boton_edmonds, boton_dijkstra, boton_atras, e, window, value_window, combo
    valueWindow()
    print((value_window))

    aplicacion(value_window)


def aplicacion(value_window):
    global picture, boton_kruskal, boton_edmonds, boton_dijkstra, boton_atras, e, window, combo
    window = Tk()
    window.title("Caminos Bolivia")
    window.geometry(value_window)  # tamaño de la pantalla
    window.configure(background="black")

    picture = 'fondo_caminos.jpg'
    e = Example(window)
    e.pack(fill=BOTH, expand=YES)

    # botones
    poner_botones()

    window.mainloop()


def valueWindow():
    global value_window, combo

    def borrarVentana():
        global value_window, combo
        value_window = combo.get()
        root.destroy()

    root = Tk()

    root.title("")

    root.geometry('350x200')

    lbl = Label(root, text="Tamaño de la pantalla:")
    lbl.place(x=80, y=2, width=200, height=40)

    combo = Combobox(root)
    combo['values'] = ('1280x720', '1366x768', '1440x900', '1680x1050', '1920x1200', '256x1440', '2560x1600')
    combo.current(1)  # set the selected item
    combo.place(x=80, y=40, width=200, height=40)

    boton_tamaño = Button(root, text="aceptar", command=borrarVentana)
    boton_tamaño.place(x=80, y=100, width=200, height=40)

    root.mainloop()


main()

