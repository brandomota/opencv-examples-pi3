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

main()
