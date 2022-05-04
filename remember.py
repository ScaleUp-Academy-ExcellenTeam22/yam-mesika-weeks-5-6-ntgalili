from PIL import Image


def decode_image(path: str) -> str:
    """
    The function decodes an image according to the position of the black pixels.
    :param path: A path of the image to decode
    :return: A decoded string
    """
    image = Image.open(path,'r')
    pixels=image.load() # load the pixels
    width,height=image.size
    black_pixels_rows = [i for j in range(width) for i in range(height) if pixels[j,i] == 1] # find the rows of the black pixels
    return "".join([chr(pix) for pix in black_pixels_rows])  # decode the row number to char



#print(decode_image("C:\\Users\\nechama\\Notebooks\\week06\\resources\\code.png"))