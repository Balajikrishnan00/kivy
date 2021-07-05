from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.base import Builder
kv="""
BoxLayout:
    Label:
        canvas.before:
            Color:
                rgb:1,1,1,1
            Rectangle:
                pos:self.pos
                size:self.size
        
        text:('Label 1')
        color:(1,0,0,1)
        font_size:32
        size_hint_y:None
        height:sp(60)
        
        
        
         
"""
class MyApp(App):
    def build(self):
        return Builder.load_string(kv)
MyApp().run()