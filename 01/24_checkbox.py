from kivy.base import runTouchApp
from kivy.base import Builder

runTouchApp(Builder.load_string("""
GridLayout:
    rows:1
    size_hint_x:None
    size_hint_y:None
    background_color:(1,0,0,)
    pos_hint:{'center_x':.5,'center_y':.5}
    cols:2
    Label:
        text:'Username'
    CheckBox:
        active:True 
    
"""))