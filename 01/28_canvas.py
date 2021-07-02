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
            pos:(100,100)
            size:(100,100)
        Rectangle:
            pos:(20,20)
            size:(20,20)
    Label:
        text:'Label1'
"""))
