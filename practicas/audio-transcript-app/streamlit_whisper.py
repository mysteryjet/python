import streamlit as st
import whisper
import pytube


st.title("Youtube a texto")
# https://youtube.com/shorts/QOkp9CIqBkY?si=-l7z8Hwv6kO3ReGS

# se carga el archivo de audio con streamlit
# audio_file = st.file_uploader("Sube tu audio", type=["wav", "mp3", "m4a"])

# se carga el modelo
st.sidebar.text("Carga de modelo de Whisper")
model = whisper.load_model("base")
st.sidebar.success("Modelo Whisper Cargado")

formbtn = st.button("Comienza tu transcripción")
if "formbtn_state" not in st.session_state:
    st.session_state.formbtn_state = False

if formbtn or st.session_state.formbtn_state:
    st.session_state.formbtn_state = True

    st.subheader("Link de Youtube")

    # insertar link de video de Youtube
    with st.form("Form audio"):
        st.write("Por favor, escribe el link del video de Youtube:")
        youtubeVideoId = st.text_input("link de tu video")
        
        # cada form, debe tener un boton de submit
        submitted = st.form_submit_button(label="Enviar")
        # checando que no esté vacio el text_input
        if submitted:
            st.write(submitted)
            if youtubeVideoId:
                st.success(f"Link del video: {youtubeVideoId}")
                youtubeVideo = pytube.YouTube(youtubeVideoId)
                # se convierte el video en audio
                audio_file = youtubeVideo.streams.get_audio_only()
                # se descarga el archivo de audio
                audio_file.download(filename='tmp.mp4')
                # reproducir el audio en la side bar
                st.sidebar.header("Reproducir Archivo de audio:")
                st.sidebar.audio('tmp.mp4')    
                # se guardan los resultados de transcripcion del modelo
                result = model.transcribe('tmp.mp4')
                st.text_area(result["text"])
                st.sidebar.success("Transcrición Completa")
                
            else:
                st.warning("Por favor, introduce un link de YouTube")
        

# carga del modelo
# @st.cache_resource
# def load_whisper_model():
#     model = whisper.load_model("base")
#     return model


"""

"""

# st.sidebar.button("Transcribir audio")
# st.sidebar.success("Transcribiendo audio")


# else:
#     st.sidebar.error("Por favor sube un archivo de audio")

# if st.sidebar.header("Reproducir Archivo de audio:"):
#     st.sidebar.audio(audio_file)