# STT logic using OpenAI Whisper or Google STT
import speech_recognition as sr

def listen_and_transcribe():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print(" Speak into the mic...")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"📝 You said: {text}")
        return text
    except sr.UnknownValueError:
        print("⚠️ Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"❌ API error: {e}")
        return ""

# Test
if __name__ == "__main__":
    listen_and_transcribe()
