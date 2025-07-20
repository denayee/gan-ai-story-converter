import streamlit as st
from elevenlabs import generate, play
import tempfile
import os
# run project using command: streamlit run app.py 

# Streamlit App Title
st.set_page_config(page_title="Story to Audiobook", layout="centered")
st.title("📖 Story to Audiobook")
st.write("Convert your written story into a human-like voice using ElevenLabs.")

# Input text area
story_text = st.text_area("✍️ Enter your story below:", height=300, placeholder="Once upon a time...")

# Voice selection
voice = st.selectbox("🎙️ Choose a voice:", [
    "Aria", "Sarah", "Laura", "Charlie", "George", "Callum",
    "River", "Liam", "Charlotte", "Alice", "Matilda", "Will",
    "Jessica", "Eric", "Chris", "Brian", "Daniel", "Lily", "Bill"
])




# Convert button
if st.button("🎧 Convert to Audiobook"):
    if story_text.strip() == "":
        st.warning("⚠️ Please enter a story before converting.")
    else:
        with st.spinner("🔄 Generating voice... Please wait."):
            try:
                
                api_key = "sk_a1173cf72eeb470cec61716edaf14778bb1050b49b2e7481" 

                # Generate audio
                audio = generate(
                    text=story_text,
                    voice=voice,
                    api_key=api_key
                )

                # Save to temp file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                    tmp_file.write(audio)
                    tmp_path = tmp_file.name

                # Audio player
                st.success("✅ Audio generated successfully!")
                st.audio(tmp_path, format='audio/mp3')

                # Download button
                with open(tmp_path, "rb") as f:
                    st.download_button("⬇️ Download Audiobook", f, file_name="audiobook.mp3", mime="audio/mp3")

                # Cleanup temp file after download
                os.remove(tmp_path)

            except Exception as e:
                st.error(f"❌ Error: {e}")
