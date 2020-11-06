import Dijkstra
import Edmonds_Karp
import Kruskal

from tkinter import *

from PIL import Image, ImageTk

global picture, boton_kruskal, boton_edmonds, boton_dijkstra, boton_atras, e

root = Tk()
root.title("Caminos Bolivia")
root.geometry('1366x768')  # tamaño de la pantalla
root.configure(background="black")


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
    global picture, boton_kruskal, boton_edmonds, boton_dijkstra, boton_atras, e

    boton_edmonds.place_forget()
    boton_kruskal.place_forget()
    boton_dijkstra.place_forget()


def poner_botones():
    global picture, boton_kruskal, boton_edmonds, boton_dijkstra, boton_atras, e

    boton_kruskal = Button(root, text="kruskal", command=kruskal, bg="black", fg="white")
    boton_kruskal.place(x=580, y=100, width=200, height=40)
    boton_edmonds = Button(root, text="edmonds", command=edmonds, bg="black", fg="white")
    boton_edmonds.place(x=580, y=40, width=200, height=40)
    boton_dijkstra = Button(root, text="dijkstra", command=dijkstra, bg="black", fg="white")
    boton_dijkstra.place(x=580, y=150, width=200, height=40)


def kruskal():
    global picture, boton_kruskal, boton_edmonds, boton_dijkstra, boton_atras, e


    Kruskal.main()
    e.destroy()
    borrar_botones()
    e.pack_forget
    picture = 'path_Kruskal.png'
    e = Example(root)
    e.pack(fill=BOTH, expand=YES)
    boton_atras = Button(root, text="atras", command=menu, bg="black", fg="white")
    boton_atras.place(x=0, y=0, width=100, height=30)


def edmonds():
    global picture, boton_kruskal, boton_edmonds, boton_dijkstra, boton_atras, e


    Edmonds_Karp.main()

    e.destroy()
    borrar_botones()
    picture = 'path_Edmonds.png'
    e = Example(root)
    e.pack(fill=BOTH, expand=YES)
    boton_atras = Button(root, text="atras", command=menu, bg="black", fg="white")
    boton_atras.place(x=0, y=0, width=100, height=30)


def dijkstra():
    global picture, boton_kruskal, boton_edmonds, boton_dijkstra, boton_atras, e

    Dijkstra.main()
    e.destroy()
    borrar_botones()
    picture = 'path_Dijkstra.png'
    e = Example(root)
    e.pack(fill=BOTH, expand=YES)
    boton_atras = Button(root, text="atras", command=menu, bg="black", fg="white")
    boton_atras.place(x=0, y=0, width=100, height=30)


def menu():
    global picture, boton_kruskal, boton_edmonds, boton_dijkstra, boton_atras, e

    e.destroy()
    picture = 'fondo_caminos.jpg'
    e = Example(root)
    e.pack(fill=BOTH, expand=YES)

    # botones
    poner_botones()


def main():
    global picture, boton_kruskal, boton_edmonds, boton_dijkstra, boton_atras, e

    picture = 'fondo_caminos.jpg'
    e = Example(root)
    e.pack(fill=BOTH, expand=YES)

    # botones
    poner_botones()


main()
root.mainloop()
