from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class mybox(BoxLayout):
    pass

class tesapp(App):
    def build(self):
        return mybox()
tesapp().run()