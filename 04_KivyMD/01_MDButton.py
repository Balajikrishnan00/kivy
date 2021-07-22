from kivymd.app import MDApp
from kivy.lang import Builder


Button="""
MDFloatLayout:
    orientation:'vertical'
    #cols:2
    MDFillRoundFlatButton:
        text:'MDFillRoundFlatButton'
    MDFillRoundFlatIconButton:
        text:'MDFillRoundFlatIconButton'
    MDFlatButton:
        text:'MDFlatButton'
    MDFloatingActionButton:
        text:'MDFloatingActionButton'
    MDFloatingActionButtonSpeedDial:
        text:'MDFloatingActionButtonSpeedDial'
    MDFloatingBottomButton:
        text:'MDFloatingBottomButton'
    MDFloatingLabel:
        text:'MDFloatingLabel'
    MDFloatingRootButton:
        text:'MDFloatingRootButton'
    MDIconButton:
        text:'MDIconButton'
    MDRaisedButton:
        text:'MDRaisedButton'
    MDRectangleFlatButton:
        text:'MDRectangleFlatButton'
    MDRectangleFlatIconButton:
        text:'MDRectangleFlatIconButton'
    MDRoundFlatButton:
        text:'MDRoundFlatButton'
    MDRoundFlatIconButton:
        text:'MDRoundFlatIconButton'
    MDTextButton:
        text:'MDTextButton'
        
    
    
    
    
    
"""

class Mainbutton(MDApp):
    def build(self):
        button=Builder.load_string(Button)
        return button
Mainbutton().run()