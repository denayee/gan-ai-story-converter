# { this for run project and create virtual env }
#  python -m venv .venv
# >> .venv\Scripts\activate
# >> pip install streamlit requests
# >> streamlit run app.py   

import streamlit as st
from elevenlabs import generate, set_api_key, voices
import tempfile
import os
from dotenv import load_dotenv

load_dotenv()
# run project using command: streamlit run app.py

# Streamlit App Title
st.set_page_config(page_title="Story to Audiobook", layout="centered")
st.title("📖 Story to Audiobook")
st.write("Convert your written story into a human-like voice using ElevenLabs.")

# Load API Key
api_key = os.getenv("ELEVENLABS_API_KEY")

if not api_key:
    st.error("⚠️ API Key not found. Please add ELEVENLABS_API_KEY to your .env file.")
    st.stop()

# Set API key for fetching voices
set_api_key(api_key)

# Dynamically fetch voices available to this user account
@st.cache_data(show_spinner=False)
def get_available_voices():
    try:
        v_list = voices()
        return [v.name for v in v_list]
    except Exception as e:
        st.warning(f"Could not load voices dynamically: {e}")
        return ["Rachel", "Drew", "Clyde", "Domi", "Bella", "Antoni"] # Fallbacks

available_voices = get_available_voices()

# Input text area
story_text = st.text_area(
    "✍️ Enter your story below:", height=300, placeholder="Once upon a time..."
)

# Voice selection
if available_voices:
    voice = st.selectbox("🎙️ Choose a valid voice from your account:", available_voices)
else:
    voice = st.text_input("🎙️ Enter a voice name manually:", "Rachel")

# Convert button
if st.button("🎧 Convert to Audiobook"):
    if story_text.strip() == "":
        st.warning("⚠️ Please enter a story before converting.")
    else:
        with st.spinner("🔄 Generating voice... Please wait."):
            try:
                # Generate audio
                audio = generate(
                    text=story_text,
                    voice=voice,
                    model="eleven_multilingual_v2",
                    api_key=api_key
                )

                # Save to temp file
                with tempfile.NamedTemporaryFile(
                    delete=False, suffix=".mp3"
                ) as tmp_file:
                    tmp_file.write(audio)
                    tmp_path = tmp_file.name

                # Audio player
                st.success("✅ Audio generated successfully!")
                st.audio(tmp_path, format="audio/mp3")

                # Download button
                with open(tmp_path, "rb") as f:
                    st.download_button(
                        "⬇️ Download Audiobook",
                        f,
                        file_name="audiobook.mp3",
                        mime="audio/mp3",
                    )

                # Cleanup temp file after download
                os.remove(tmp_path)

            except Exception as e:
                st.error(f"❌ Error: {e}")
