from openai import OpenAI
import soundfile as sf

client = OpenAI()

text = "come out to show them"

# Available TTS voices
voices = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]

for voice in voices:
    print(f"Generating audio with voice: {voice}")
    
    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",  # neural TTS
        voice=voice,
        input=text
    )
    
    filename = f"come_out_to_show_them_{voice}.wav"
    with open(filename, "wb") as f:
        f.write(response.read())
    
    print(f"Saved: {filename}")

