import streamlit as st
import whisper

st.title('Audio transcription app')

audio = st.file_uploader('Upload your audio file', type=['mp3', 'wav', 'm4a'])

@st.cache
def load_model():
    model = whisper.load_model('base')
    return model

model = load_model()

if model:
    st.write('Whisper model is loaded')

if st.sidebar.button('Transcribe audio'):
    if audio:
        st.sidebar.success('Transcribing your audio file')
        transcription = model.transcribe(audio.name)
        st.sidebar.success('Transcription is completed')
        st.markdown(transcription['text'])
    else:
        st.sidebar.error('Upload your audio file')

st.sidebar.header('Play original audio file')
st.sidebar.audio(audio)