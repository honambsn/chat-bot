import speech_recognition as sr
import openai
import time
import pygame

# Initialize OpenAI API
openai.api_key = "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"

# Function to recognize speech
def recognize_speech(timeout=3):
    recognizer = sr.Recognizer()
    pygame.init()
    pygame.mixer.init()
    countdown_sound = pygame.mixer.Sound("tone2.wav")
    countdown_sound.play()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        for i in range(timeout, 0, -1):
            print(i, end=" ", flush=True)
            time.sleep(1)
        print("\nSpeak now!")
        countdown_sound.stop()  # Stop the countdown sound
        audio = recognizer.listen(source, timeout=timeout)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Error fetching results; {0}".format(e))
    return None

# Function to interact with ChatGPT API
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo-0613:personal::8wBiYAPJ",  # eng-ver.
        #model = "ft:gpt-3.5-turbo-0613:personal::8wtkKqNW", #vn ver.
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()


# Main function
def main():
    while True:
        # Get input from speech
        speech_text = recognize_speech()
        if speech_text:
            if speech_text.lower() in ["quit", "exit", "bye"]:
                break
            # Interact with ChatGPT using the recognized speech as input
            gpt_response = chat_with_gpt(speech_text)
            print("GPT response:", gpt_response)
            # Add any additional processing or actions based on the GPT response

# Call the main function to start the program
if __name__ == "__main__":
    main()
