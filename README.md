### Secret of Monkey Island
The purpose of this repo is to replicate the GPT game found in this [video](https://www.youtube.com/watch?v=EYLFam1qymk&t=2s), without needing to sign up for a ClosedAI token.

Tech stack is as follows:
- Streamlit for the UI
- Falcon 180B for text generation and image prompt generation
- SDXL for image generation (the prompt could be improved)
- ElevenLabs for text to speech

You can try a demo [here](https://monkey-island-os-5azshv4egpgrydfhvn33rb.streamlit.app/). You will have to sign in t yoru huggingface account to use this, and I'm not sure how streamlit handles secrets, so use at your own risk.