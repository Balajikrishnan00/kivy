from kivy.app import App
from kivy.base import Builder
from kivy.core.window import Window
Window.size=(320,480)
kv= """

BoxLayout:
    orientation:'vertical'
    padding:10
    spacing:12
    TextInput:
        hint_text:'hello'
        
    TextInput:
    TextInput:
    TextInput:
    TextInput:
    Button:
        text:'Create An Account'
        
    Label:
        text:'Already have an Account?[b] Sign in[/b]'
        markup:True
        
    
    

"""


class MainApp(App):
    def build(self):
        return Builder.load_string(kv)
MainApp().run()