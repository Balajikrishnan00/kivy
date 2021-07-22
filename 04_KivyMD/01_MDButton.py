from kivymd.app import MDApp
from kivy.lang import Builder
#from kivymd.uix.card import


Button="""
MDFloatLayout:
    MDIconButton:
        icon:'language-python'
        pos_hint:{'center_x':.1,'center_y':.9}
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
    MDFloatingActionButton:
        icon: "android"
        elevation_normal: 12
        pos_hint:{'center_x':.2,'center_y':.9}
    MDFlatButton:
        text: "MDFLATBUTTON"
        theme_text_color: "Custom"
        text_color: 0, 0, 1, 1
        pos_hint:{'center_x':.33,'center_y':.9}
    MDRaisedButton:
        text: "MDRAISEDBUTTON"
        md_bg_color: 1, 0, 1, 1
        pos_hint:{'center_x':.5,'center_y':.9}
    MDRectangleFlatButton:
        text: "MDRECTANGLEFLATBUTTON"
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        line_color: 0, 0, 1, 1
        pos_hint:{'center_x':.75,'center_y':.9}
    MDRectangleFlatIconButton:
        icon: "android"
        text: "MDRECTANGLEFLATICONBUTTON"
        theme_text_color: "Custom"
        text_color: 0, 0, 1, 1
        line_color: 1, 0, 1, 1
        icon_color: 1, 0, 0, 1
        pos_hint:{'center_x':.19,'center_y':.8}
    MDRoundFlatButton:
        text: "MDROUNDFLATBUTTON"
        text_color: 0, 1, 0, 1
        pos_hint:{'center_x':.50,'center_y':.8}
    MDRoundFlatIconButton:
        icon: "android"
        text: "MDROUNDFLATICONBUTTON"
        pos_hint:{'center_x':.8,'center_y':.8}
    MDFillRoundFlatButton:
        text:'MDFillRoundFlatButton'
        pos_hint:{'center_x':.12,'center_y':.7}
    MDFillRoundFlatIconButton:
        text:'MDFillRoundFlatIconButton'
        pos_hint:{'center_x':.4,'center_y':.7}
    MDTextButton:
        text: "MDTEXTBUTTON"
        custom_color: 0, 1, 0, 1
        pos_hint:{'center_x':.64,'center_y':.7}
    MDFloatingActionButtonSpeedDial:
        data: app.data
        root_button_anim: True
    MDLabel:
        text:'Buttons'
        halign:'center'
        
"""

class Mainbutton(MDApp):
    data = {
        'Python': 'language-python',
        'PHP': 'language-php',
        'C++': 'language-cpp',
    }
    def build(self):
        button=Builder.load_string(Button)
        return button


Mainbutton().run()