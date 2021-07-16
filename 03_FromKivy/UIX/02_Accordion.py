from kivy.app import App
from kivy.base import Builder
from kivy.uix.boxlayout import BoxLayout


class MyBox(BoxLayout):
    pass

class MYApp(App):
    def build(self):
        Builder.load_file('02_Accordion.kv')
        return MyBox()
MYApp().run()