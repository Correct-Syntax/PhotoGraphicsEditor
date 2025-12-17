import base64

def create_imagestring(image, filename):
    with open(image, 'rb') as img:
        image_string = base64.encodebytes(img.read())

        file = open(filename, 'w')
        file.write(str(image_string))
        file.close()
        print('successfully saved bytes:', image_string, 'to file:', filename)


create_imagestring('arrow_open.gif', '.dat')
