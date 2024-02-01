import pytube
import whisper

import logging
import sys
import argparse

parser = argparse.ArgumentParser(description="Transcribe un video de YouTube usando Whisper")

# parser.add_argument("--video", help="Introduce el link del video de Youtube a transcribir")
args = parser.parse_args()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

# if not args.video:
#     logging.error('Por favor introduce una url de YouTube a transcribir')
#     exit()

# se carga modelo de whisper
logging.info('Descargando el modelo "small" de Whisper')
model = whisper.load_model('small')

# variable que carga el video de YT
# youtubeVideoId = "https://youtube.com/shorts/cz-DaqClllQ?si=-gBSFcBCvRzVoZyz"
# se recupera el video de YT
# youtubeVideo = pytube.YouTube(args.video)
youtubeVideoId = input("Introduce el link del video de Youtube a transcribir y presiona enter: ")
logging.info("Descargando el video de YoutTube...")
youtubeVideo = pytube.YouTube(youtubeVideoId)

# se convierte el video en audio
logging.info("Obteniendo el audio del video...")
audio = youtubeVideo.streams.get_audio_only()
# se descarga el archivo de audio
audio.download(filename ='tmp.mp4')

# se guarda los resultados del modelo
logging.info("Transcribiendo el audio...")
result = model.transcribe('tmp.mp4')

print(result["text"])

"""
Hoy te voy a enseñar cómo puedes usar inteligencia artificial y Python para pasar un vídeo de YouTube a texto. 
Lo primero y más importante es que necesitas estas dependencias:
whisper, pytube y por supuesto FFMP. 
Importamos las dependencias de pythup y whisper. 
Creamos una variable con nuestro vídeo de YouTube y una variable donde vamos a cargar el modelo de whisper. 
En este caso vamos a utilizar el small que es bastante rápido y funciona bien. 
Recuperamos el vídeo de YouTube con pytube y lo convertimos en audio.
Vamos a descargar este archivo de audio. 
Hemos una variable result donde guardaremos los resultados del modelo. 
Una vez que estamos transcribiendo el archivo que habíamos descargado. Y finalmente solo tenemos que pintar los resultados. Guardamos los cambios y ejecutamos nuestro fichero.
Es normal que tarda un poco porque tiene que descargarse el modelo que son unos cuantos megas y además 
utilizando machine learning va a entender el audio. Y después de un rato ya tenemos justamente el texto de nuestro vídeo transcrito. Si te ha gustado esto dale like.
"""
