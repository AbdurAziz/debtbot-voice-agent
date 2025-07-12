# Convert text to speech using ElevenLabs or gTTS
import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)  # Words per minute
    engine.setProperty('volume', 1.0)  # Max volume
    engine.say(text)
    engine.runAndWait()

# Test
if __name__ == "__main__":
    speak_text("Absolutely! I’ve pushed your payment to next Friday. Let me know if you need anything else.")
