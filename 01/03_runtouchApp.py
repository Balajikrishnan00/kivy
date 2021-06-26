from kivy.base import runTouchApp
from kivy.lang.builder import Builder

runTouchApp(Builder.load_string(''' 
StackLayout:
    Label:
        text:'s1'
        font_size:'20dp'
        color:(0,1,0,1)
        
        pos_hint:{'center_x':.5,'center_y':.2}
        '''))