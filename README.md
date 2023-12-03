### Secret of Monkey Island
The purpose of this repo is to replicate the GPT game found in this [video](https://www.youtube.com/watch?v=EYLFam1qymk&t=2s), without needing to sign up for a ClosedAI token. Most of the actual inference is run through huggingface Spaces.

Tech stack is as follows:
- Streamlit for the UI
- [Falcon 180B](https://huggingface.co/chat/) for text generation and image prompt generation
- [SDXL](https://openskyml-fast-sdxl-stable-diffusion-xl.hf.space/--replicas/545b5tw7n/) for image generation (the prompt could be improved)
- [ElevenLabs](https://elevenlabs-tts.hf.space/) for text to speech

Preferably you would use a [TPU edition of SDXL](https://google-sdxl.hf.space/), which is a loot faster, also less precise on prompts, but sadly, there is no API. 

Same goes for ElevenLabs, which has a cap on 250 characters of text, preferably, I would use [StyleTTS2](https://huggingface.co/spaces/styletts2/styletts2), but it's not available as an API.

You can try a demo [here](https://monkey-island-os-5azshv4egpgrydfhvn33rb.streamlit.app/). You will have to sign in t yoru huggingface account to use this, and I'm not sure how streamlit handles secrets, so use at your own risk.