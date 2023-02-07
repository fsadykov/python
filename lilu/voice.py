import speech_recognition as sr

# Set up the speech recognition module
r = sr.Recognizer()

# Start listening for voice input
with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)

# Transcribe the audio to text
text = r.recognize_google(audio)

# Write the transcription to a text file
with open("transcription.txt", "w") as file:
    file.write(text)

print("Transcription written to file.")
