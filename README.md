# Clasificación de grietas en paredes de concreto

## Introducción

Este proyecto tiene como objetivo desarrollar una herramienta para clasificar grietas en paredes de concreto utilizando un modelo de aprendizaje automático y una interfaz gráfica sencilla (GUI). La herramienta está diseñada para ser utilizada por personal sin experiencia previa en programación o aprendizaje automático, permitiendo una evaluación rápida y sencilla del estado de las paredes de concreto.

## Descripción del proyecto

El proyecto se compone de los siguientes elementos:

* **Modelo de aprendizaje automático:** Un modelo de red neuronal entrenado para clasificar imágenes de grietas en paredes de concreto como positivas (requieren reparación) o negativas (no requieren reparación).
* **Interfaz gráfica de usuario (GUI):** Una interfaz sencilla que permite al usuario cargar una imagen de una grieta y obtener la clasificación del modelo.
* **Conjunto de datos de imágenes:** Un conjunto de datos de imágenes de grietas positivas y negativas utilizado para entrenar el modelo de aprendizaje automático.
* **Código fuente:** El código fuente del modelo de aprendizaje automático, la GUI y las instrucciones para su uso.

## Características

* Clasificación de grietas en paredes de concreto con alta precisión.
* Interfaz gráfica sencilla e intuitiva.
* Fácil de usar para personal sin experiencia previa en programación o aprendizaje automático.
* Potencial para ser utilizado en inspecciones de infraestructura, evaluación de edificios y otras aplicaciones.

## Beneficios

* Permite una evaluación rápida y precisa del estado de las paredes de concreto.
* Reduce la necesidad de inspecciones manuales por parte de expertos.
* Ayuda a identificar grietas que requieren reparación de forma preventiva, evitando daños mayores y costos adicionales.
* Facilita la toma de decisiones informadas sobre el mantenimiento y la reparación de estructuras de concreto.

## Tecnologías utilizadas

* **Lenguaje de programación:** Python
* **Biblioteca de aprendizaje automático:** TensorFlow o Keras
* **Marco de trabajo para GUI:** Tkinter 
* **Bibliotecas de procesamiento de imágenes:** OpenCV o Pillow

## Estructura del proyecto

* Carpeta de imagenes de prueba
* Carpeta de imagenes negativo
* Carpeta de imagenes positivas
* Archivos de entrenamiento de la red neuronal CNN_Detector de grietas.ipynb
* archivo de imprementacion de la red neuronal Deteccion_de_grietas.py
* imagenes para los gui
* las imagenes que dice imagen gui # son las fotos del proyecto


## Instrucciones de uso

1. Clonar el repositorio del proyecto en tu computadora local.
2. Instalar las dependencias necesarias utilizando el archivo 
3. Entrenar el modelo de aprendizaje automático ejecutando el archivo CNN_Detector de grietas.ipynb.
4. De entrenar el modelo le va a salir la red ya entrenada en un archivo .h5, tener el archivo en la misma carpeta.
5. Ejecutar el archivo Deteccion_de_grietas.py para iniciar la interfaz gráfica de usuario.
6. Probar el archivo con imagenes ya cargadas o con la camara.
7. La interfaz gráfica mostrará la clasificación del modelo (positiva o negativa) para la grieta.
