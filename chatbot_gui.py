import tkinter as tk
from tkinter import messagebox

# Simple rule-based chatbot logic.
def get_bot_response(user_input: str) -> str:
    normalized = user_input.strip().lower()

    if normalized in ["quit", "exit", "bye"]:
        return "Goodbye! Have a great day."
    elif "hello" in normalized or "hi" in normalized or "hey" in normalized:
        return "Hello! Nice to meet you."
    elif "how are you" in normalized or "how are you doing" in normalized:
        return "I'm just a simple chatbot, but I'm doing well. Thanks for asking!"
    elif normalized == "help":
        return "I can respond to greetings, tell you how I'm doing, and say goodbye. Try typing 'hello', 'how are you', or 'bye'."
    elif "your name" in normalized or "what's your name" in normalized:
        return "I'm a small rule-based bot created to demonstrate a simple Python GUI."
    else:
        return "I'm not sure how to respond to that. Try saying hello or type 'help'."


class ChatbotGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Chatbot")
        self.geometry("400x300")
        self.resizable(False, False)

        # Welcome label.
        welcome_label = tk.Label(self, text="Welcome to the simple chatbot!", font=("Arial", 14))
        welcome_label.pack(pady=10)

        # Chat history display.
        self.chat_history = tk.Text(self, wrap=tk.WORD, state=tk.DISABLED, width=48, height=10)
        self.chat_history.pack(padx=10, pady=5)

        # Input field frame.
        input_frame = tk.Frame(self)
        input_frame.pack(padx=10, pady=5, fill=tk.X)

        self.user_entry = tk.Entry(input_frame, width=30, font=("Arial", 12))
        self.user_entry.pack(side=tk.LEFT, expand=True, fill=tk.X)
        self.user_entry.bind("<Return>", self.send_message)

        send_button = tk.Button(input_frame, text="Send", command=self.send_message)
        send_button.pack(side=tk.LEFT, padx=(5, 0))

        quit_button = tk.Button(self, text="Quit", command=self.on_quit)
        quit_button.pack(pady=(0, 10))

        self.insert_message("Chatbot", "Hello! Type a message and press Send.")

    def insert_message(self, sender: str, message: str) -> None:
        self.chat_history.configure(state=tk.NORMAL)
        self.chat_history.insert(tk.END, f"{sender}: {message}\n")
        self.chat_history.configure(state=tk.DISABLED)
        self.chat_history.see(tk.END)

    def send_message(self, event=None) -> None:
        user_text = self.user_entry.get()
        if not user_text.strip():
            return

        self.insert_message("You", user_text)
        self.user_entry.delete(0, tk.END)

        response = get_bot_response(user_text)
        self.insert_message("Chatbot", response)

        if user_text.strip().lower() in ["quit", "exit", "bye"]:
            self.after(500, self.destroy)

    def on_quit(self) -> None:
        if messagebox.askokcancel("Quit", "Do you want to close the chatbot?"):
            self.destroy()


if __name__ == "__main__":
    app = ChatbotGUI()
    app.mainloop()
