
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from nodes import *
import sys
from verse_lexer import lexicon
from verse_parser import Parser
from verse_interpreter import Interpreter
import start_text




class VerseInterpreterApp(App):
    def build(self):
        self.title = '* Verse Interpreter w/GUI * v1.0'
        self.icon = 'viip.png'
        self.root = BoxLayout(orientation='vertical')

        # Create the label with the provided text
        intro_text = """
        * Verse Interpreter w/GUI * v1.0
        A Verse programming sandbox independent of UEFN!
        Frontend & GUI by Cruz Wootten aka Lil Wikipedia
        Backend by Kariyampalli Christy & Turobin-Ort Marcel
        The interpreter was released under MIT license
        """
        self.intro_label = Label(text=intro_text, halign='center', valign='middle')
        self.intro_label.bind(size=self.intro_label.setter('text_size'))  # Ensures the text wraps within the label
        self.root.add_widget(self.intro_label)

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
        try:
            # Here you should call the function from your repository and update the output label
            input_text = self.input.text
            result = verse_input(input_text)
            self.output.text = result

            # lexer = lexicon(input_text)
            # parser = Parser(lexer)
            # interpreter = Interpreter(parser)
            #lexer.input = input_text
            #interpreter.reset()
            # result = interpreter.interpret()
            # self.output.text = repr(result)
            # print(repr(result))
        except Exception as e:
            self.output.text = f"Error: {str(e)}"
def verse_input(text):
    sys.setrecursionlimit(1000000)
    userverse = text

    lexer = lexicon(userverse)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    result = interpreter.interpret()
    return repr(result)

if __name__ == '__main__':
    VerseInterpreterApp().run()
