# AI Doctor with Vision and Voice

## Overview
AI Doctor with Vision and Voice is an AI-powered health assistant that takes voice input from patients, processes medical images, and provides diagnostic insights with speech-based responses. It integrates **speech recognition**, **image analysis**, and **text-to-speech** functionalities.

## Features
- 🎤 **Speech Recognition**: Converts patient audio input to text using **Groq Whisper API**.
- 🏥 **Medical Image Analysis**: Uses **LLaMA-3.2 Vision** to analyze medical images and provide diagnostic insights.
- 🔊 **AI Doctor Response**: Generates professional doctor-like responses.
- 🔁 **Text-to-Speech**: Converts AI doctor's response into audio using **Google TTS, ElevenLabs, and Edge TTS**.
- 🌐 **Gradio UI**: Provides an interactive web interface for easy usage.

## Installation
### 1️⃣ Clone the repository
```bash
git clone https://github.com/tirthosaha69/health-agentic-ai.git
cd health-agentic-ai
```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Set Up Environment Variables
Create a `.env` file and add your API keys:
```
GROQ_API_KEY=your_groq_api_key
```

## Usage
### Run the Application
```bash
python gradio_app.py
```
### Gradio Interface
The app runs locally. Open the displayed **localhost URL** in your browser.

## Project Structure
```
health_agentic_ai/
│── main.py                # Gradio interface and core functionality
│── brain_of_the_doctor.py # Image encoding & AI-based medical analysis
│── voice_of_the_doctor.py # Text-to-speech (TTS) processing
│── voice_of_the_patient.py # Speech recognition (STT) and recording
│── requirements.txt       # Dependencies
│── .env                   # API keys and environment variables
```

## How It Works
1. **User speaks into the microphone** 🎤
2. **Speech is transcribed** into text using Groq Whisper
3. **If an image is provided**, it is analyzed using LLaMA-3 Vision
4. **Doctor-like response is generated** with AI
5. **Response is converted into speech** using TTS models
6. **User receives both text and audio responses**

## Future Improvements 🚀
- Integrate **multilingual support** for broader accessibility.
- Enhance **diagnostic accuracy** with additional AI models.
- Deploy the app using **Flask/Django for production**.

## Contributing 🤝
Pull requests are welcome! Open an issue for bug reports or feature requests.

## License 📝
This project is licensed under the **MIT License**.

