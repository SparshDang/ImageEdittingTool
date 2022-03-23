from PIL import Image
from imageEnhancementClass import ImageEnhancement
from imageTransposeClass import ImageTransposing
import os


class ImageClass(ImageEnhancement, ImageTransposing):
    def __init__(self, image):
        if isinstance(image, str):
            self.imagePath = image
            self.image = Image.open(self.imagePath)
        else:
            self.image = image
        ImageEnhancement.__init__(self, self.image)
        ImageTransposing.__init__(self, self.image)

    def showImage(self):
        edittedImage = self.getEdittedImage()
        edittedImage.show()

    def getEdittedImage(self):
        imageEnhancementEdit = self.getEnhancementEdittedImage()
        wholeImage = self.getTransposedImage(imageEnhancementEdit)
        return wholeImage

    def saveImage(self, name):
        edittedImage = self.getEdittedImage()
        newImageName = name + self.getFileExtension()
        edittedImage.save(newImageName)

    def getFileExtension(self):
        return os.path.splitext(self.imagePath)[1]

    def getNameToSave(self):
        return input('Enter File Name: ')

    def getImageDimensions(self):
        return self.image.size

    def reduceImageDimesion(self, values):
        self.image = self.image.resize(values)

    def getPILImage(self):
        return self.image


if __name__ == '__main__':
    newImage = ImageClass('test_image.jpg')
    while True:
        print('''
Choose Option:)
  1)Change Contrast
  2)Change Brightness
  3)Change Sharpness
  4)Change Color
  5)Flip Horizontally
  6)Flip Vertically
  7)Show
  8)Save Image
  9)Exit
''')

        chosenOption = int(input('Enter Option:  '))
        if chosenOption == 9:
            break

        elif chosenOption == 1:
            newContrast = int(input('Enter Number between -100 and 100: '))
            newImage.changeContrast(newContrast)
        elif chosenOption == 2:
            newBrightness = int(input('Enter Number between -100 and 100: '))
            newImage.changeBrightness(newBrightness)
        elif chosenOption == 3:
            newSharpness = int(input('Enter Number between -100 and 100: '))
            newImage.changeSharpness(newSharpness)
        elif chosenOption == 4:
            newColor = int(input('Enter Number between -100 and 100: '))
            newImage.changeColor(newColor)
        elif chosenOption == 5:
            newImage.flipImageHorizontally()
        elif chosenOption == 6:
            newImage.flipImageVertically()

        elif chosenOption == 7:
            newImage.showImage()
        elif chosenOption == 8:
            newImage.saveImage()
