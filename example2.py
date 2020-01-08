import argparse,cv2,numpy
from matplotlib import pyplot

def access_pixel_values():
    imagem = cv2.imread('trem.jpg')
    valorPixel = imagem[150,150]
    print(valorPixel)

def access_pixel_gayscale_values():
    imagem = cv2.imread('trem.jpg')
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    valorPixel = imagem[150,150]
    print(valorPixel)

def access_pixel_color_intensity():
    imagem = cv2.imread('trem.jpg')
    valorPixel = imagem[150,150,0]
    print(valorPixel)

def access_data_image():
    imagem = cv2.imread('trem.jpg')
    print(imagem.shape)
    print(imagem.size)

def get_historygram_photo_black_and_white():
    imagem = cv2.imread('trem.jpg')
    pyplot.hist(imagem.ravel(),256,[0,256])
    pyplot.show()

parse = argparse.ArgumentParser()

parse.add_argument("-run", help="run option")

args = parse.parse_args()

if args.run == '1':
    access_pixel_values()
elif args.run == '2':
    access_pixel_gayscale_values()
elif args.run == '3':
    access_pixel_color_intensity()
elif args.run == '4':
    access_data_image()
elif args.run == '5':
    get_historygram_photo_black_and_white()