from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.base import Builder
kv='''
BoxLayout:
    orientation:'vertical'
    padding:(20,10)
    Button:
        text:'Button1'
    Button:
        text:'Button2'
    '''

class mainApp(App):
    def build(self):
        return Builder.load_string(kv)
if __name__ == '__main__':
    mainApp().run()