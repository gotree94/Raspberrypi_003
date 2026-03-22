from openai import OpenAI
import pygame
import tempfile
import os
import time

#client = OpenAI(api_key="sk-proj-************************")

pygame.init()
pygame.mixer.init()

print("Type text to speak.")

while True:
    text = input("TTS> ")

    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=text,
        response_format="wav"
    )

    audio_bytes = response.read()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio_bytes)
        wav_path = f.name

    pygame.mixer.music.load(wav_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    os.remove(wav_path)
