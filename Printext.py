import tkinter as tk
from tkinter import filedialog
from PIL import Image
import pytesseract
import pyperclip

def extract_text_from_image(image_path):
    """
    Extract text from an image using Tesseract-OCR
    """
    text = pytesseract.image_to_string(Image.open(image_path))
    return text

def load_image():
    """
    Load an image file using a file dialog
    """
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", ".jpg .jpeg .png .bmp")])
    if image_path:
        image_entry.delete(0, tk.END)
        image_entry.insert(0, image_path)
        extract_and_display_text()

def extract_and_display_text():
    """
    Extracts text from the image and displays it in the text area
    """
    image_path = image_entry.get()
    if image_path:
        extracted_text = extract_text_from_image(image_path)
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, extracted_text)

def copy_text():
    """
    Copies the extracted text to the clipboard
    """
    text = text_area.get("1.0", tk.END).strip()
    pyperclip.copy(text)

root = tk.Tk()
root.title("Printext")

image_label = tk.Label(root, text="Image File:")
image_label.grid(row=0, column=0, padx=5, pady=5)

image_entry = tk.Entry(root, width=50)
image_entry.grid(row=0, column=1, padx=5, pady=5)

load_button = tk.Button(root, text="Load Image", command=load_image)
load_button.grid(row=0, column=2, padx=5, pady=5)

text_area = tk.Text(root, wrap=tk.WORD, height=10, width=50)
text_area.grid(row=1, columnspan=3, padx=5, pady=5)

copy_button = tk.Button(root, text="Copy Text", command=copy_text)
copy_button.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
