from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string("""
GridLayout:
    
    canvas:
        Color:
            rgb:1,0,10
        Ellipse:
            pos:self.pos
            size:self.size
        Rectangle:
            pos:self.pos
            size:self.size
    
    Label:
        text:'Label1'
        halign:'center'
"""))
