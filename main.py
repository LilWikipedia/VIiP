from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import sys
from verse_lexer import lexicon
from verse_parser import Parser
from verse_interpreter import Interpreter
from nodes import *
import start_text
import nodes

class VerseInterpreterApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical')
        
        self.input = TextInput(hint_text='Enter text here', multiline=True)
        self.root.add_widget(self.input)
        
        self.output = Label(text='Output will be shown here', halign='left', valign='top')
        self.output.bind(size=self.output.setter('text_size'))  # Ensures the text wraps within the label
        self.root.add_widget(self.output)
        
        self.button = Button(text='Interpret')
        self.button.bind(on_press=self.on_button_press)
        self.root.add_widget(self.button)
        
        return self.root
    
    def on_button_press(self, instance):
        # Here you should call the function from your repository and update the output label
        input_text = self.input.text
        lexer = lexicon(input_text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()
        return self.output.text(result)
        #  = result



if __name__ == '__main__':
    VerseInterpreterApp().run()
