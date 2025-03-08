import tkinter as tk
from tkinter import messagebox
import sys
import os

# Obtener el directorio padre (donde está expert_system.py)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

import expert_system  # Ahora debería funcionar la importación

def enviar_respuestas():
    """Obtiene las respuestas, las envía al sistema experto y muestra los resultados."""
    respuesta1 = var1.get()
    respuesta2 = var2.get()
    respuesta3 = var3.get()

    if respuesta1 and respuesta2 and respuesta3:
        # Convertir respuestas en hechos compatibles con CLIPS
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

        # Buscar animales con esas características
        animales_encontrados = expert_system.buscar_animal_por_caracteristicas(hechos)

        # Mostrar resultados en el frame derecho
        if animales_encontrados:
            resultado_label.config(text="Animales encontrados:\n" + "\n".join(animales_encontrados))
        else:
            resultado_label.config(text="No se encontraron animales con esas características.")
    else:
        messagebox.showwarning("Error", "Debes responder todas las preguntas antes de enviar.")

def cerrar_ventana():
    """Cierra la ventana principal."""
    root.destroy()

# Crear ventana principal
root = tk.Tk()
root.title("Identificación de Animales")
root.geometry("600x350")  # Aumentamos el ancho para acomodar los dos paneles

# Crear dos frames para dividir la interfaz en dos columnas
frame_preguntas = tk.Frame(root, width=300)
frame_resultados = tk.Frame(root, width=300, bg="lightgray")  # Fondo gris para diferenciar

frame_preguntas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
frame_resultados.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Variables para almacenar las respuestas
var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()

# Preguntas en el frame izquierdo
tk.Label(frame_preguntas, text="1. ¿El animal es marino?").pack(anchor="w")
tk.Radiobutton(frame_preguntas, text="Sí", variable=var1, value="Sí").pack(anchor="w")
tk.Radiobutton(frame_preguntas, text="No", variable=var1, value="No").pack(anchor="w")

tk.Label(frame_preguntas, text="2. ¿El animal es vertebrado?").pack(anchor="w")
tk.Radiobutton(frame_preguntas, text="Sí", variable=var2, value="Sí").pack(anchor="w")
tk.Radiobutton(frame_preguntas, text="No", variable=var2, value="No").pack(anchor="w")

tk.Label(frame_preguntas, text="3. ¿El animal es cuadrúpedo?").pack(anchor="w")
tk.Radiobutton(frame_preguntas, text="Sí", variable=var3, value="Sí").pack(anchor="w")
tk.Radiobutton(frame_preguntas, text="No", variable=var3, value="No").pack(anchor="w")

# Frame para alinear los botones horizontalmente
frame_botones = tk.Frame(frame_preguntas)
frame_botones.pack(pady=10)

# Botón para enviar respuestas
tk.Button(frame_botones, text="Enviar", command=enviar_respuestas).pack(side=tk.LEFT, padx=5)

# Botón para cerrar la ventana
tk.Button(frame_botones, text="Cerrar", command=cerrar_ventana).pack(side=tk.LEFT, padx=5)

# Sección de resultados en el frame derecho
tk.Label(frame_resultados, text="Resultados", font=("Arial", 12, "bold"), bg="lightgray").pack()
resultado_label = tk.Label(frame_resultados, text="Aquí aparecerán los resultados...", fg="black", bg="lightgray")
resultado_label.pack(pady=10)

# Ejecutar la ventana
root.mainloop()
