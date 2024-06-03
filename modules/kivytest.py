
import kivy_deps
for importer, modname, ispkg in pkgutil.iter_modules(kivy_deps.__path__):
        if not ispkg:
            continue
        if modname.startswith('gst'):
            _packages.insert(0, (importer, modname, 'kivy_deps'))
        else:
            _packages.append((importer, modname, 'kivy_deps'))

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='Hello, Kivy!')

if __name__ == '__main__':
    MyApp().run()