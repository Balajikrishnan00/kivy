from kivymd.app import MDApp
from kivy.lang import Builder

kv="""
MDScreen:
    MDCard:
        size:None,None
        size:'300dp','500dp'
        pos_hint:{"center_x":.5,'center_y':5}
        MDLabel:
            text:"LOGIN"
            halign:"center"
        
             
"""

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(kv)
MainApp().run()
