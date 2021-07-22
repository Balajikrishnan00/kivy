from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.textfield import MDTextFieldRect
Window.size=(320,600)

login="""

    
        
    
"""


class SingnUp(MDApp):
    def build(self):
        return Builder.load_string(login)
if __name__ == '__main__':
    SingnUp().run()