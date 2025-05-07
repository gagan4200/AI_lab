import tkinter as tk

# Simple response function
def get_response(msg):
    if "hi" in msg or "hello" in msg:
        return "Hello! Welcome to our restaurant. How can I assist you today?"
    elif "menu" in msg:
        return "You can view our menu on our website or I can send you today's specials."
    elif "reservation" in msg:
        return "Sure! For what date and time would you like to make a reservation?"
    elif "hours" in msg or "open" in msg:
        return "We're open from 10 AM to 10 PM, Monday through Sunday."
    elif "location" in msg:
        return "We're located at 123 Foodie Lane, Gourmet City."
    elif "bye" in msg:
        return "Goodbye! We hope to see you soon."
    else:
        return "sorry ,i didn't understand your question about our restaurant?"

# Function to handle sending message
def send():
    user_msg = entry.get()
    chat.insert(tk.END, "You: " + user_msg + "\n")
    # response = get_response(user_msg.lower())
    chat.insert(tk.END, "Bot: " + get_response(user_msg) + "\n\n")
    entry.delete(0, tk.END)

# GUI setup
window = tk.Tk()
window.title("Simple Chatbot")

chat = tk.Text(window, height=20, width=50)
chat.pack()

entry = tk.Entry(window, width=40)
entry.pack(side=tk.LEFT, padx=10)

send_button = tk.Button(window, text="Send", command=send)
send_button.pack(side=tk.LEFT)

window.mainloop()