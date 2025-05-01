import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np

# Function to load and process the image
def convert_to_sketch():
    try:
        # Open file dialog to select an image
        file_path = filedialog.askopenfilename()
        if not file_path:
            return

        # Read the image
        img = cv2.imread(file_path)

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Invert the grayscale image
        inverted_gray_image = 255 - gray_image

        # Blur the inverted image
        blurred_image = cv2.GaussianBlur(inverted_gray_image, (111, 111), 0)

        # Invert the blurred image
        inverted_blurred_image = 255 - blurred_image

        # Create the pencil sketch
        sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

        # Convert the original image and sketch to images that can be displayed in Tkinter
        original_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        original_image = Image.fromarray(original_rgb)
        original_image.thumbnail((400, 400))  # Resize to fit the window
        original_tk = ImageTk.PhotoImage(original_image)

        sketch_rgb = cv2.cvtColor(sketch, cv2.COLOR_GRAY2RGB)
        sketch_image = Image.fromarray(sketch_rgb)
        sketch_image.thumbnail((400, 400))  # Resize to fit the window
        sketch_tk = ImageTk.PhotoImage(sketch_image)

        # Display the images in the Tkinter window
        original_label.config(image=original_tk)
        original_label.image = original_tk  # Keep a reference to the image

        result_label.config(image=sketch_tk)
        result_label.image = sketch_tk  # Keep a reference to the image

        # Enable the save button after processing
        save_button.config(state=tk.NORMAL)

        # Store the sketch image for saving
        global sketch_to_save
        sketch_to_save = sketch_image

    except Exception as e:
        messagebox.showerror("Error", f"Error processing the image: {e}")

# Function to save the pencil sketch image
def save_sketch():
    try:
        # Open file dialog to select location to save the sketch
        save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("All Files", "*.*")])
        if not save_path:
            return

        # Save the sketch image
        sketch_to_save.save(save_path)
        messagebox.showinfo("Success", f"Sketch saved successfully at {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving the image: {e}")

# Set up the main window
root = tk.Tk()
root.title("Image to Pencil Sketch Converter")
root.geometry("850x600")

# Set up the layout
header_label = tk.Label(root, text="Image to Pencil Sketch Converter", font=("Arial", 18))
header_label.pack(pady=20)

# Button to trigger image selection and conversion
convert_button = tk.Button(root, text="Select Image", command=convert_to_sketch, font=("Arial", 14))
convert_button.pack(pady=10)

# Frame to hold the original image and the sketch side by side
image_frame = tk.Frame(root)
image_frame.pack(pady=20)

# Labels to display the original image and the pencil sketch
original_label = tk.Label(image_frame)
original_label.grid(row=0, column=0, padx=10)

result_label = tk.Label(image_frame)
result_label.grid(row=0, column=1, padx=10)

# Button to save the pencil sketch
save_button = tk.Button(root, text="Save Sketch", command=save_sketch, font=("Arial", 12), state=tk.DISABLED)
save_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
