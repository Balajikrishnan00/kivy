from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty,BooleanProperty


class myBox(GridLayout):
    my_text = StringProperty('OFF')
    my_Label_Value = StringProperty('0')
    value = 0
    Toggle_Button=BooleanProperty(False)
    switch_Active=BooleanProperty(False)




    def minus(self):
        if self.Toggle_Button:
            if self.my_Label_Value == '0':
                return '0'
            else:
                self.value -= 1
                self.my_Label_Value = str(self.value)
        else:
            self.my_text='Click Here!'

    def plus(self):
        if self.Toggle_Button:


            self.value += 1
            self.my_Label_Value = str(self.value)
    def on_ToggleButton(self,widget):
        if widget.state=='normal':
            self.Toggle_Button=False
            widget.state='normal'
        else:
            self.Toggle_Button=True
            self.my_text='ON'
    def SwitchButton(self,widget):
        if widget.active:
            print(widget.active)
            self.switch_Active=True
        else:

            self.switch_Active=False





class TestApp(App):
    pass


TestApp().run()
