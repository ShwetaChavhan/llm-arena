#TODO
#error handling

"""Provide the Gradio interface for comparing AI model responses."""

# Third-party imports 
import logging
import gradio as gr

# Application imports
from src.logging_config import configure_logging
from src.arena import battle

# Configure application-wide logging before handling user requests
configure_logging()

logger = logging.getLogger(__name__)

def vote(label):
    """Display a confirmation message for the selected vote.

    Args:
        label: Label identifying the selected model and vote.

    Returns:
        A Markdown-formatted confirmation message.
    """
    logger.info("User submitted vote | selection=%s", label)    
    return f"🗳️ Thanks! You voted: **{label}**"   

# Build the interface using Gradio's Blocks layout.
with gr.Blocks(title="LLM Arena") as demo:
    gr.Markdown("# 🥊 LLM Arena — one prompt, two models")
    prompt = gr.Textbox(label="Ask both models the same thing")
    go = gr.Button("⚔️ Battle!", variant="primary")

    with gr.Row():
        with gr.Column():
            gr.Markdown("### 🤖 Model: Gemini")
            out_a = gr.Markdown()
            with gr.Row():
                up_a   = gr.Button("👍");  down_a = gr.Button("👎")
        with gr.Column():
            gr.Markdown("### 🤖 Model: Groq")
            out_b = gr.Markdown()
            with gr.Row():
                up_b   = gr.Button("👍");  down_b = gr.Button("👎")

    # Display feedback after the user votes for a model.
    verdict = gr.Markdown()

    # Send the same prompt to both models and display their responses.
    go.click(battle, inputs=prompt, outputs=[out_a, out_b])
    
    # Upvoting and downvoting buttons
    up_a.click(lambda: vote("👍 Model A"), outputs=verdict)
    down_a.click(lambda: vote("👎 Model A"), outputs=verdict)
    up_b.click(lambda: vote("👍 Model B"), outputs=verdict)
    down_b.click(lambda: vote("👎 Model B"), outputs=verdict)

demo.launch(share=True)