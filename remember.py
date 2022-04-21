from PIL import Image


def decode_image(path):
    """
    The function decodes an image by to the position of the black pixels
    :param path: A path of the image to decode
    :return: A decoded string
    """
    image = Image.open(path,'r')
    pixels=image.load() # load the pixels
    width,height=image.size
    black_pixels_rows = [i for j in range(height) for i in range(width) if pixels[i,j] == 1] # find the rows of the black pixels
    chars=[chr(pix) for pix in black_pixels_rows]  # decode the row number to char
    return "".join(chars)  
