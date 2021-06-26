from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class class2(BoxLayout):
    def __init__(self,**kwargs):
        super(class2, self).__init__(**kwargs)
        self.orientation='vertical'
        self.padding=(20,10)
        self.btn1=Button(text='Button1')
        self.btn2=Button(text='Button2')
        self.add_widget(self.btn1)
        self.add_widget(self.btn2)




class myApp(App):
    def build(self):
        return class2()

if __name__ == '__main__':
    myApp().run()