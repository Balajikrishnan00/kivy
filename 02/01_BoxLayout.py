from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyBoxlayout(App):
    def build(self):
        box=BoxLayout()
        box.orientation='vertical'
        box.padding=30
        box.spacing=10
        b1=Button(text='Button1',)
        b2=Button(text='Button2',)
        b3 =Button(text='Button3',)

        box.add_widget(b1)
        box.add_widget(b2)
        box.add_widget(b3)

        return box

if __name__ == '__main__':
    MyBoxlayout().run()