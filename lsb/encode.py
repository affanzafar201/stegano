
from stegano import utils

def encode(path_of_img, message, shift=0):
    '''
    Encode the message to image
    '''
    len_message = len(message)
    assert len_message != 0, "length of message is 0"

    img, new_img = utils.open_image(path_of_img)
    
    if img.mode not in ['RGB', 'RGBA']:
        img = img.convert('RGB')

    width, height = img.size
    message  = str(len_message) + ":" + str(message)
    message_bits = utils.str2bits(message)
    message_bits += "0"* ((3 - len(message_bits)%3)%3)
    print(message_bits)
    npixels = width*height

    bitstream = iter(message_bits)
    if len(message_bits) > npixels*3:
        raise Exception("The message is too long to be hidden in this image")

    for row in range(height):
        for col in range(width):

            if shift !=0:
                shift -=1
                continue

            try:
                pixel = img.getpixel((col,row))

                r = utils.setlsb(pixel[0],next(bitstream))
                g = utils.setlsb(pixel[1],next(bitstream))
                b = utils.setlsb(pixel[2],next(bitstream))

                if img.mode == 'RGBA':
                    new_img.putpixel((col,row),(r,g,b,pixel[3]))
                else:
                    new_img.putpixel((col,row),(r,g,b))

            except StopIteration:
                img.close()
                return new_img




