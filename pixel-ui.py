import tkinter as tk
from PIL import Image, ImageTk

def draw_pixel(canvas, x, y, color):
    """Draw a single pixel on the canvas."""
    canvas.create_line(x, y, x + 1, y, fill=color)

def draw_image_pixels(canvas, pixels, width, height):
    """Draw the image pixels one by one."""
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Convert RGB values to hex color format
            hex_color = f'#{r:02x}{g:02x}{b:02x}'
            draw_pixel(canvas, x, y, hex_color)
            canvas.update()  # Update canvas to show pixel

# Create a tkinter window
root = tk.Tk()
root.title("Pixel Drawing")

# Set up the image and canvas
width, height = 100, 100
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

# Create a new image with RGB mode, 100x100 pixels
image = Image.new("RGB", (width, height), "white")
pixels = image.load()

# Modify pixels (example)
pixels[10, 10] = (255, 0, 0)  # Red pixel
pixels[20, 20] = (0, 255, 0)  # Green pixel
pixels[30, 30] = (0, 0, 255)  # Blue pixel
for i in range(100):
    pixels[i,50] = (0,0,0)
#
# Draw the pixels on the canvas, pixel by pixel
draw_image_pixels(canvas, pixels, width, height)

# Start the tkinter main loop
root.mainloop()

