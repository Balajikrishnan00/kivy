from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.app import App
runTouchApp(Builder.load_string('''
Label:
    text:'Welcome'
    Button:
        text:'B1'
        size_hint:(.2,.1)
        pos:root.x,root.top-self.height
    Button:
        text:'B2'
        size_hint:(.2,.1)
        pos:root.right-self.width,root.y
    Button:
        text:'B3'
        size_hint:(.2,.1)
    Button:
        text:'B4'
        size_hint:(.2,.1)
        pos:root.x,root.top-self.width,root.y
      
    

'''))