import tkinter as tk
from tkinter import messagebox
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

import expert_system 

def enviar_respuestas():
    respuesta1 = var1.get()
    respuesta2 = var2.get()
    respuesta3 = var3.get()

    if respuesta1 and respuesta2 and respuesta3:
        hechos = []
        if respuesta1 == "Sí":
            hechos.append("Marino")
        elif respuesta1 == "No":
            hechos.append("NoMarino")

        if respuesta2 == "Sí":
            hechos.append("Vertebrado")
        elif respuesta2 == "No":
            hechos.append("NoVertebrado")

        if respuesta3 == "Sí":
            hechos.append("Cuadrupedo")
        elif respuesta3 == "No":
            hechos.append("NoCuadrupedo")

        ambiente_experto = expert_system.inicializar_ambiente()

        for hecho in hechos:
            ambiente_experto.assert_string(f"({hecho})")

        animales_encontrados = expert_system.ejecutar_ambiente(ambiente_experto)

        if animales_encontrados:
            resultado_clasificacion_label.config(text="Clasificación: " + animales_encontrados["clasificacion"])
            resultado_label.config(text="Animales encontrados:\n" + "\n".join(animales_encontrados["animales"]))
        else:
            resultado_label.config(text="No se encontraron animales con esas características.")
    else:
        messagebox.showwarning("Error", "Debes responder todas las preguntas antes de enviar.")

def cerrar_ventana():
    root.destroy()

root = tk.Tk()
root.title("Identificación de Animales")
root.geometry("600x350")  

frame_preguntas = tk.Frame(root, width=300)
frame_resultados = tk.Frame(root, width=300, bg="lightgray")  

frame_preguntas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
frame_resultados.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()

tk.Label(frame_preguntas, text="1. ¿El animal es marino?").pack(anchor="w")
tk.Radiobutton(frame_preguntas, text="Sí", variable=var1, value="Sí").pack(anchor="w")
tk.Radiobutton(frame_preguntas, text="No", variable=var1, value="No").pack(anchor="w")

tk.Label(frame_preguntas, text="2. ¿El animal es vertebrado?").pack(anchor="w")
tk.Radiobutton(frame_preguntas, text="Sí", variable=var2, value="Sí").pack(anchor="w")
tk.Radiobutton(frame_preguntas, text="No", variable=var2, value="No").pack(anchor="w")

tk.Label(frame_preguntas, text="3. ¿El animal es cuadrúpedo?").pack(anchor="w")
tk.Radiobutton(frame_preguntas, text="Sí", variable=var3, value="Sí").pack(anchor="w")
tk.Radiobutton(frame_preguntas, text="No", variable=var3, value="No").pack(anchor="w")

frame_botones = tk.Frame(frame_preguntas)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Enviar", command=enviar_respuestas).pack(side=tk.LEFT, padx=5)

tk.Button(frame_botones, text="Cerrar", command=cerrar_ventana).pack(side=tk.LEFT, padx=5)

tk.Label(frame_resultados, text="Resultados", font=("Arial", 12, "bold"), bg="lightgray").pack()
resultado_clasificacion_label = tk.Label(frame_resultados, text="", fg="black", bg="lightgray")
resultado_label = tk.Label(frame_resultados, text="Aquí aparecerán los resultados...", fg="black", bg="lightgray")
resultado_clasificacion_label.pack(pady=10)
resultado_label.pack(pady=10)

root.mainloop()
