# main.py
import cv2
from tkinter import Tk, Canvas, Button, PhotoImage, filedialog
from PIL import Image, ImageTk

class PhotoToSketchConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo to Sketch Converter")

        self.canvas = Canvas(root, width=600, height=400)
        self.canvas.pack()

        self.load_button = Button(root, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.convert_button = Button(root, text="Convert to Sketch", command=self.convert_to_sketch)
        self.convert_button.pack()

        self.image_path = ""
        self.photo_image = None

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image_path = file_path
            image = Image.open(file_path)
            self.photo_image = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor="nw", image=self.photo_image)

    def convert_to_sketch(self):
        if self.image_path:
            original_image = cv2.imread(self.image_path)
            gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
            inverted_image = cv2.bitwise_not(gray_image)
            blurred_image = cv2.GaussianBlur(inverted_image, (111, 111), 0)
            inverted_blurred_image = cv2.bitwise_not(blurred_image)
            sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

            cv2.imshow("Sketch", sketch_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    app = PhotoToSketchConverter(root)
    root.mainloop()
