import os
from elevenlabs import ElevenLabs, save
from playsound import playsound
from dotenv import load_dotenv
import platform
import subprocess
from gtts import gTTS
import elevenlabs
from elevenlabs.client import ElevenLabs
import edge_tts
import asyncio
load_dotenv()


def autoplay(output_filepath):
    os_name = platform.system()

    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif os_name == "Windows":  # Windows (Play MP3 directly using ffplay)
            subprocess.run(['ffplay', '-nodisp', '-autoexit', output_filepath], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif os_name == "Linux":  # Linux
            subprocess.run(['mpg123', output_filepath], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")
        


def text_to_speech_with_gtts(input_text, output_filepath):
    # Generate and save MP3
    tts = gTTS(text=input_text, lang='en')
    tts.save(output_filepath)

    os_name = platform.system()

    autoplay(output_filepath=output_filepath)
    return output_filepath

# text_to_speech_with_gtts(input_text="hello guys welcome back to my youtube channel ", output_filepath="ans.mp3")


def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs()
    audio = client.generate(
        text=input_text,
        voice="Dorothy",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

    os_name = platform.system()

    autoplay(output_filepath=output_filepath)
    return output_filepath


async def text_to_speech_edge_tts(text_input, output_filepath):
    communicate = edge_tts.Communicate(text_input, "en-US-JennyNeural")
    await communicate.save(output_filepath)
    
    autoplay(output_filepath=output_filepath)
    return output_filepath
    
    

# # Test
# input_text = "hello guys , welcome to my youtube channel"
# output_filepath = "voice_logs/test.mp3"
# text_to_speech_with_elevenlabs(input_text=input_text, output_filepath=output_filepath)


# asyncio.run(text_to_speech_edge_tts(text_input="How you guys doing ?", output_filepath="output.mp3"))











# microsoft edge




