# LLM Arena

Get answers from two AI models for the same prompt and compare them side by side.

## Overview

LLM Arena is a Python application that sends a user-provided prompt to two AI models and displays their responses side by side. It provides a simple interface for comparing answers and voting for a preferred response.

The application uses Gradio for its user interface and OpenAI-compatible API clients to communicate with Google Gemini and Groq-hosted models.


## Features

- Dual-model comparison: Submit the same prompt to two AI models.

- Side-by-side responses: View both answers in a single interface.

- Response voting: Upvote or downvote a model's response.

- Error handling: Display user-friendly messages when model requests fail.

- Application logging: Record application events and errors for debugging.

- Environment-based configuration: Store API credentials outside the source code.



## Tech Stack
- Language: Python
- User interface: Gradio
- AI API client: OpenAI Python SDK
- Model providers: Google Gemini and Groq
- Configuration: dotenv
- Logging: Python standard library


## Project Structure
    llm-arena/
        ├── src/
        │   ├── arena.py
        │   ├── model_clients.py
        │   └── logging_config.py
        ├── app.py
        ├── .env.example
        ├── .gitignore
        ├── requirements.txt
        └── README.md


## Module Responsibilities

app.py — Builds and launches the Gradio interface and connects user actions to application functions.

src/arena.py — Coordinates model requests and collects responses for comparison.

src/model_clients.py — Initializes API clients for Gemini and Groq.

src/logging_config.py — Configures application logging.



## Getting Started

    
Prerequisites

- Python 3.10 or a compatible version supported by the installed dependencies.

- A Gemini API key.

- A Groq API key.


1.  Clone the repository
   
    ```bash    
        git clone https://github.com/ShwetaChavhan/llm-arena.git

        cd llm-arena
    ```

2.  Create a virtual environment

    ```bash
        python -m venv .venv
    ```
    
    Activate it.

    *Windows*

    ```bash
        .venv\Scripts\activate
    ```

    *macOS / Linux*

    ```bash
        source .venv/bin/activate
    ```

3.  Install dependencies

    ```bash
        pip install -r requirements.txt
    ```

4.  Configure environment variables

    Create a *.env* file in the project root. Copy content of *.env.example* file into *.env*. Replace the placeholder values with your own API keys.

    **Never commit .env or expose API keys in source code, screenshots, or logs.**


5.  Run the application

    From the project root, execute:

    ```bash
        python app.py
    ```

    Open the local Gradio URL displayed in the terminal.


## How to Use

1. Enter a question or instruction in the prompt field.

2. Click Battle! to request answers from both models.

3. Compare the responses displayed side by side.

4.  Use the voting buttons to select your preferred response.




## Limitations

- Model responses may differ in accuracy, completeness, and style.

- API availability, rate limits, and usage quotas depend on the providers.

- Voting is currently intended as interface feedback; persistent vote storage requires additional implementation.

- The application requires valid API credentials and an internet connection.



## Future Improvements

- Execute model requests concurrently to reduce response time.

- Add persistent voting and comparison history.

- Allow users to select models and configure generation parameters.


## Author

**Shweta Chavhan**

🎯 Project Purpose

This project was built as a learning project to gain hands-on experience with AI API integration.

GitHub:  [Shweta Chavhan](https://github.com/ShwetaChavhan) 