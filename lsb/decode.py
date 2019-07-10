
from stegano import utils

def decode(img_path, shift=0):
    '''
    Decodes the encrypted message
    '''
    img,_ = utils.open_image(img_path)
    width, height = img.size

    buff, count = 0,0
    bitlab = list()
    limit = None

    for row in range(height):
        for col in range(width):

            if shift != 0:
                shift -= 1
                continue

            pixel = img.getpixel((col,row))
            if img.mode == 'RGBA':
                pixel = pixel[:3]

            for color in pixel:
                buff += (color & 1) <<  (8 - 1 -  count)
                count += 1

                if count == 8:
                    bitlab.append(chr(buff))
                    buff, count = 0,0
                    if bitlab[-1] == ':' and limit is None:
                        try:
                            limit = int("".join(bitlab[:-1]))
                        except:
                            pass
            if len(bitlab) - len(str(limit)) - 1 == limit:
                img.close()
                return "".join(bitlab[len(str(limit))+1:])
