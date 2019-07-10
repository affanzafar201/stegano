
from PIL import Image

def open_image(img):
    '''
    Opens an image 
    '''
    image = Image.open(img,'r')

    new_image = image.copy()
    return image,new_image
