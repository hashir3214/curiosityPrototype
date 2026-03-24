# 🔍 Curiosity AI - Gradio Chat Application

A conversational AI application powered by Groq's lightning-fast inference and Llama 3.3 70B model, built with Gradio for an intuitive chat interface.

## Features

- 💬 Interactive chat interface powered by Gradio
- ⚡ Ultra-fast responses using Groq API
- 🤖 Powered by Llama 3.3 70B Versatile model
- 📝 Conversation history tracking
- 🎨 Clean and modern UI

## Prerequisites

- Python 3.8 or higher
- Groq API key (get one at [console.groq.com](https://console.groq.com))

## Installation

1. Clone the repository:
```bash
git clone https://github.com/hashir3214/curiosityPrototype.git
cd curiosityPrototype
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment:
```bash
cp .env.example .env
```

4. Add your Groq API key to the `.env` file:
```
GROQ_API_KEY=your_actual_api_key_here
```

## Usage

Run the application:
```bash
python app.py
```

The app will start on `http://localhost:7860`. Open this URL in your browser to start chatting with Curiosity AI!

## About Groq

Groq provides ultra-fast LLM inference, making conversations with AI feel instantaneous. This app uses the Llama 3.3 70B Versatile model, one of the most capable open-source language models available.

## Model Information

- **Model**: Llama 3.3 70B Versatile
- **Provider**: Groq
- **Context Window**: 128k tokens
- **Capabilities**: General-purpose conversational AI with strong reasoning and knowledge

## License

MIT License
