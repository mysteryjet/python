from tkinter import font
import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO

window = tk.Tk()
window.geometry("600x500")
window.title("Pokedex Sample")
window.config(padx= 10, pady=10)

title_label = tk.Label(window, text="Manuel Pokedex")
title_label.config(font = ("Ubuntu", 32))
title_label.pack(padx=10, pady=10)

# Se agregará los datos y la imagen del pokemon
pokemon_image = tk.Label(window)
pokemon_image.pack(padx=10, pady=10)

pokemon_informacion = tk.Label(window)
pokemon_informacion.config(font=("Ubuntu", 20))
pokemon_informacion.pack(padx=10, pady=10)

pokemon_tipos = tk.Label(window)
pokemon_tipos.config(font=("Ubuntu", 20))
pokemon_tipos.pack(padx=10, pady=10)

# Funcion
def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))
    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))
    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_informacion.config(text=f"{pokemon.dex} - {pokemon.name}".title())
    pokemon_tipos.config(text=" - ".join([t for t in pokemon.types]).title())

label_id_name = tk.Label(window, text="Ingresa el ID o Nombre del Pokemon")
label_id_name.config(font=("Ubuntu", 20))
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(window, height=1,)
text_id_name.config(font=("Ubuntu", 20))
text_id_name.pack(padx=10, pady=10)
boton_load = tk.Button(window, text="Cargar Pokemon", command=load_pokemon)
boton_load.config(font= ("Ubuntu", 20))
boton_load.pack(padx=10, pady=10)

window.mainloop()