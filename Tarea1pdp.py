from PIL import Image 
from PIL import ImageDraw

class Proyect:
    def __init__(self,filename):
        self.list = []
        self.file = filename
        self.png = Image.open(self.file).convert('RGB')

    def add_image(self):
        self.list.append(self.file)

    def show_image(self):
        return self.png.show()
    def save_image(self):
        self.png.save(self.file)
    
    def get_information(self):
        pass



class Filter(Proyect):

    def __init__(self, filename,filter):
        super(). __init__(filename)
        self.filter = filter
        self.pixel = self.png.load()

        pass



im=Proyect('pipa')
im.show_image()