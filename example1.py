import cv2,sys

parameter_dict = {}

def load_image():
    image = cv2.imread('trem.jpg')
    cv2.imshow("trem", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def load_video():
    camera = 0 if parameter_dict['camera'] is None else int(parameter_dict['camera'])
    print(camera)
    captura = cv2.VideoCapture(0)

    while True:
        ret, frame = captura.read()
        cv2.imshow('imagem', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    captura.release()
    cv2.destroyAllWindows()

def load_color_segmentation():
    image = cv2.imread('trem.jpg')

    blue, green, red = cv2.split(image)

    cv2.imshow('Red channel', red)

    cv2.imshow('Blue Channel', blue)

    cv2.imshow('Green Channel', green)

    cv2.imwrite('trem-red-channel.jpg',red)
    cv2.imwrite('trem-green-channel.jpg', green)
    cv2.imwrite('trem-blue-channel.jpg', blue)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def load_segmentation_images():
    image_red = cv2.imread("trem-red-channel.jpg")
    image_blue = cv2.imread("trem-blue-channel.jpg")
    image_green = cv2.imread("trem-green-channel.jpg")
    image = cv2.merge((image_blue, image_green, image_red))
    cv2.imshow("trem", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def convert_gray_tones():
    imagem = cv2.imread("trem.jpg")
    imagem = cv2.cvtColor(imagem,cv2.COLOR_RGB2GRAY)
    cv2.imshow(imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def convert_HSV_image():
    imagem = cv2.imread('trem.jpg')
    imagem = cv2.cvtColor(imagem,cv2.COLOR_BGR2HSV)
    matriz, saturacao, valor = cv2.split(imagem)

    cv2.imshow('Canal H', matriz)
    cv2.imshow('Canal S', saturacao)
    cv2.imshow('Canal V',valor)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def merge_HGV_image():
    imagem = cv2.imread('trem.jpg')
    imagem = cv2.cvtColor(imagem,cv2.COLOR_BGR2HSV)
    matriz, saturacao, valor = cv2.split(imagem)
    image_merge = cv2.merge((matriz,saturacao,valor))
    #image_merge = cv2.cvtColor(image_merge, cv2.COLOR_HSV2BGR)
    cv2.imshow("nome",image_merge)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def load_params():
    for user_input in sys.argv[1:]:
        if "=" not in user_input:
            continue
        varname = user_input.split("=")[0]
        varvalue = user_input.split("=")[1]
        parameter_dict[varname] = varvalue

def main():
    load_params()
    start_option = parameter_dict['run']

    if start_option == '1':
        load_image()
    elif start_option == '2':
        load_video()
    elif start_option == '3':
        load_color_segmentation()
    elif start_option == '4':
        load_segmentation_images()
    elif start_option == '5':
        convert_gray_tones()
    elif start_option == '6':
        convert_HSV_image()
    elif start_option == '7':
        merge_HGV_image()

main()
