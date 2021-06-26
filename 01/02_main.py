from kivy.app import App
from kivy.uix.label import Label

class myApp(App):
    def build(self):
        return Label(text='Hello world',font_size='20dp',color=(1,1,0,1),)

if __name__ == '__main__':
    myApp().run()
# Label(text='',font_size='',color=(,))
