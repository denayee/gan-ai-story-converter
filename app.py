# { this for run project and create virtual env }
#  python -m venv .venv
# >> .venv\Scripts\activate
# >> pip install streamlit gTTS
# >> streamlit run app.py   

import streamlit as st
from gtts import gTTS
import io

# run project using command: streamlit run app.py

# Streamlit App Title
st.set_page_config(page_title="Story to Audiobook", layout="centered")
st.title("📖 Story to Audiobook")
st.write("Convert your written story into audio using Google Text-to-Speech (gTTS).")

# Initialize Session State
if "audio_data" not in st.session_state:
    st.session_state.audio_data = None

if "story_input" not in st.session_state:
    st.session_state.story_input = ""

# Callback to reset the app properly before widget initialization
def reset_app():
    st.session_state.audio_data = None
    st.session_state.story_input = ""

# Input text area
story_text = st.text_area(
    "✍️ Enter your story below:", 
    height=300, 
    placeholder="Once upon a time...", 
    key="story_input"
)

# Language selection
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Hindi": "hi"
}
selected_lang = st.selectbox("🌐 Choose an accent/language:", list(languages.keys()))
lang_code = languages[selected_lang]

# Accent selection for English
tld = "com"
if selected_lang == "English":
    accents = {
        "United States": "com",
        "United Kingdom": "co.uk",
        "Australia": "com.au",
        "India": "co.in",
        "Canada": "ca"
    }
    selected_accent = st.selectbox("🌎 Choose an English accent:", list(accents.keys()))
    tld = accents[selected_accent]

# Convert button
if st.button("🎧 Convert to Audiobook"):
    if story_text.strip() == "":
        st.warning("⚠️ Please enter a story before converting.")
    else:
        with st.spinner("🔄 Generating voice... Please wait."):
            try:
                # Generate audio using gTTS
                tts = gTTS(text=story_text, lang=lang_code, tld=tld, slow=False)
                
                # Save audio directly into memory (BytesIO) instead of a temporary file
                fp = io.BytesIO()
                tts.write_to_fp(fp)
                st.session_state.audio_data = fp.getvalue()
                st.success("✅ Audio generated successfully!")

            except Exception as e:
                st.error(f"❌ Error generating audio: {e}")

# If audio has been generated and saved in session state, display it
if st.session_state.audio_data:
    st.audio(st.session_state.audio_data, format="audio/mp3")

    st.download_button(
        label="⬇️ Download Audiobook",
        data=st.session_state.audio_data,
        file_name="audiobook.mp3",
        mime="audio/mp3",
    )

st.write("---")
# Reset Button at the bottom
st.button("🗑️ Reset Page", on_click=reset_app)
