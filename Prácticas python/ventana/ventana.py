import tkinter as tk
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
hostip = (s.getsockname()[0])
s.close()

ventana=tk.Tk()
ventana.title("¿Cual es mi IP?")
ventana.geometry("250x50")
ventana.configure(background="dim gray")

etiqueta1=tk.Label(ventana, text= "¿Cual es mi IP?", bg="dim gray", fg="white")
etiqueta1.pack()

etiquetaip=tk.Label(ventana, text= "Tu IP es " + hostip, bg="dim gray", fg="firebrick")
etiquetaip.pack()



ventana.mainloop()
