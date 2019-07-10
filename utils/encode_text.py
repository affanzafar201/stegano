

def str2bits(message):
    '''
    converts stream of text to binary message encoded in 8bits
    '''
    temp = list()
    for char in message:
        temp.append(bin(ord(char))[2:].rjust(8,"0"))

    return ''.join(temp)



def setlsb(word, new_bit):
    '''
    sets the lsb of word to new bit
    '''
    return (word & ~1) |  int(new_bit)


