from PIL import Image


class ImageTransposing:
    def __init__(self, image: Image):
        self.image = image
        self.isHorizontallyFlipped = False
        self.isVerticallyFlipped = False

    def flipImageHorizontally(self):
        self.isHorizontallyFlipped = not self.isHorizontallyFlipped

    def flipImageVertically(self):
        self.isVerticallyFlipped = not self.isVerticallyFlipped

    def getTransposedImage(self, image=None):

        edittedImage = image
        if self.isHorizontallyFlipped:
            edittedImage = edittedImage.transpose(Image.FLIP_LEFT_RIGHT)
        if self.isVerticallyFlipped:
            edittedImage = edittedImage.transpose(Image.FLIP_TOP_BOTTOM)
        return edittedImage
