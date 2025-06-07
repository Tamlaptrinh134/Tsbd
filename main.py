from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Hello world'))
        layout.add_widget(Label(text='❤️ Unicode'))
        layout.add_widget(Label(text='Multi\nLine'))
        layout.add_widget(Label(text='Font size test', font_size='20sp'))
        return layout

MyApp().run()
