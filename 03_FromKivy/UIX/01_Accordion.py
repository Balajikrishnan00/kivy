from kivy.app import App
from kivy.uix.accordion import Accordion,AccordionItem
from kivy.uix.label import Label

class MyAccordion(Accordion):
    def __init__(self,**kwargs):
        super(MyAccordion, self).__init__(**kwargs)
        self.orientation='vertical'
        self.A_item=AccordionItem(title='HTML')
        self.A_item.add_widget(Label(text='People often think it is extremely difficult'))
        self.add_widget(self.A_item)

        self.A_item = AccordionItem(title='CSS')
        self.A_item.add_widget(Label(text='People often think it is extremely difficult'))
        self.add_widget(self.A_item)

        self.A_item = AccordionItem(title='Java')
        self.A_item.add_widget(Label(text='People often think it is extremely difficult'))
        self.add_widget(self.A_item)

        self.A_item = AccordionItem(title='Python')
        self.A_item.add_widget(Label(text='People often think it is extremely difficult'))
        self.add_widget(self.A_item)



class mainApp(App):
    def build(self):
        return MyAccordion()
mainApp().run()