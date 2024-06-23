from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk, ImageDraw
import os, random
import pyttsx3
import json
from difflib import get_close_matches
import datetime
import sys


class ChatApp: 
    def __init__(self, master):
        self.master = master
        self.master.title("ELSA")
        
        self.message_list = []
        self.text_to_speech = False
        
        self.chat_frame = Frame(master, bg="#f0f0f0")
        self.chat_frame.pack(pady=10, padx=10)
        
        #Use image for bot icon
        self.profile_icon_bot = self.create_rounded_image("bot.png", 50)
      
        self.chat_text = Text(self.chat_frame, width=80, height=20, bg="#f0f0f0", fg="green", font=("Arial", 12))
        self.chat_text.pack(side=RIGHT, fill=BOTH)  
        
        self.scrollbar = Scrollbar(self.chat_frame, command=self.chat_text.yview)
        self.scrollbar.pack(side=LEFT, fill=Y)
        self.chat_text.config(yscrollcommand=self.scrollbar.set)
        
        self.message_entry = Entry(master, width=80, font=("Arial", 12))
        self.message_entry.pack(pady=10)
        self.message_entry.bind("<Return>", self.send_message)
        
        self.send_button = Button(master, text="Send", bg="#0084ff", fg="white", font=("Arial", 12), command=self.send_message)
        self.send_button.pack(pady=10)
        
        self.text_to_speech_button = Button(master, text="Text to Speech", bg="#0084ff", fg="white", font=("Arial", 12), command=self.toggle_text_to_speech)
        self.text_to_speech_button.pack(pady=10)
        
        self.clear_chat_button = Button(master, text="Clear Chat", bg="#ff0000", fg="white", font=("Arial", 12), command=self.clear_chat)
        self.clear_chat_button.pack(pady=10)

        #Path to json dataset
        with open('knowledge_base.json') as json_file:
            data = json.load(json_file)
        self.questions = {item['question']: item['answer'] for item in data['questions']}

    def display_user_message(self, message):
        self.chat_text.config(state=NORMAL)
        self.chat_text.insert(END, f"You :{message}\n", 'user_message')
        self.chat_text.tag_config('user_message', justify='right', foreground='green', background='white')
        self.chat_text.config(state=DISABLED)
        self.chat_text.see(END)

    def send_message(self, event=None):
        message = self.message_entry.get()
        if message:
            self.message_entry.delete(0, END)
            if message.lower() == "pic":
                self.send_image()
            else:
                self.display_user_message(message)
                self.receive_message(message)
        else:
            messagebox.showerror("Error", "Please enter a message.")
    
    def receive_message(self, message):
        if message.lower() == 'hi':
            response = "Hello"
        elif message.lower() == 'date':
            date = datetime.datetime.now()
            response = date.strftime("%x")
        elif message.lower() == 'time':
            date = datetime.datetime.now()
            response = date.strftime("%X")
        elif message.lower() == 'clear':
            self.clear_chat()
        elif message.lower() == 'bye':
            sys.exit()

        else:
            best_match = get_close_matches(message, self.questions.keys(), n=1, cutoff=0.8)
            if best_match:
                response = self.questions[best_match[0]]
            else:
                response = "Sorry, I didn't understand that."
        
        self.message_list.append((response))
        self.display_message(response, self.profile_icon_bot)
        if self.text_to_speech:
            self.speak_message(response)
        
    def send_image(self):
        image_folder = "img"
        image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
        if image_files:
            random_image = random.choice(image_files)
            image_path = os.path.join(image_folder, random_image)
            self.display_message("", self.profile_icon_bot , image_path)
        else:
            self.display_message("  No images found.", self.profile_icon_bot)
    
    def display_message(self, message, profile_icon, image_path=None):
        self.chat_text.config(state=NORMAL)
        self.chat_text.window_create(END, window=Label(self.chat_text, image=profile_icon))
        if image_path:
            image = Image.open(image_path)
            image = image.resize((200, 200))
            photo = ImageTk.PhotoImage(image)
            self.chat_text.image_create(END, image=photo)
            self.chat_text.image = photo
        self.chat_text.insert(END, f" {message}\n")
        
        self.chat_text.config(state=DISABLED)
        self.chat_text.see(END)
    
    def create_rounded_image(self, image_path, size):
        image = Image.open(image_path)
        image = image.resize((size, size))
        mask = Image.new("L", (size, size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size, size), fill=255)
        image.putalpha(mask)
        return ImageTk.PhotoImage(image)
    
    def toggle_text_to_speech(self):
        self.text_to_speech = not self.text_to_speech
        if self.text_to_speech:
            self.text_to_speech_button.config(text="Text to Speech ON")
        else:
            self.text_to_speech_button.config(text="Text to Speech OFF")
    
    def speak_message(self, message):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # Select a female voice
        engine.say(message)
        engine.runAndWait()
    
    def clear_chat(self):
        self.chat_text.config(state=NORMAL)
        self.chat_text.delete(1.0, END)
        self.chat_text.config(state=DISABLED)

root = Tk()
root.title("ELSA")
root.configure(bg="#f0f0f0")
chat_app = ChatApp(root)
root.mainloop()
