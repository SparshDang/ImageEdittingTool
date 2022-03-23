from fileinput import filename
from tkinter import *
from tkinter.font import BOLD
from tkinter import filedialog
from tkinter.messagebox import showinfo
from PIL import ImageTk

from imageClass import ImageClass


class ImageEdittingTool(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1000x600')
        self.title('Image Editing Tool')

        self.image = None
        self.edittedImage = None
        self.fileSaveStatus = True

        self.__createTitleFrame()
        self.__createEditingFrame()
        self.__createCanvas()

    def __createTitleFrame(self):
        titleFrame = Frame(self, pady=5)
        titleFrame.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        titleLabel = Label(
            titleFrame, text='Image Editing Tool', font=('Arial', 30, BOLD))
        titleLabel.pack()

    def __createEditingFrame(self):
        self.editingFrame = Frame(self)
        self.editingFrame.place(relx=0, rely=0.1, relheight=0.9, relwidth=0.4)

        self.__createContrastScale()
        self.__createContrastLabel()
        self.__createBrightnessScale()
        self.__createBrightnessLabel()
        self.__createColorScale()
        self.__createColorLabel()
        self.__createSharpnessScale()
        self.__createSharpnessLabel()

        self.__createFlippingFrame()
        self.__createFlippingButtons()

        self.__createFileButtonsFrame()
        self.__createFileButtons()

    def __createContrastScale(self):
        self.contrastScale = Scale(
            self.editingFrame, from_=-100, to=100, orient='horizontal')
        self.contrastScale.pack(fill='x')
        self.contrastScale.bind('<B1-Motion>', self.__contrastChange)

    def __contrastChange(self, event):
        newContrast = self.contrastScale.get()
        if self.image:
            self.image.changeContrast(newContrast)
            self.__updateImage()

    def __createContrastLabel(self):
        contrastLabel = Label(
            self.editingFrame, text='Contrast', font=('Arial', 12, NORMAL))
        contrastLabel.pack(fill='x')

    def __createBrightnessScale(self):
        self.brightnessScale = Scale(
            self.editingFrame, from_=-100, to=100, orient='horizontal')
        self.brightnessScale.pack(fill='x')
        self.brightnessScale.bind('<B1-Motion>', self.__brightnessChange)

    def __brightnessChange(self, event):
        newBrighness = self.brightnessScale.get()
        if self.image:
            self.image.changeBrightness(newBrighness)
            self.__updateImage()

    def __createBrightnessLabel(self):
        brghtnessLabel = Label(
            self.editingFrame, text='Brightness', font=('Arial', 12, NORMAL))
        brghtnessLabel.pack(fill='x')

    def __createColorScale(self):
        self.colorScale = Scale(
            self.editingFrame, from_=-100, to=100, orient='horizontal')
        self.colorScale.pack(fill='x')
        self.colorScale.bind('<B1-Motion>', self.__colorChange)

    def __colorChange(self, event):
        newColor = self.colorScale.get()
        if self.image:
            self.image.changeColor(newColor)
            self.__updateImage()

    def __createColorLabel(self):
        colorLabel = Label(
            self.editingFrame, text='Color', font=('Arial', 12, NORMAL))
        colorLabel.pack(fill='x')

    def __createSharpnessScale(self):
        self.sharpnessScale = Scale(
            self.editingFrame, from_=-100, to=100, orient='horizontal')
        self.sharpnessScale.pack(fill='x')
        self.sharpnessScale.bind('<B1-Motion>', self.__sharpnessChange)

    def __sharpnessChange(self, event):
        newsharpness = self.sharpnessScale.get()
        if self.image:
            self.image.changeSharpness(newsharpness)
            self.__updateImage()

    def __createSharpnessLabel(self):
        sharpnessLabel = Label(
            self.editingFrame, text='Sharpness', font=('Arial', 12, NORMAL))
        sharpnessLabel.pack(fill='x')

    def __createFlippingFrame(self):
        self.flipButtonsFrame = LabelFrame(self.editingFrame, text='Flip')
        self.flipButtonsFrame.pack(fill='x')

    def __createFlippingButtons(self):
        self.horizontalFlip = Button(self.flipButtonsFrame, text='Horizonatal')
        self.horizontalFlip.pack(side=LEFT, fill='x', expand=True)
        self.horizontalFlip.bind('<Button-1>', self.__doHorizontalFlip)

        self.verticalFlip = Button(self.flipButtonsFrame, text='Vertical')
        self.verticalFlip.pack(side=LEFT, fill='x', expand=True)
        self.verticalFlip.bind('<Button-1>', self.__doVerticalFlip)

    def __doHorizontalFlip(self, event):
        if self.image:
            self.image.flipImageHorizontally()
            self.__updateImage()

    def __doVerticalFlip(self, event):
        if self.image:
            self.image.flipImageVertically()
            self.__updateImage()

    def __createFileButtonsFrame(self):
        self.fileButtonsFrame = LabelFrame(
            self.editingFrame, text='File Settings')
        self.fileButtonsFrame.pack(fill='x')

    def __createFileButtons(self):
        self.openButton = Button(self.fileButtonsFrame, text='Open')
        self.openButton.pack(side=LEFT, expand=True, fill='x')
        self.openButton.bind('<Button-1>', self.__openImage)

        self.saveButton = Button(self.fileButtonsFrame, text='Save')
        self.saveButton.pack(side=LEFT, expand=True, fill='x')
        self.saveButton.bind('<Button-1>', self.__saveImage)

    def __openImage(self, event):
        self.__selectImageToOpen()
        self.__reduceImageSizeToFit()
        self.__placeImageInCanvas()
        self.__reset()

    def __selectImageToOpen(self):
        fileName = filedialog.askopenfilename()
        self.image = ImageClass(fileName)

    def __reduceImageSizeToFit(self):
        canvasWidth, canvasHeight = self.__getCanvasSize()
        imageWidth, imageHeight = self.image.getImageDimensions()
        if imageWidth > canvasWidth or imageHeight > canvasHeight:
            sizeToReduce = min(canvasWidth/imageWidth,
                               canvasHeight/imageHeight)

            newWidth = int(sizeToReduce * imageWidth)
            newHeight = int(sizeToReduce * imageHeight)
            self.image.reduceImageDimesion((newWidth, newHeight))
            self.edittedImage = self.image

    def __placeImageInCanvas(self):
        x, y = self.__getPositionOfImage()
        image = self.__getTkinterImage()
        self.canvas.background = image
        self.canvas.create_image(
            x, y, image=image, anchor=NW)

    def __getCanvasSize(self):
        return (self.canvas.winfo_width(), self.canvas.winfo_height())

    def __getPositionOfImage(self):
        canvasWidth, canvasHeight = self.__getCanvasSize()
        imageWidth, imageHeight = self.image.getImageDimensions()

        x = canvasWidth//2 - imageWidth//2
        y = canvasHeight//2 - imageHeight//2

        return x, y

    def __getTkinterImage(self):
        tkImage = ImageTk.PhotoImage(self.edittedImage.getPILImage())
        return tkImage

    def __createCanvas(self):
        self.canvas = Canvas(self, bg='white')
        self.canvas.place(relx=0.4, rely=0.1, relwidth=0.6, relheight=0.9)

    def __updateImage(self):
        self.edittedImage = ImageClass(self.image.getEdittedImage())
        self.canvas.delete('all')
        self.__placeImageInCanvas()

    def __saveImage(self, event):
        if self.image:
            fileName = filedialog.asksaveasfilename()
            self.image.saveImage(fileName)
            showinfo('Image Save', 'image Saved')

    def __reset(self):
        self.contrastScale.set(0)
        self.sharpnessScale.set(0)
        self.brightnessScale.set(0)
        self.colorScale.set(0)


if __name__ == '__main__':
    gui = ImageEdittingTool()
    gui.mainloop()
