from PIL import Image 

# Create a new image with RGB mode, 100x100 pixels, white background
image = Image.new("RGB", (100, 100), "white")
pixels = image.load()  # Create the pixel map

# Draw some pixels
pixels[10, 10] = (255, 0, 0)  # Red pixel at (10, 10)
pixels[20, 20] = (0, 255, 0)  # Green pixel at (20, 20)
pixels[30, 30] = (0, 0, 255)  # Blue pixel at (30, 30)
for i in range(100):
    pixels[i,50] = (0,0,0)
# Save the image
image.save("pixels_image.png")

# Display the image (optional)
image.show()

