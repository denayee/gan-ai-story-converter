# Story to Audiobook Converter 📖🎧

A Python web application built with Streamlit that converts your written stories into high-quality, human-like audiobooks using the [ElevenLabs API](https://elevenlabs.io/).

## Features
- **Easy-to-use Interface:** Built with Streamlit for a clean, intuitive experience.
- **Multiple Voices:** Choose from a wide selection of ElevenLabs premium voices.
- **Audio Playback:** Listen to the generated audiobook directly in the browser.
- **Downloadable Audio:** Save the generated audiobook as an `.mp3` file.

## Prerequisites
- Python 3.8+
- An [ElevenLabs](https://elevenlabs.io/) API key.

## Installation

1. **Clone or Download** this repository.
2. **Install Required Packages:**
   ```bash
   pip install streamlit elevenlabs python-dotenv
   ```
3. **Configure the Environment Variable:**
   Create a `.env` file in the project's root directory and add your ElevenLabs API key:
   ```env
   ELEVENLABS_API_KEY=your_actual_api_key_here
   ```

## Running the App

1. Open your terminal in the project directory.
2. Run the following command:
   ```bash
   streamlit run app.py
   ```
3. Your browser will automatically open the app. Enter your story, select a voice, and click **Convert to Audiobook**.
