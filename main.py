import ast
from tkinter.ttk import Combobox

import Dijkstra
import Edmonds_Karp
import Kruskal

from tkinter import *

from PIL import Image, ImageTk

global picture, boton_kruskal, boton_edmonds, boton_dijkstra, boton_atras, e, window, lugar_y_texto_nodos
lugar_y_texto_nodos = 110
lugar_y_texto_aristas = 380

global conexiones_eliminadas
conexiones_eliminadas = 0

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


def deleteRute(nodeO, nodeD):
    global conexiones_eliminadas
    rf = open("copyLugares.txt", "r")
    cities = ast.literal_eval(rf.read())
    rf.close()

    indexO = list(cities.keys())[list(cities.values()).index(nodeO)]
    indexD = list(cities.keys())[list(cities.values()).index(nodeD)]

    with open('connections.txt') as openfileobject:
        flag = 0
        copyStringConnect = []
        for line in openfileobject:

            if flag != 1:
                string_line = line.rstrip("\n")

                number_of_nodes_reserve, number_of_edges = map(int, string_line.split())
                copyStringConnect.append(line)
                flag = 1
                continue

            nodeA, nodeB, weight = map(float, line.split())
            nodeA = int(nodeA)
            nodeB = int(nodeB)
            if int(nodeA) is not indexO or int(nodeB) is not indexD and \
                    (int(nodeA) is not indexD or int(nodeB) is not indexO):
                copyStringConnect.append(line)
            else:
                string_line = copyStringConnect[0].rstrip("\n")

                number_of_nodes, number_of_edges = map(int, string_line.split())
                number_of_edges -= 1
                conexiones_eliminadas += 1
                if number_of_edges + conexiones_eliminadas is not number_of_nodes_reserve:
                    number_of_edges = number_of_nodes_reserve - conexiones_eliminadas
                copyStringConnect[0] = str(number_of_nodes) + " " + str(number_of_edges) + "\n"

    openfileobject.close()
    openfile = open("copyconnect.txt", "w")
    for line in range(len(copyStringConnect)):
        openfile.write(copyStringConnect[line])

    openfile.close()


def deleteNode(nombres_ciudades):
    global conexiones_eliminadas
    rf = open("copyLugares.txt", "r")
    cities = ast.literal_eval(rf.read())
    rf.close()
    rf = open("copyCoords.txt", "r")
    coords = ast.literal_eval(rf.read())
    rf.close()

    nodos_eliminados = len(nombres_ciudades)
    for i in range(len(nombres_ciudades)):

        index = list(cities.keys())[list(cities.values()).index(nombres_ciudades[i])]

        with open('connections.txt') as openfileobject:
            flag = 0
            copyStringConnect = []

            for line in openfileobject:

                if flag is not 1:
                    string_line = line.rstrip("\n")

                    number_of_nodes_reserve, number_of_edges = map(int, string_line.split())
                    copyStringConnect.append(line)
                    flag = 1

                    continue

                nodeA, nodeB, weight = map(float, line.split())
                nodeA = int(nodeA)
                nodeB = int(nodeB)
                if nodeA is not index and nodeB is not index:
                    copyStringConnect.append(line)
                else:
                    string_line = copyStringConnect[0].rstrip("\n")
                    number_of_nodes, number_of_edges = map(int, string_line.split())
                    number_of_edges -= 1
                    conexiones_eliminadas += 1
                    if number_of_edges + conexiones_eliminadas is not number_of_nodes_reserve:
                        number_of_edges = number_of_nodes_reserve - conexiones_eliminadas
                    copyStringConnect[0] = str(number_of_nodes) + " " + str(number_of_edges) + "\n"

        openfileobject.close()

        cities.__delitem__(index)

        coords.__delitem__(nombres_ciudades[i])

    openfile = open("copyconnect.txt", "w")
    for line in range(len(copyStringConnect)):
        openfile.write(copyStringConnect[line])

    openfile.close()
    #
    rf = open("copyLugares.txt", "w")
    st_cities = str(cities)
    rf.write(st_cities)
    rf = open("copyCoords.txt", "w")
    st_coords = str(coords)
    rf.write(st_coords)

    rf.close()

    # print(conexiones_eliminadas)


def init_Texts():

    rf = open("lugares.txt", "r")
    lugares = rf.read()
    rf = open("copyLugares.txt", "w")
    rf.write(lugares)

    rf = open("coordenadas.txt", "r")
    coordenadas = rf.read()
    rf = open("copyCoords.txt", "w")
    rf.write(coordenadas)

    rf = open("connections.txt", "r")
    conexiones = rf.read()
    rf = open("copyconnect.txt", "w")
    rf.write(conexiones)

    rf.close()


def actualS():
    global lugares, combo_nodo_inicio, s

    with open('lugares.txt', 'r') as dict_file:
        dict_text = dict_file.read()
        diccionario = eval(dict_text)

    for key in diccionario:  # binary search
        if combo_nodo_inicio.get() == diccionario[key]:
            s = key


def actualT():
    global lugares, combo_nodo_destino,t

    with open('lugares.txt', 'r') as dict_file:
        dict_text = dict_file.read()
        diccionario = eval(dict_text)

    for key in diccionario:  # binary search
        if combo_nodo_destino.get() == diccionario[key]:
            t = key


def borrar_botones():
    global picture, boton_kruskal, boton_edmonds, boton_dijkstra, boton_atras, \
        boton_eliminar_arista, boton_eliminar_nodo, e, window

    boton_edmonds.place_forget()
    boton_kruskal.place_forget()
    boton_dijkstra.place_forget()
    boton_eliminar_nodo.place_forget()
    boton_eliminar_arista.place_forget()


def poner_botones():
    global picture, boton_kruskal, boton_edmonds, boton_dijkstra, boton_atras, \
        boton_eliminar_arista, boton_eliminar_nodo, e, window, lugar_y_texto_nodos

    boton_kruskal = Button(window, text="Caminos mas usasdos de Bolivia", command=kruskal, bg="black", fg="white")
    boton_kruskal.place(x=180, y=100, width=200, height=40)
    boton_edmonds = Button(window, text="poblaciones a evitar", command=edmonds, bg="black", fg="white")
    boton_edmonds.place(x=180, y=200, width=200, height=40)
    boton_dijkstra = Button(window, text="Camino mas corto", command=dijkstra, bg="black", fg="white")
    boton_dijkstra.place(x=180, y=300, width=200, height=40)
    # botones de eliminar
    boton_eliminar_nodo = Button(window, text="Eliminar lugar", command=eliminarNodo, bg="grey", fg="white")
    boton_eliminar_nodo.place(x=800, y=130, width=150, height=40)
    boton_eliminar_arista = Button(window, text="Eliminar Carretera", command=eliminarArista, bg="grey", fg="white")
    boton_eliminar_arista.place(x=800, y=500, width=150, height=40)


def eliminarNodo():
    global window, combo_nodos, combo_caminoA, combo_caminoB, lugar_y_texto_nodos, combo_nodo_destino, combo_nodo_inicio

    lista_nodos = []
    lista_nodos.append(combo_nodos.get())
    deleteNode(lista_nodos)
    lblnodo = Label(window, text=combo_nodos.get())
    lblnodo.place(x=1000, y=lugar_y_texto_nodos, width=200, height=40)
    lugar_y_texto_nodos += 30


def eliminarArista():
    global window, combo_nodos, combo_caminoA, combo_caminoB, lugar_y_texto_aristas, combo_nodo_destino, combo_nodo_inicio

    deleteRute(combo_caminoA.get(), combo_caminoB.get())
    texto = combo_caminoA.get() + "-" + combo_caminoB.get()
    lblaArista = Label(window, text=texto)
    lblaArista.place(x=1000, y=lugar_y_texto_aristas, width=200, height=40)
    lugar_y_texto_aristas += 30


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
    global picture, boton_kruskal, boton_edmonds, boton_dijkstra, boton_atras, e, window,  s, t

    actualS()
    actualT()
    Edmonds_Karp.main(s, t)

    e.destroy()
    borrar_botones()
    picture = 'path_Edmonds.png'
    e = Example(window)
    e.pack(fill=BOTH, expand=YES)
    boton_atras = Button(window, text="atras", command=menu, bg="black", fg="white")
    boton_atras.place(x=0, y=0, width=100, height=30)


def dijkstra():
    global picture, boton_kruskal, boton_edmonds, boton_dijkstra, boton_atras, e, window, s, t

    actualS()
    actualT()
    Dijkstra.main(s, t)
    e.destroy()
    borrar_botones()
    picture = 'path_Dijkstra.png'
    e = Example(window)
    e.pack(fill=BOTH, expand=YES)
    boton_atras = Button(window, text="atras", command=menu, bg="black", fg="white")
    boton_atras.place(x=0, y=0, width=100, height=30)


def menu():
    global picture, boton_kruskal, boton_edmonds, boton_dijkstra, boton_atras, e, window,lugar_y_texto_nodos,lugar_y_texto_aristas

    e.destroy()
    picture = 'fondo_caminos.jpg'
    e = Example(window)
    e.pack(fill=BOTH, expand=YES)

    lugar_y_texto_nodos = 110
    lugar_y_texto_aristas = 380
    init_Texts()
    # botones
    poner_botones()
    listaLugares()

    # Letras
    lbl = Label(window, text="Lugares a eliminar")
    lbl.place(x=1000, y=80, width=200, height=40)

    lbl = Label(window, text="carreteras a eliminar")
    lbl.place(x=1000, y=350, width=200, height=40)


def main():
    global picture, boton_kruskal, boton_edmonds, boton_dijkstra, boton_atras, e, window, value_window, combo
    valueWindow()
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
    listaLugares()

    # Letras
    lbl = Label(window, text="Lugares a eliminar")
    lbl.place(x=1000, y=80, width=200, height=40)

    lbl = Label(window, text="carreteras a eliminar")
    lbl.place(x=1000, y=350, width=200, height=40)

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


def listaLugares():
    global window, combo_nodos, combo_caminoA, combo_caminoB, combo_nodo_destino, combo_nodo_inicio, lugares
    f = open('listaLugares.txt', 'r')
    lugares = []

    for line in f:
        lugares.append(line.strip())

    f.close()

    combo_nodos = Combobox(window)
    combo_nodos.place(x=800, y=80, width=150, height=30)
    combo_nodos['values'] = lugares
    combo_nodos.current(0)  # set the selected item

    combo_caminoA = Combobox(window)
    combo_caminoA.place(x=800, y=400, width=150, height=30)
    combo_caminoA['values'] = lugares
    combo_caminoA.current(0)  # set the selected item

    combo_caminoB = Combobox(window)
    combo_caminoB.place(x=800, y=450, width=150, height=30)
    combo_caminoB['values'] = lugares
    combo_caminoB.current(26)  # set the selected item

    # nodo destino y nodo inicio
    combo_nodo_inicio = Combobox(window)
    combo_nodo_inicio.place(x=180, y=450, width=150, height=30)
    combo_nodo_inicio['values'] = lugares
    combo_nodo_inicio.current(0)  # set the selected item

    combo_nodo_destino = Combobox(window)
    combo_nodo_destino.place(x=180, y=550, width=150, height=30)
    combo_nodo_destino['values'] = lugares
    combo_nodo_destino.current(1)  # set the selected item
    #LAbels nodos s y t
    lblnodo = Label(window, text="lugar de partida")
    lblnodo.place(x=330, y=450, width=150, height=30)

    lblnodo = Label(window, text="lugar de destino")
    lblnodo.place(x=330, y=550, width=150, height=30)


init_Texts()
main()
