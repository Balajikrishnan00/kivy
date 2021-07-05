from kivy.app import App
from kivy.base import Builder
kv="""
BoxLayout:
    orientation:"vertical"
    padding:30
    ProgressBar:
        id:bar
        max:slider.max
        value:slider.value
    Slider:
        id:slider
        max:200
        value:10
    Slider:
        #orientation:'vertical'
        max:slider.max
        value:slider.value
        on_value:slider.value=self.value
    
    
"""

class MainApp(App):
    def build(self):
        return Builder.load_string(kv)
MainApp().run()
