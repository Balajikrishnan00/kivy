from kivy.base import Builder
from kivy.base import runTouchApp

runTouchApp(Builder.load_string("""
BoxLayout:
    orientation:'vertical'
    size_hint_y:None
    #size_hint_x:None
    #pos_hint:{'center_x':.5,'center_y':.5}
    height:sp(200)
    
    Label:
        text:'Label1'
        font_size:30
    Button:
        text:'Button 1'
        
"""))