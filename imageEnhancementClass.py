from PIL import ImageEnhance


class ImageEnhancement:
    def __init__(self, image):
        self.image = image

        self.appliedEnhancements = {
            'Contrast': 1,
            'Brightness': 1,
            'Color': 1,
            'Sharpness': 1,
        }
        self.enhancementsFunctions = {
            'Contrast': ImageEnhance.Contrast,
            'Brightness': ImageEnhance.Brightness,
            'Color': ImageEnhance.Color,
            'Sharpness': ImageEnhance.Sharpness,
        }

    def changeContrast(self, value):
        self.appliedEnhancements['Contrast'] = self.convertValueInRange(value)

    def changeBrightness(self, value):
        self.appliedEnhancements['Brightness'] = self.convertValueInRange(
            value)

    def changeSharpness(self, value):
        self.appliedEnhancements['Sharpness'] = self.convertValueInRange(value)

    def changeColor(self, value):
        self.appliedEnhancements['Color'] = self.convertValueInRange(value)

    def convertValueInRange(self, value):
        return (value/100) + 1

    def getEnhancements(self):
        return self.appliedEnhancements

    def getEnhancementEdittedImage(self):
        edittedImage = self.image.copy()
        for enhancement, value in self.getEnhancements().items():
            edittedImage = self.enhancementsFunctions[enhancement](
                edittedImage)
            edittedImage = edittedImage.enhance(value)
        return edittedImage
