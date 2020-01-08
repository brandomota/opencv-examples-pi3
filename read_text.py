import cv2, pytesseract
import pyttsx3


def ler_texto_imagem(imagem):
    reader = pyttsx3.init()
    texto = pytesseract.image_to_string(imagem,lang='por')
    if len(texto) > 0:
        reader.say(texto)
        reader.runAndWait()


def run():
    stream = cv2.VideoCapture(0)

    while True:
        ret, imagem = stream.read()
        cv2.imshow('teste', imagem)
        imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        ler_texto_imagem(imagem)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    stream.release()
    cv2.destroyAllWindows()


run()