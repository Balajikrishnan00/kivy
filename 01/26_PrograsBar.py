from kivy.base import runTouchApp
from kivy.base import Builder

runTouchApp(Builder.load_string("""
BoxLayout:

    orientation:'vertical'
    padding:30
    ProgressBar:
        max:70
        value:20
        
    
"""))