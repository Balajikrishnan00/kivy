from kivy.app import App
from kivy.uix.button import Button

class mainapp(App):
    def build(self):
        b1=Button(text='BUTTON 1',size_hint=(.2,.1),pos_hint={'x':.4},)

        return b1

if __name__ == '__main__':
    mainapp().run()

# pos_hint={'center_x':.5,'center_y':.5}
# size_hint=(.2,.1)
# size_hint_y=.3
# pos_hint={'x':value,'y':value}
#          {'top':value,'lift'=value} top,down : lift,right
