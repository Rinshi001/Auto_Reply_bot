# WhatsApp Auto-Reply Bot 🤖

A Python-based WhatsApp Auto-Reply Bot that automatically reads your WhatsApp messages, generates replies like you using Gemini API, and sends them. This bot uses PyAutoGUI for interacting with the screen and pyperclip to handle clipboard text. It detects new messages in a selected chat, generates human-like replies using Gemini API, automatically pastes and sends messages, runs continuously in a loop, and is easy to set up and customize. 

## Project Explanation

This bot works in the following way: it selects the chat area using PyAutoGUI, copies the messages to the clipboard, generates a reply using Gemini API similar to how you would respond, pastes and sends the reply into WhatsApp Web, and repeats this process continuously to keep replying to new messages as they arrive.

## Setup Instructions

To set up, clone the repository (`git clone https://github.com/Rinshi001/Auto_Reply_bot.git`) and navigate into it (`cd Auto_Reply_bot`). Create a virtual environment (`python -m venv venv`) and activate it (`venv\Scripts\activate` on Windows or `source venv/bin/activate` on Linux/Mac). Install dependencies using `pip install -r requirements.txt`. Create a `.env` file and add your Gemini API key like so: `API_KEY=your_gemini_api_key_here`.

## Finding Correct Chat Coordinates

Since the bot relies on screen coordinates to select chat messages, run `main.py` using `python main.py`. Move your mouse over the top-left and bottom-right corners of the chat area; the script will print the coordinates, which you should copy and paste into `check.py`. For example: `chat_start_x, chat_start_y = 733, 191` and `chat_end_x, chat_end_y = 1823, 925`.

## Running the Bot

Open WhatsApp Web with the correct chat visible and run `check.py` using `python check.py`. The bot will continuously detect new messages, generate replies using Gemini API, and paste and send them automatically.

## Future Enhancements

Future improvements could include detecting messages using WhatsApp Web’s DOM instead of screen coordinates, supporting multiple chats automatically, smarter AI response customization for more natural replies, and improving reliability across different screen resolutions and browser sessions.

## Notes

Adjust coordinates if your screen resolution changes, keep your `.env` file private, and optionally include a `.env.example` for sharing the project setup with others.
