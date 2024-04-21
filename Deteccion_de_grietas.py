# Librerias que vamos a necesitar 
import numpy as np
import cv2
from tkinter import Tk, Label, Button, Frame, Text
from PIL import Image, ImageTk
from tensorflow.keras.models import load_model


#................Funciones.............


# esta funcion es para leer las imagenes adaptarlas para que se vea en el Label 
def video(paso= False, imagen= None, selec= 0):
    global cap, modelo

    if paso== True: cap= True
        
    if cap or paso:
        if selec == 0:

            try:
                _,frame= cap.read()
            except:
                frame = None
        
        if selec == 1:
            frame= imagen

        # Tratar el frame
        if frame is not None:
            frame= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame= cv2.resize(frame, (500, 500))
            predict_image_class(frame= frame, selec= 1, model= modelo)


            # Convertir el video
            frame= Image.fromarray(frame)
            frame= ImageTk.PhotoImage(frame)
        
            video_labe.config(image= frame)
            video_labe.image= frame
            video_labe.after(10, video)
            video_labe.place(x= 650, y= 100)
    


# Esta funcion es para cuando se oprima el boton de activar camara esta es la funcion que se encarga de eso 
def videocam_on():
    global cap


    texto1.config(text= "Video captura: Activada")
    cam_on.place_forget()
    cam_off.place(x= 60, y= 450)
    cap= cv2.VideoCapture(1)
    video()


# Es para apagar la camara 
def videocam_off():

    global cap
    if cap:
        cap.release()
        cap = None
        video_labe.config(image="")

    texto1.config(text= "Video captura: Desactivada")
    cam_off.place_forget()
    cam_on.place(x= 60, y= 450)
    video_labe.place_forget()
    


# Función para preprocesar la imagen
def preprocess_image(image_path= None, selec= 0, frame= None):
    image = cv2.imread(image_path) if selec==0 else frame
    image = cv2.resize(image, (200, 200))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = image / 255.0
    image = np.expand_dims(image, axis=-1)

    return image



# Función para predecir la clase de la imagen
def predict_image_class(image_path= None, model= None, selec= 0, frame= None):
    # Preprocesar la imagen
    preprocessed_image= preprocess_image(image_path) if selec==0 else preprocess_image(frame= frame, selec= 1) 
    prediction = model.predict(np.array([preprocessed_image]))
    predicted_class = np.argmax(prediction)

    # Es para sacar el mensaje que queremos arrojar 
    diccionario= {0:'No Hay Grieta', 1:'Hay Grieta'}
    mensaje= diccionario[predicted_class]
    texto3.config(text= mensaje)

   

# Función para 
def clasificar_imagen(image_path):
    global modelo 

    def callback():
        # Clasificar la imagen y obtener la imagen con el cuadrado
        predict_image_class(image_path, modelo)
        imagen= cv2.imread(image_path)
        video(paso= True, imagen= imagen, selec= 1)
                
    return callback


 
    



#................Codigo principal.............

# Cargar el modelo entrenado
modelo = load_model('Modelo_deteccion_grietas.h5')

# Creamos la instacia de la ventana
pantalla= Tk()

# Abrir las diferentes imagenes que tenemos

imagen_fondo = Image.open("Fondo del proyecto.jpg")
imFondo = ImageTk.PhotoImage(imagen_fondo)

imagen_botones = Image.open("imagen_boton.jpg")
im_botones = ImageTk.PhotoImage(imagen_botones)

cam_on= Image.open("prendido.jpg") 
cam_img_on= ImageTk.PhotoImage(cam_on)

cam_off= Image.open("apagado.jpg")
cam_img_off= ImageTk.PhotoImage(cam_off)


# Valor iniciar de las variables
deteccion= 'No hay deteccion'

# Ventana principal
pantalla.title("DETECTOR DE GRIETAS")
pantalla.geometry("1350x700")


# Fondo
background = Label(image= imFondo, text= "Fondo")
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)


# las etiquetas del Interfaz
texto1= Label(pantalla, text="Video captura: Desactivada")
texto1.place(x= 800, y= 50)

texto2= Label(pantalla, text="Deteccion: ")
texto2.place(x= 50, y= 100)

texto3= Label(pantalla, text= deteccion)
texto3.place(x=110, y= 100)

texto4= Label(pantalla, text="Imagen pruba 1: ")
texto4.place(x= 50, y= 150)

texto5= Label(pantalla, text="Imagen pruba 2: ")
texto5.place(x= 50, y= 200)

texto6= Label(pantalla, text="Imagen pruba 3: ")
texto6.place(x= 50, y= 250)

texto7= Label(pantalla, text="Imagen pruba 4: ")
texto7.place(x= 50, y= 300)

texto8= Label(pantalla, text="Imagen pruba 5: ")
texto8.place(x= 50, y= 350)

texto9= Label(pantalla, text="Imagen pruba 6: ")
texto9.place(x= 50, y= 400)


# Es el label donde se va a mostrar la camara o las imagenes de prueba 
video_labe= Label(pantalla)



# Botones principales del GUI

boton_prueba_1 = Button(pantalla, image=im_botones, height="18", width="80", command=clasificar_imagen('Imagenes de prueba\Grieta.jpg'))
boton_prueba_1.place(x = 150, y = 150)

boton_prueba_2 = Button(pantalla, text="", image=im_botones, height="18", width="80", command=clasificar_imagen('Imagenes de prueba\Copia de 19799.jpg'))
boton_prueba_2.place(x = 150, y = 200)

boton_prueba_3 = Button(pantalla, text="", image=im_botones, height="18", width="80", command=clasificar_imagen('Imagenes de prueba\Grieta 3.jpg'))
boton_prueba_3.place(x = 150, y = 250)

boton_prueba_4 = Button(pantalla, text="", image=im_botones, height="18", width="80", command=clasificar_imagen('Imagenes de prueba\Copia de 19800.jpg'))
boton_prueba_4.place(x = 150, y = 300)

boton_prueba_5 = Button(pantalla, text="", image=im_botones, height="18", width="80", command=clasificar_imagen('Imagenes de prueba\Grieta 6.jpg'))
boton_prueba_5.place(x = 150, y = 350)

boton_prueba_6 = Button(pantalla, text="", image=im_botones, height="18", width="80", command=clasificar_imagen('Imagenes de prueba\Copia de 19801.jpg'))
boton_prueba_6.place(x = 150, y = 400)


# botones para prender y apagar la camara

cam_on= Button(pantalla, text= "camara on", image= cam_img_on, height= "160", width= "160", command=videocam_on)
cam_on.place(x= 60, y= 450)

cam_off= Button(pantalla, text= "Camara off", image= cam_img_off, height= "160", width= "160", command=videocam_off)




