import tkinter as tk
from tkinter import *
from tkinter import messagebox

from flask import redirect


# Crear la ventana principal
def formulario():
    global nombre_texto, nit_texto, correo_texto
    ventana = Tk()
    ventana.title("Practica 2")
    ventana.geometry("%dx%d+%d+%d" % (600,450,450,150))
    ventana.resizable(0,0)


    panel_Frame = Frame(ventana)
    panel_Frame.pack(side = "top")
    panel_Frame.place(width = "600", height = "450")
    panel_Frame.config(background = "Black")

    label = Label(text = "REGISTRO DE CLIENTES" , foreground = "White", bg = "black", font = ("Modern", 36) )
    label.pack()
    label.place(x = 45, y = 50, width = 450, height= 40)

    nombre_texto = Text(foreground = "White", bg = "black", font = "Modern", highlightbackground="white",highlightthickness=1)
    nombre_texto.pack()
    nombre_texto.place(x = 285, y = 150, width = 150, height= 25)

    nit_texto = Text(foreground = "White", bg = "black", font = "Modern", highlightbackground="white",highlightthickness=1)
    nit_texto.pack()
    nit_texto.place(x = 285, y = 200, width = 150, height= 25)

    correo_texto = Text(foreground = "White", bg = "black", font = "Modern", highlightbackground="white",highlightthickness=1)
    correo_texto.pack()
    correo_texto.place(x = 285, y = 250, width = 150, height= 25)

    label2 = Label(text = "Nombre:", foreground = "White", bg = "black", font = "Modern", highlightbackground="white")
    label2.pack()
    label2.place(x = 145, y = 150,width = 120, height= 25)

    label4 = Label(text = "Correo Electrónico:", foreground = "White", bg = "black", font = "Modern", highlightbackground="white" )
    label4.pack()
    label4.place(x = 145, y = 250,width = 130, height= 25)

    label3 = Label(text = "NIT:", foreground = "White", bg = "black", font = "Modern", highlightbackground="white" )
    label3.pack()
    label3.place(x = 145, y = 200,width = 120, height= 25)

    

    button_guardar = Button(panel_Frame, text="Guardar Cliente", command= guardar_cliente,  foreground = "white", bg = "black", font = "Modern", highlightbackground="white",highlightthickness=2)
    button_guardar.pack()
    button_guardar.place(x = 230, y = 350 ,width= 150, height  = 40)

    ventana.mainloop()

clientes = []
def guardar_cliente():
    global nombre_texto, nit_texto, correo_texto
    nombre = nombre_texto.get(1.0, tk.END).strip()
    nit = nit_texto.get(1.0, tk.END).strip()
    correo = correo_texto.get(1.0, tk.END).strip()

    if nombre and nit and correo:
        if any(cliente["NIT"] == nit for cliente in clientes):
            messagebox.showerror("Error", "El Cliente ya existe")
        else:
            clientes.append({"Nombre": nombre, "NIT": nit, "Correo": correo})
            messagebox.showinfo("Éxito", "Cliente guardado correctamente.")
            guardar_clientes_html()
    else:
        messagebox.showerror("Error", "Por favor complete todos los campos.")
    return redirect('/')

def guardar_clientes_html():
   with open("templates/index.html", "w") as f:
    f.write("<html><head><title>Clientes Registrados</title>")
    f.write("<style>")
    f.write("body {")
    f.write("    font-family: Arial, sans-serif;")
    f.write("    background-color: #f4f4f4;")
    f.write("    text-align: center;")
    f.write("}")
    f.write("h1 {")
    f.write("    color: #333;")
    f.write("}")
    f.write("table {")
    f.write("    border-collapse: collapse;")
    f.write("    width: 80%;")
    f.write("    margin: 20px auto;")  # Añadir margen superior e inferior para separar la tabla de otros elementos
    f.write("    background-color: #fff;")
    f.write("    border: 1px solid #ddd;")
    f.write("}")
    f.write("th, td {")
    f.write("    padding: 8px;")
    f.write("    border-bottom: 1px solid #ddd;")
    f.write("}")
    f.write("th {")
    f.write("    background-color: #f2f2f2;")
    f.write("}")
    f.write("</style>")
    f.write("</head><body>")
    f.write("<h1>Clientes Registrados</h1>")
    f.write("<table>")
    f.write("<tr>")
    f.write("<th>Nombre</th>")
    f.write("<th>NIT</th>")
    f.write("<th>Correo</th>")
    f.write("</tr>")
    for cliente in clientes:
        nombre = cliente.get('Nombre', 'N/A')
        nit = cliente.get('NIT', 'N/A')
        correo = cliente.get('Correo', 'N/A')
        f.write(f"<tr><td>{nombre}</td><td>{nit}</td><td>{correo}</td></tr>")
    f.write("</table></body></html>")



formulario()