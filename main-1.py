from lsb import *
from PIL import *
if __name__=='__main__':

    x = encode("lenna.png", "Hello")
    x.save("lenna-henna.png")
