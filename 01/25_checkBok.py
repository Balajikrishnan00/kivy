from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.base import Builder

runTouchApp(Builder.load_string("""
GridLayout:
    cols:2
    Label:
        text:'Username'
    CheckBox:
        active:True
    Label:
        text:'Label2'
    CheckBox:
        group:'radio'
        active:True
        
        
"""))