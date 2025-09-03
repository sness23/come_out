from openai import OpenAI
import soundfile as sf

client = OpenAI()

text = "come out to show them"

# Available TTS voices (updated list from docs)
voices = ["alloy", "ash", "ballad", "coral", "echo", "fable", "nova", "onyx", "sage", "shimmer"]

# Voice style variations using instructions
style_variations = [
    ("normal", "Speak at a normal pace."),
    ("fast", "Speak quickly and energetically."),
    ("very_fast", "Speak very rapidly and urgently."),
    ("slow", "Speak slowly and deliberately."),
    ("documentary", "Speak in a raw, unpolished, documentary tone with a grainy, slightly metallic texture, as if recorded on a 1960s tape recorder. Deliver the words quietly and matter-of-factly, with an undertone of fatigue and trauma. Keep the rhythm steady, with sharp consonants and elongated vowels, intimate yet ghostly, as though reluctantly recounting a painful memory.")
]

for voice in voices:
    for style_name, instruction in style_variations:
        print(f"Generating audio with voice: {voice}, style: {style_name}")
        
        response = client.audio.speech.create(
            model="gpt-4o-mini-tts",
            voice=voice,
            input=text,
            instructions=instruction
        )
        
        filename = f"come_out_to_show_them_{voice}_{style_name}.wav"
        with open(filename, "wb") as f:
            f.write(response.read())
        
        print(f"Saved: {filename}")

