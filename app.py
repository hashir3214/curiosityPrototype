import os
import gradio as gr
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Chat history storage
chat_history = []

def chat_with_curiosity(message, history):
    """
    Chat function that interacts with Groq API using Llama models.

    Args:
        message: User's input message
        history: Chat history from Gradio

    Returns:
        Updated chat history
    """
    try:
        # Build messages array from history
        messages = []

        # Add system message
        messages.append({
            "role": "system",
            "content": "You are Curiosity AI, a helpful and knowledgeable AI assistant powered by Groq. You are curious, thoughtful, and eager to help users learn and explore new ideas."
        })

        # Add conversation history
        for user_msg, assistant_msg in history:
            messages.append({"role": "user", "content": user_msg})
            if assistant_msg:
                messages.append({"role": "assistant", "content": assistant_msg})

        # Add current message
        messages.append({"role": "user", "content": message})

        # Call Groq API with streaming
        response_text = ""
        stream = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Using Groq's powerful open-source model
            messages=messages,
            temperature=0.7,
            max_tokens=2048,
            stream=True
        )

        # Stream the response
        for chunk in stream:
            if chunk.choices[0].delta.content:
                response_text += chunk.choices[0].delta.content
                yield response_text

    except Exception as e:
        error_message = f"Error: {str(e)}\n\nPlease make sure your GROQ_API_KEY is set correctly."
        yield error_message

def clear_chat():
    """Clear the chat history."""
    return []

# Create Gradio interface
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # 🔍 Curiosity AI

        Welcome to Curiosity AI! I'm powered by Groq's lightning-fast inference with Llama 3.3 70B.
        Ask me anything - I'm here to help you learn and explore!
        """
    )

    chatbot = gr.Chatbot(
        label="Chat with Curiosity AI",
        height=500,
        show_copy_button=True
    )

    with gr.Row():
        msg = gr.Textbox(
            label="Your message",
            placeholder="Type your message here...",
            scale=4,
            show_label=False
        )
        submit_btn = gr.Button("Send", scale=1, variant="primary")

    with gr.Row():
        clear_btn = gr.Button("Clear Chat", scale=1)

    gr.Markdown(
        """
        ---
        **Note:** This app requires a Groq API key. Get yours at [console.groq.com](https://console.groq.com)
        """
    )

    # Event handlers
    msg.submit(chat_with_curiosity, inputs=[msg, chatbot], outputs=[chatbot])
    msg.submit(lambda: "", None, msg)  # Clear input after submit

    submit_btn.click(chat_with_curiosity, inputs=[msg, chatbot], outputs=[chatbot])
    submit_btn.click(lambda: "", None, msg)  # Clear input after submit

    clear_btn.click(clear_chat, None, chatbot)

if __name__ == "__main__":
    # Check if API key is set
    if not os.environ.get("GROQ_API_KEY"):
        print("WARNING: GROQ_API_KEY environment variable is not set!")
        print("Please set it in your .env file or as an environment variable.")
        print("Get your API key at: https://console.groq.com")

    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False
    )
