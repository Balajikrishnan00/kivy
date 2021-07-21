from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatIconButton

class keypad(MDBoxLayout):
    pass

class KeyPadAPP(MDApp):
    def build(self):
        return keypad()
KeyPadAPP().run()