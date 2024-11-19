from PIL import Image 
from PIL import ImageFilter

imagem = Image.open('avenger.png')

desfocada = imagem.filter(ImageFilter.BLUR)

desfocada.show()
