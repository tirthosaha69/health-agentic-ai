import os
import base64
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Convert image to required format
image_path = "download 2.jpg"

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

model = "llama-3.2-90b-vision-preview"

def analyze_image_with_query(query, model, encoded_image):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))  # Ensure API key is loaded

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}},
            ]
        }
    ]

    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content

# Define query
# query = "Is that normal on skin, doctor?"

# # Run function and print result
# print(analyze_image_with_query(query=query, model=model, encoded_image=encode_image(image_path)))
