from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size=(450,600)





class Tutorials(MDApp):
    def build(self):
        return Builder.load_file('tutorial_1.kv')
