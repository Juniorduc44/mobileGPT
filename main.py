# Version 0.0.2
import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
model_id = 'gpt-3.5-turbo'

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import openai
from plyer import filechooser

class ChatApp(App):
    def build(self):
        openai.api_key = openai.api_key
        self.messages = [{'role': 'system', 'content': 'You are talking to GPT-3.5 assistant.'}]

        # Root Layout
        self.layout = BoxLayout(orientation='vertical')

        # Display Area
        self.display_area = TextInput(readonly=True, size_hint=(1, 0.8))
        self.layout.add_widget(self.display_area)

        # Input Area
        self.input_area = TextInput(size_hint=(1, 0.1))
        self.layout.add_widget(self.input_area)

        # Send Button
        self.send_button = Button(text='Send', size_hint=(1, 0.1))
        self.send_button.bind(on_press=self.send_message)
        self.layout.add_widget(self.send_button)

        # Save Button
        self.save_button = Button(text='Save Conversation', size_hint=(1, 0.1))
        self.save_button.bind(on_press=self.save_conversation)
        self.layout.add_widget(self.save_button)

        return self.layout

    def send_message(self, event):
        user_message = self.input_area.text
        self.display_area.text += f'User: {user_message}\n'
        self.input_area.text = ''
        self.messages.append({'role': 'user', 'content': user_message})

        # Call to the GPT-3.5 API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Replace with actual model name if different
            messages=self.messages
        )

        bot_response = response['choices'][0]['message']['content']
        self.messages.append({'role': 'assistant', 'content': bot_response})

        self.display_area.text += f'Bot: {bot_response}\n'

    def save_conversation(self, event):
        filepath = filechooser.save_file(title="Save Conversation", filters=[("Text files", "*.txt")])
        if filepath:
            with open(filepath[0], 'w') as output_file:
                output_file.write(self.display_area.text)

if __name__ == '__main__':
    ChatApp().run()
