from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class MyAncharlayout(App):
    def build(self):
        # creating FloatLayout()
        float=FloatLayout()

        # creating AnchorLayout()
        anchar1 =  AnchorLayout()
        anchar2 = AnchorLayout()
        anchar3 = AnchorLayout()
        anchar4 = AnchorLayout()
        anchar5 = AnchorLayout()
        anchar6 = AnchorLayout()
        anchar7 = AnchorLayout()
        anchar8 = AnchorLayout()
        anchar9 = AnchorLayout()


        # anchor pos
        anchar1.anchor_x='left'
        anchar1.anchor_y='top'

        anchar2.anchor_x = 'center'
        anchar2.anchor_y = 'top'

        anchar3.anchor_x = 'right'
        anchar3.anchor_y = 'top'

        anchar4.anchor_x = 'left'
        anchar4.anchor_y = 'center'

        anchar5.anchor_x = 'center'
        anchar5.anchor_y = 'center'

        anchar6.anchor_x = 'right'
        anchar6.anchor_y = 'center'

        anchar7.anchor_x = 'left'
        anchar7.anchor_y = 'bottom'

        anchar8.anchor_x = 'center'
        anchar8.anchor_y = 'bottom'

        anchar9.anchor_x = 'right'
        anchar9.anchor_y = 'bottom'






        # creating Button
        b1=  Button(text='B1',size_hint=(.2,.1))
        b2 = Button(text='B2',size_hint=(.2,.1))
        b3 = Button(text='B3',size_hint=(.2,.1))
        b4 = Button(text='B4',size_hint=(.2,.1))
        b5 = Button(text='B5',size_hint=(.2,.1))
        b6 = Button(text='B6',size_hint=(.2,.1))
        b7 = Button(text='B7',size_hint=(.2,.1))
        b8 = Button(text='B8',size_hint=(.2,.1))
        b9=  Button(text='B9',size_hint=(.2,.1))

        # add_widget buttons in anchor var
        anchar1.add_widget(b1)
        anchar2.add_widget(b2)
        anchar3.add_widget(b3)
        anchar4.add_widget(b4)
        anchar5.add_widget(b5)
        anchar6.add_widget(b6)
        anchar7.add_widget(b7)
        anchar8.add_widget(b8)
        anchar9.add_widget(b9)


        # add_widget anchor in float
        float.add_widget(anchar1)
        float.add_widget(anchar2)
        float.add_widget(anchar3)
        float.add_widget(anchar4)
        float.add_widget(anchar5)
        float.add_widget(anchar6)
        float.add_widget(anchar7)
        float.add_widget(anchar8)
        float.add_widget(anchar9)

        return float
MyAncharlayout().run()