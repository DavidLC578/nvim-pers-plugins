import tkinter as tk
import random



app = tk.Tk()
app.geometry('700x700')

ResultadoLabel = tk.Label(app)

def adivinarNumero():
    #rand = random.randint(0,4)
    rand= 1
    numero = entryNumero.get()
    if int(numero) == int(rand):
       ResultadoLabel.config(text="Adivinaste")
    else:
       ResultadoLabel.config(text="Perdiste")
       

entryNumero = tk.Entry(app)
entryNumero.pack()

btnAdivinar = tk.Button(app, text="Adivinar", command=adivinarNumero)
btnAdivinar.pack()

ResultadoLabel.pack()

app.mainloop()

