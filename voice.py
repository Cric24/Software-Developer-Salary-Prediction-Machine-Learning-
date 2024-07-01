import streamlit as st
import speech_recognition as sr
from datetime import datetime
from feedback import feedback_form 

def run_voice_feedback():
    # Function to capture voice input
    def capture_voice():
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            st.write("Please speak...")
            recognizer.adjust_for_ambient_noise(source)
            audio_data = recognizer.listen(source)

        return audio_data

    # Display a button to capture voice input
    if st.button("Start Recording Voice", key="start_recording"):
        audio_data = capture_voice()

        # Perform speech-to-text conversion
        if audio_data:
            recognizer = sr.Recognizer()
            try:
                text = recognizer.recognize_google(audio_data)
                st.text_area("Voice Input", value=text, height=200)
                st.session_state["voice_text"] = text  # Store the voice input in session state
            except sr.UnknownValueError:
                st.write("Could not understand audio")
            except sr.RequestError as e:
                st.write("Could not request results; {0}".format(e))

    # Add a button to submit feedback
    if st.button("Submit Voice Feedback", key="submit_voice_feedback"):
        # Process the feedback (store it in feedback.txt)
        if "voice_text" in st.session_state:
            feedback_text = st.session_state["voice_text"]
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("feedback.txt", "a") as file:
                file.write(f"{timestamp}: {feedback_text}\n")
            st.success("Thank you for your feedback!")
        else:
            st.warning("Please capture voice input first before submitting feedback.")

    feedback_form()

# Run the voice feedback functionality when this file is executed directly
if __name__ == "__main__":
    run_voice_feedback()
