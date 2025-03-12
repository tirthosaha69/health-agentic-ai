import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO


def record_audio(file_path, timeout=20, phrase_time_limit=None):
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now...")

            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete")

            # Convert audio to WAV bytes
            wav_data = audio_data.get_wav_data()

            # Convert WAV to MP3 using pydub
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")

            logging.info(f"✅ Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"❌ An error occurred: {e}")

# Example Usage
# audio_filepath="patient_voice_test.mp3"
# record_audio(file_path=audio_filepath)


from dotenv import load_dotenv
from groq import Groq
load_dotenv()

def transcribe_with_groq(audio_filepath):
    client = Groq()
    sst_model = "whisper-large-v3"
    audio_file = open(audio_filepath, "rb")
    transcription = client.audio.transcriptions.create(
        model=sst_model,
        file=audio_file,
        language="en"
    )

    return transcription.text


# output = "tirtho.mp3"
# record_audio(output)
# print(transcribe_with_groq(output))