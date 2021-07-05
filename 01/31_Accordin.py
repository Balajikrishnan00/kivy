from kivy.app import App
from kivy.uix.accordion import Accordion,AccordionItem
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        a=Accordion()
        for x in range(5):
            Ai=AccordionItem(title='Title %d'%x,min_space=60)
            Ai.add_widget(Label(text='Label\n'*5))
            a.add_widget(Ai)
        return a
if __name__ == '__main__':
    MyApp().run()