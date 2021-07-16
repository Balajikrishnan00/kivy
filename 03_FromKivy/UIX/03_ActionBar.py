"""
from kivy.app import App
#from kivy.uix.actionbar import ActionBar,ActionView
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

class User_actionbar(BoxLayout):
    pass

class MainApp(App):
    def build(self):
        Builder.load_file('03_ActionBar.kv')
        return User_actionbar()
MainApp().run()
"""
from kivy.uix.actionbar import ActionBar
#print(dir(ActionBar))
help(ActionBar)