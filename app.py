import streamlit as st
import asyncio
import pyaudio

from QuickAgent import ConversationManager

def get_audio():
    """
    Function to capture audio using PyAudio
    """
    p = pyaudio.PyAudio()

    # Define audio stream parameters
    # You can adjust these values based on your needs
    sample_rate = 44100
    chunk = 1024
    format = pyaudio.paInt16
    channels = 1

    stream = p.open(format=format,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=chunk)

    frames = []

    # Record audio for a short duration (adjust as needed)
    for _ in range(0, int(sample_rate / chunk * 2)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop the stream and close PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()

    return b''.join(frames)

def main():
    st.title("Speech Recognition Interface")

    if st.button("Start Recording"):
        audio_data = get_audio()
        manager = ConversationManager()
        # Pass the captured audio data to the ConversationManager
        manager.process_audio(audio_data)

        # Rest of your code for displaying conversation history

    st.sidebar.markdown("## Instructions")
    st.sidebar.info(
        """
        1. Click the "Start Recording" button to begin the speech recognition process.
        2. Speak your message clearly.
        3. The recognized speech and the corresponding response from the language model will be displayed.
        4. Say "goodbye" to exit the conversation.
        """
    )

if __name__ == "__main__":
    main()
