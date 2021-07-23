from kivymd.app import MDApp
from kivy.lang import Builder

KV="""
MDFloatLayout:
    MDTextField:
        hint_text: "MDTextField"
        size_hint_x:.5
        pos_hint:{'center_x':.5,'center_y':.8}
    MDTextFieldRound:
        hint_text: "MDTextFieldRound"
        size_hint_x:.5
        pos_hint:{'center_x':.5,'center_y':.6}
    MDTextFieldRect:
        hint_text: "MDTextFieldRect"
        size_hint_y:.1
        size_hint_x:.5
        pos_hint:{'center_x':.5,'center_y':.4}
"""

class TextField(MDApp):
    def build(self):
        long=Builder.load_string(KV)
        return long
TextField().run()
