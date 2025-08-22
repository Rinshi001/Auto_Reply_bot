import pyautogui
import pyperclip
import time
from generate_reply import gen_reply

# -----------------------------
# CONFIGURATION
# -----------------------------
# Coordinates for selecting the latest message area (bottom of chat)
chat_start_x, chat_start_y = 800, 700
chat_end_x, chat_end_y = 1800, 900

# Coordinates for message input box
message_box_x, message_box_y = 1500, 950

# Interval between checking for new messages
poll_interval = 5

# Keep track of last processed message
last_message = ""

# -----------------------------
# START BOT
# -----------------------------
print("WhatsApp Auto-Reply Bot started. Press Ctrl+C to stop.")
time.sleep(5)  # Give user time to focus WhatsApp Web

while True:
    try:
        # -----------------------------
        # 1️⃣ Copy the latest chat portion
        # -----------------------------
        pyautogui.click(chat_start_x, chat_start_y)
        pyautogui.moveTo(chat_start_x, chat_start_y)
        pyautogui.dragTo(chat_end_x, chat_end_y, duration=0.3, button='left')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)
        chat_text = pyperclip.paste()

        # -----------------------------
        # 2️⃣ Extract last line (latest message)
        # -----------------------------
        chat_lines = chat_text.strip().split('\n')
        if len(chat_lines) == 0:
            continue
        latest_message = chat_lines[-1]

        # -----------------------------
        # 3️⃣ Check if it's new
        # -----------------------------
        if latest_message != last_message:
            last_message = latest_message
            print("New message detected:", latest_message)

            # -----------------------------
            # 4️⃣ Generate reply using Gemini API
            # -----------------------------
            reply = gen_reply(chat_text)
            print("Generated reply:", reply)

            # -----------------------------
            # 5️⃣ Paste reply into WhatsApp
            # -----------------------------
            pyperclip.copy(reply)
            time.sleep(0.5)
            pyautogui.click(message_box_x, message_box_y)
            time.sleep(0.2)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.2)
            pyautogui.press('enter')
            print("Reply sent!")

        # -----------------------------
        # 6️⃣ Wait before next check
        # -----------------------------
        time.sleep(poll_interval)

    except KeyboardInterrupt:
        print("Bot stopped by user.")
        break

    except Exception as e:
        print("Error:", e)
        time.sleep(poll_interval)
