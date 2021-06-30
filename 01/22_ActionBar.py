from kivy.base import runTouchApp
from kivy.base import Builder
from kivy.core.window import Window
Window.size=(320,480)

runTouchApp(Builder.load_string("""
ActionBar:
    pos_hint:{'top':1}
    ActionView:
        ActionPrevious:
            title:'Action Bar'
            with_previous:False
        ActionButton:
            text:'B1'
        ActionButton:
            text:'B2'
        ActionButton:
            text:'B3'
        ActionButton:
            text:'B4'
            
        
        
    
"""))
