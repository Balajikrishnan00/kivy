from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

Window.size=(350,600)

LoginPage="""
MDFloatLayout:
    
    MDLabel:
        text:'Login Page'
        theme_text_color:'Custom'
        text_color:0,0,0,1
        pos_hint:{'center_y':.8}
        font_style:'H4'
        bold:True
        halign:'center'
    MDLabel:
        text:'Welcome'
        font_style:'H5'
        halign:'center'
        pos_hint:{'center_y':.7}
    MDTextField:
        id:email
        hint_text:'Enter Email'
        pos_hint:{'center_x':.5,'center_y':.6}
        current_hint_text_color:0,0,0,1
        size_hint_x:.84
    MDTextField:
        id:password
        hint_text:'Password'
        current_hint_text_color:0,0,0,1
        pos_hint:{'center_x':.5,'center_y':.45}
        size_hint_x:.84
        password:True
    MDRaisedButton:
        id:login
        text:'Login'
        pos_hint:{'center_x':.5,'center_y':.35}
        size_hint_x:.5
        theme_text_color:'Custom'
        text_color:1,1,1,1
        font_style:'H5'
        on_release:app.verifying( email.text, password.text )
        
        
        
        
"""



class Tutorials(MDApp):

    def build(self):
        self.theme_cls.primary_palette='Red'
        login=Builder.load_string(LoginPage)
        return login
    def verifying(self,email,password):
        if email=='welcome' and password=='123':
            print('welcome')
        else:
            print('incorrect email or password')

if __name__ == '__main__':
    Tutorials().run()
