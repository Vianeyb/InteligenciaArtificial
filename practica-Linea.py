import tkinter as tk
from PIL import Image, ImageTk

def draw_pixel(canvas, x, y, color):
    """Dibuja un solo píxel en el lienzo."""
    canvas.create_line(x, y, x + 1, y, fill=color)

def draw_image_pixels(canvas, pixels, width, height):
    """Dibuja los píxeles de la imagen uno por uno (no se usará en esta versión)."""
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Convierte los valores RGB al formato de color hex
            hex_color = f'#{r:02x}{g:02x}{b:02x}'
            draw_pixel(canvas, x, y, hex_color)
            canvas.update()  # Actualiza el lienzo para mostrar el píxel

def lineaD(canvas, x1, y1, x2, y2, color=(0, 0, 0)):
    """Dibuja una línea de (x1, y1) a (x2, y2) en el lienzo."""
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        # Dibuja el píxel en el lienzo
        draw_pixel(canvas, x1, y1, f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}')

        if x1 == x2 and y1 == y2:  # Cuando llegamos al punto final
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

# Crear la ventana para el dibujo 
root = tk.Tk()
root.title("Dibujo de línea pixel a pixel entre dos puntos")

# Configurar el ancho y alto de la imagen
width, height = 110, 110
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

# Llamar a la función que dibuja la línea
lineaD(canvas, 0, 0, 100, 100, color=(255, 0, 0))  # Color rojo como un tuple (R, G, B)

root.mainloop()
