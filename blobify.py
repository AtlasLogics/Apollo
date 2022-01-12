import re
import base64

def blobify():
    """
    Accepts a base64 encoded canvas string such as that returned by Canvas.toDataURL() and transforms
    it into a Blob() object. This operation however is typically performed in reverse by the
    canvas.toDataURL() function however for research purposes this is composed below.
    """
    canvas = input()
    pattern = re.compile(";|,")
    filetype, encoding, data = re.split(pattern, canvas[5:])
    data = [ord(byte) for byte in base64.b64decode(data).decode('ISO-8859-1')]
    return {'size': len(data), 'type': filetype, 'data': data}
    
if __name__ == '__main__':
    blobify()