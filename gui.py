# gui.py
from tkinter import filedialog

class PhotoToSketchConverterGUI(PhotoToSketchConverter):
    def __init__(self, root):
        super().__init__(root)

        self.save_button = Button(root, text="Save Sketch", command=self.save_sketch)
        self.save_button.pack()

    def save_sketch(self):
        if self.image_path:
            sketch_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if sketch_path:
                cv2.imwrite(sketch_path, cv2.cvtColor(self.sketch_image, cv2.COLOR_GRAY2BGR))

if __name__ == "__main__":
    root = Tk()
    app = PhotoToSketchConverterGUI(root)
    root.mainloop()
