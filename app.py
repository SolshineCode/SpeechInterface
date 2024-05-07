import streamlit as st
import asyncio
from QuickAgent import ConversationManager

def main():
    st.title("Speech Recognition Interface")

    if st.button("Start Recording"):
        manager = ConversationManager()
        asyncio.run(manager.main())

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
