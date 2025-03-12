import gradio as gr
from dotenv import load_dotenv
load_dotenv()

from brain_of_the_doctor import encode_image, analyze_image_with_query 
from voice_of_the_patient import transcribe_with_groq, record_audio
from voice_of_the_doctor import text_to_speech_with_gtts, text_to_speech_edge_tts, text_to_speech_with_elevenlabs

system_prompt = """You are a highly experienced doctor, I know you are not, but this is for learning purposes. What's in this image? 
                   Do you find anything wrong with it medically? If you make a differential, suggest some remedies for them. 
                   Don't add any numbers or special characters in your response. Your response should be in one long paragraph. 
                   Also, always answer as if you are answering a real person. Don't respond as an AI model in markdown, 
                   and your answer should mimic that of an actual doctor, not an AI bot. 
                   Keep your answer concise (max 2 sentences). No preamble, start your answer right away, please."""


def process_inputs(audio_filepath, image_filepath):
    speech_to_text_output = transcribe_with_groq(audio_filepath=audio_filepath)

    if image_filepath:
        encoded_image = encode_image(image_filepath)
        doctor_response = analyze_image_with_query(
            query=system_prompt + " " + speech_to_text_output,
            model="llama-3.2-90b-vision-preview",
            encoded_image=encoded_image
            
        )
    else:
        doctor_response = "No image provided for me to analyze."

    output_filepath = "final.mp3"
    text_to_speech_with_gtts(doctor_response, output_filepath)
    
    return speech_to_text_output, doctor_response, output_filepath


# process_inputs()
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio("final.mp3") 
    ],
    title="AI Doctor with Vision and Voice"
)

iface.launch(debug=True)
